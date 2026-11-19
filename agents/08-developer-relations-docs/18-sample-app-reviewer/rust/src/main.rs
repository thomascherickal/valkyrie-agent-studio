pub fn review_sample_app(input: &str) -> String {
    format!("[review_sample_app] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-sample-app-reviewer:gemini-4-hydrogen:low] {}", review_sample_app(input))
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
        assert!(out.contains("18-sample-app-reviewer"));
        assert!(out.contains("review_sample_app"));
    }
}
