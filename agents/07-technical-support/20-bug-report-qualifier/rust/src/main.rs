pub fn qualify_bug_report(input: &str) -> String {
    format!("[qualify_bug_report] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-bug-report-qualifier:gemini-4-hydrogen:low] {}", qualify_bug_report(input))
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
        assert!(out.contains("20-bug-report-qualifier"));
        assert!(out.contains("qualify_bug_report"));
    }
}
