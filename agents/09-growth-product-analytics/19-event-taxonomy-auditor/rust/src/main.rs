pub fn audit_event_names(input: &str) -> String {
    format!("[audit_event_names] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-event-taxonomy-auditor:gemini-4-hydrogen:low] {}", audit_event_names(input))
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
        assert!(out.contains("19-event-taxonomy-auditor"));
        assert!(out.contains("audit_event_names"));
    }
}
