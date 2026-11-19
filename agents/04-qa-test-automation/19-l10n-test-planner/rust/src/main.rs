pub fn plan_locale_tests(input: &str) -> String {
    format!("[plan_locale_tests] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-l10n-test-planner:gemini-4-hydrogen:low] {}", plan_locale_tests(input))
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
        assert!(out.contains("19-l10n-test-planner"));
        assert!(out.contains("plan_locale_tests"));
    }
}
