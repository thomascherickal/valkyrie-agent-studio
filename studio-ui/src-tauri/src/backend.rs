//! Starts the Python API alongside the desktop window and stops it on exit.
//!
//! What to start (the bundled API in an installed app, the venv's uvicorn in development) is decided in `plan`.
//! A running API on the port is detected and reused.

use std::net::{SocketAddr, TcpStream};
use std::process::{Child, Command, Stdio};
use std::time::Duration;

use crate::plan::{default_plan, Plan};

pub const API_ADDR: &str = "127.0.0.1:8000";

pub fn is_up(addr: &SocketAddr) -> bool {
    TcpStream::connect_timeout(addr, Duration::from_millis(200)).is_ok()
}

/// Owns the API process we started, if any. Dropping it stops the process.
pub struct Backend(Option<Child>);

impl Backend {
    /// Reuses an API already listening on `addr`. Otherwise spawns one. A failed spawn is logged, not fatal.
    pub fn start_with(addr: &SocketAddr, plan: &Plan) -> Backend {
        if is_up(addr) {
            return Backend(None);
        }
        let spawned = Command::new(&plan.program)
            .args(&plan.args)
            .current_dir(&plan.cwd)
            .stdin(Stdio::null())
            .spawn();
        match spawned {
            Ok(child) => Backend(Some(child)),
            Err(err) => {
                eprintln!("Could not start the Valkyrie API ({}): {err}. Start it with `make run-gui`.", plan.program.display());
                Backend(None)
            }
        }
    }

    pub fn start() -> Backend {
        Backend::start_with(&API_ADDR.parse().expect("valid address"), &default_plan())
    }

    /// Stops the API process we started. Returns false when there was nothing to stop.
    pub fn stop(&mut self) -> bool {
        match self.0.take() {
            Some(mut child) => {
                let _ = child.kill();
                let _ = child.wait();
                true
            }
            None => false,
        }
    }
}

impl Drop for Backend {
    fn drop(&mut self) {
        self.stop();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::net::TcpListener;
    use std::sync::{Mutex, MutexGuard};

    // Tests that bind ports must not overlap: a port one test just released could be handed to another.
    static PORTS: Mutex<()> = Mutex::new(());

    fn serial() -> MutexGuard<'static, ()> {
        PORTS.lock().unwrap_or_else(|poisoned| poisoned.into_inner())
    }

    fn closed_addr() -> SocketAddr {
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        listener.local_addr().unwrap() // the listener drops here, so nothing is listening
    }

    fn sleeper() -> Plan {
        Plan { program: "sleep".into(), args: vec!["30".into()], cwd: ".".into() }
    }

    #[test]
    fn is_up_detects_a_listener() {
        let _guard = serial();
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        assert!(is_up(&listener.local_addr().unwrap()));
        assert!(!is_up(&closed_addr()));
    }

    #[test]
    fn reuses_a_running_api() {
        let _guard = serial();
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        let mut backend = Backend::start_with(&listener.local_addr().unwrap(), &sleeper());
        assert!(!backend.stop(), "nothing was spawned, so nothing to stop");
    }

    #[test]
    fn spawns_and_stops_when_the_api_is_down() {
        let _guard = serial();
        let mut backend = Backend::start_with(&closed_addr(), &sleeper());
        assert!(backend.stop());
        assert!(!backend.stop());
    }

    #[test]
    fn a_failed_spawn_is_not_fatal() {
        let _guard = serial();
        let missing = Plan { program: "/no/such/python".into(), args: vec![], cwd: ".".into() };
        let mut backend = Backend::start_with(&closed_addr(), &missing);
        assert!(!backend.stop());
    }

    #[test]
    fn start_returns_a_backend() {
        let _guard = serial();
        drop(Backend::start()); // reuses or spawns, then stops whatever it started
    }

    /// End to end: starts the real API, waits until it listens, then stops it.
    /// Needs studio-core/.venv, so run it with `cargo test -p valkyrie-studio-tauri -- --ignored`.
    #[test]
    #[ignore = "needs studio-core/.venv with the API dependencies installed"]
    fn starts_the_real_api_and_stops_it() {
        let _guard = serial();
        let addr: SocketAddr = API_ADDR.parse().unwrap();
        assert!(!is_up(&addr), "port 8000 is busy: stop the running API first");
        let mut backend = Backend::start_with(&addr, &default_plan());
        let up = (0..100).any(|_| {
            std::thread::sleep(Duration::from_millis(100));
            is_up(&addr)
        });
        assert!(up, "the API never started listening");
        assert!(backend.stop());
        std::thread::sleep(Duration::from_millis(300));
        assert!(!is_up(&addr), "the API kept running after stop");
    }
}
