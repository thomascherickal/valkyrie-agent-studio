pub fn audit_tags(input: &str) -> String {
    format!("[audit_tags] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-tagging-policy-auditor:gemini-4-hydrogen:low] {}", audit_tags(input))
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
        assert!(out.contains("14-tagging-policy-auditor"));
        assert!(out.contains("audit_tags"));
    }
}
