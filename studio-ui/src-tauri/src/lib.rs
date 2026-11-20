//! Tauri Rust desktop shell exposing native Valkyrie runtime commands.

pub mod backend;
pub mod plan;
pub mod sidecar;

use serde::Serialize;
use valkyrie_rust_runtime::{mock_llm::MockGeminiAgent, AgentResult, ValkyrieAgent};

#[derive(Debug, Serialize, PartialEq)]
pub struct RuntimeInfo {
    pub shell: &'static str,
    pub platform: &'static str,
    pub arch: &'static str,
    pub default_model: &'static str,
    pub thinking_level: &'static str,
}

pub mod commands {
    use super::*;

    #[tauri::command]
    pub fn get_runtime_info() -> RuntimeInfo {
        RuntimeInfo {
            shell: "tauri-rust",
            platform: std::env::consts::OS,
            arch: std::env::consts::ARCH,
            default_model: "gemini-4-hydrogen",
            thinking_level: "low",
        }
    }

    #[tauri::command]
    pub fn run_rust_agent(agent_id: String, prompt: String) -> AgentResult {
        let agent = MockGeminiAgent::new(&agent_id);
        agent.execute(&prompt)
    }

    /// Synchronize native window and GTK widget theme (including `<select>` popups on Linux)
    /// with the Studio's selected theme mode (`"light"`, `"dark"`, or `"system"`).
    #[tauri::command]
    pub fn set_window_theme(window: tauri::WebviewWindow, mode: String) {
        let theme = match mode.as_str() {
            "light" => Some(tauri::Theme::Light),
            "dark" => Some(tauri::Theme::Dark),
            _ => None,
        };
        let _ = window.set_theme(theme);

        #[cfg(target_os = "linux")]
        {
            use gtk::prelude::*;
            let mode_clone = mode.clone();
            let _ = window.run_on_main_thread(move || {
                if let Some(settings) = gtk::Settings::default() {
                    let current = settings
                        .gtk_theme_name()
                        .map(|s| s.to_string())
                        .unwrap_or_default();
                    match mode_clone.as_str() {
                        "light" => {
                            settings.set_gtk_application_prefer_dark_theme(false);
                            let light_theme = if let Some(base) = current.strip_suffix("-Dark") {
                                format!("{base}-Light")
                            } else if let Some(base) = current.strip_suffix("-dark") {
                                base.to_string()
                            } else {
                                current.clone()
                            };
                            if !light_theme.is_empty() && light_theme != current {
                                settings.set_gtk_theme_name(Some(&light_theme));
                            }
                        }
                        "dark" => {
                            settings.set_gtk_application_prefer_dark_theme(true);
                            let dark_theme = if let Some(base) = current.strip_suffix("-Light") {
                                format!("{base}-Dark")
                            } else if !current.is_empty()
                                && !current.ends_with("-Dark")
                                && !current.ends_with("-dark")
                                && std::path::Path::new(&format!("/usr/share/themes/{current}-dark")).exists()
                            {
                                format!("{current}-dark")
                            } else {
                                current.clone()
                            };
                            if !dark_theme.is_empty() && dark_theme != current {
                                settings.set_gtk_theme_name(Some(&dark_theme));
                            }
                        }
                        _ => {
                            settings.reset_property("gtk-application-prefer-dark-theme");
                            settings.reset_property("gtk-theme-name");
                        }
                    }
                }
            });
        }
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    // Start the Python API with the window. It is stopped on the Exit event, because the event loop
    // can end the process without running destructors.
    let mut api = backend::Backend::start();
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::get_runtime_info,
            commands::run_rust_agent,
            commands::set_window_theme
        ])
        .build(tauri::generate_context!())
        .expect("error while building Valkyrie Tauri desktop shell")
        .run(move |_app, event| {
            if let tauri::RunEvent::Exit = event {
                api.stop();
            }
        });
}

#[cfg(test)]
mod tests {
    use super::commands::*;

    #[test]
    fn test_tauri_commands() {
        let info = get_runtime_info();
        assert_eq!(info.shell, "tauri-rust");
        assert_eq!(info.default_model, "gemini-4-hydrogen");
        assert_eq!(info.thinking_level, "low");

        let res = run_rust_agent("01-prd-architect".into(), "Draft SSO PRD".into());
        assert!(res.content.contains("01-prd-architect"));
        assert!(res.content.contains("Draft SSO PRD"));
        assert!(res.cost_usd > 0.0);
    }
}
