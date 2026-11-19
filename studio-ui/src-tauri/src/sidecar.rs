//! The API shipped inside an installer: a PyInstaller binary named `valkyrie-api` placed beside the app executable.
//! Build it with `make sidecar`; `make package` then lets Tauri bundle it.

use std::path::{Path, PathBuf};

/// The file name of the bundled API on this operating system.
pub fn file_name() -> &'static str {
    if cfg!(windows) {
        "valkyrie-api.exe"
    } else {
        "valkyrie-api"
    }
}

/// The bundled API inside `exe_dir`, when it is there.
pub fn find(exe_dir: &Path, exists: &dyn Fn(&Path) -> bool) -> Option<PathBuf> {
    let candidate = exe_dir.join(file_name());
    exists(&candidate).then_some(candidate)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn the_file_name_follows_the_operating_system() {
        assert_eq!(file_name().ends_with(".exe"), cfg!(windows));
        assert!(file_name().starts_with("valkyrie-api"));
    }

    #[test]
    fn finds_the_binary_only_when_it_exists() {
        let found = find(Path::new("/opt/studio"), &|p| p == Path::new("/opt/studio").join(file_name()));
        assert_eq!(found, Some(Path::new("/opt/studio").join(file_name())));
        assert_eq!(find(Path::new("/opt/studio"), &|_| false), None);
    }
}
