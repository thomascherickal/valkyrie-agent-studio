pub fn draft_status_update(input: &str) -> String {
    format!("[draft_status_update] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-status-page-updater:gemini-4-hydrogen:low] {}", draft_status_update(input))
}

fn main() {
    println!("{}", run_agent("sample"));
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_run() {
        let out = run_agent("verify");
        assert!(out.contains("10-status-page-updater"));
        assert!(out.contains("draft_status_update"));
    }
}
