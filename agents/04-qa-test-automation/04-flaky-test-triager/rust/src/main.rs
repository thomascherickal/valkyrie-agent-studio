pub fn classify_flakiness(input: &str) -> String {
    format!("[classify_flakiness] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-flaky-test-triager:gemini-4-hydrogen:low] {}", classify_flakiness(input))
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
        assert!(out.contains("04-flaky-test-triager"));
        assert!(out.contains("classify_flakiness"));
    }
}
