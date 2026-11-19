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
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    // Start the Python API with the window. It is stopped on the Exit event, because the event loop
    // can end the process without running destructors.
    let mut api = backend::Backend::start();
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::get_runtime_info,
            commands::run_rust_agent
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
