pub fn evaluate_ab_stats(input: &str) -> String {
    format!("[evaluate_ab_stats] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-ab-test-interpreter:gemini-4-hydrogen:low] {}", evaluate_ab_stats(input))
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
        assert!(out.contains("03-ab-test-interpreter"));
        assert!(out.contains("evaluate_ab_stats"));
    }
}
