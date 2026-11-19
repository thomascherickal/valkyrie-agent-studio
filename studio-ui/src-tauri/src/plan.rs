//! Decides how to start the API: the bundled sidecar when the app is installed, else the development interpreter.
//!
//! ponytail: in development the repo root is fixed at compile time. Set VALKYRIE_PYTHON to choose the interpreter,
//! or start the API yourself: a running API on the port is detected and reused.

use std::path::{Path, PathBuf};

use crate::sidecar;

#[derive(Debug, PartialEq)]
pub struct Plan {
    pub program: PathBuf,
    pub args: Vec<String>,
    pub cwd: PathBuf,
}

/// Development: VALKYRIE_PYTHON if set, else the repo's venv python when it exists, else `python3`.
pub fn dev_plan(repo_root: &Path, python_override: Option<String>, venv_python_exists: bool) -> Plan {
    let core = repo_root.join("studio-core");
    let venv_python = if cfg!(windows) {
        core.join(".venv/Scripts/python.exe")
    } else {
        core.join(".venv/bin/python")
    };
    let program = match python_override {
        Some(path) => PathBuf::from(path),
        None if venv_python_exists => venv_python,
        None => PathBuf::from("python3"),
    };
    let args = ["-m", "uvicorn", "valkyrie.api_server:app", "--port", "8000"];
    Plan { program, args: args.iter().map(|a| a.to_string()).collect(), cwd: core }
}

/// An installed app: run the bundled API from the folder it sits in. It keeps its data in the user's folder.
pub fn sidecar_plan(program: PathBuf) -> Plan {
    let cwd = program.parent().map(Path::to_path_buf).unwrap_or_else(|| PathBuf::from("."));
    Plan { program, args: vec![], cwd }
}

/// The bundled API beside `exe_dir` if there is one, else whatever `dev` builds.
pub fn choose(exe_dir: Option<&Path>, exists: &dyn Fn(&Path) -> bool, dev: impl FnOnce() -> Plan) -> Plan {
    match exe_dir.and_then(|dir| sidecar::find(dir, exists)) {
        Some(program) => sidecar_plan(program),
        None => dev(),
    }
}

/// The plan for this machine, read from the environment and the file system.
pub fn default_plan() -> Plan {
    let exe_dir = std::env::current_exe().ok().and_then(|exe| exe.parent().map(Path::to_path_buf));
    choose(exe_dir.as_deref(), &|path| path.is_file(), || {
        let root = Path::new(env!("CARGO_MANIFEST_DIR")).join("../..");
        let venv_exists = root.join("studio-core/.venv").is_dir();
        dev_plan(&root, std::env::var("VALKYRIE_PYTHON").ok(), venv_exists)
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn dev_plan_prefers_override_then_venv_then_python3() {
        let root = Path::new("/repo");
        assert_eq!(dev_plan(root, Some("/opt/py".into()), true).program, PathBuf::from("/opt/py"));
        let venv = dev_plan(root, None, true);
        assert!(venv.program.starts_with("/repo/studio-core/.venv"));
        assert_eq!(dev_plan(root, None, false).program, PathBuf::from("python3"));
        assert_eq!(venv.cwd, PathBuf::from("/repo/studio-core"));
        assert_eq!(venv.args, ["-m", "uvicorn", "valkyrie.api_server:app", "--port", "8000"]);
    }

    #[test]
    fn the_sidecar_runs_from_its_own_folder_with_no_arguments() {
        let plan = sidecar_plan(PathBuf::from("/opt/studio/valkyrie-api"));
        assert_eq!(plan.cwd, PathBuf::from("/opt/studio"));
        assert!(plan.args.is_empty());
        assert_eq!(sidecar_plan(PathBuf::from("/")).cwd, PathBuf::from(".")); // a path with no folder falls back to here
    }

    fn dev() -> Plan {
        dev_plan(Path::new("/repo"), None, false)
    }

    #[test]
    fn an_installed_app_uses_the_bundled_api_and_a_checkout_does_not() {
        let installed = choose(Some(Path::new("/opt/studio")), &|_| true, dev);
        assert_eq!(installed.program, Path::new("/opt/studio").join(sidecar::file_name()));
        assert!(installed.args.is_empty());
        assert_eq!(choose(Some(Path::new("/opt/studio")), &|_| false, dev), dev());
        assert_eq!(choose(None, &|_| true, dev), dev()); // no executable folder known
    }

    #[test]
    fn default_plan_runs_uvicorn_from_studio_core_when_nothing_is_bundled() {
        let plan = default_plan();
        assert!(plan.cwd.ends_with("studio-core"));
        assert!(plan.args.contains(&"uvicorn".to_string()));
    }
}
