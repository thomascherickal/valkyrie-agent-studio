pub fn audit_wcag_aa(input: &str) -> String {
    format!("[audit_wcag_aa] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-accessibility-auditor:gemini-4-hydrogen:low] {}", audit_wcag_aa(input))
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
        assert!(out.contains("08-accessibility-auditor"));
        assert!(out.contains("audit_wcag_aa"));
    }
}
