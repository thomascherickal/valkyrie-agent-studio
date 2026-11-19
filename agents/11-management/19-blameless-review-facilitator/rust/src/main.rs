pub fn run_blameless_review(input: &str) -> String {
    format!("[run_blameless_review] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-blameless-review-facilitator:gemini-4-hydrogen:low] {}", run_blameless_review(input))
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
        assert!(out.contains("19-blameless-review-facilitator"));
        assert!(out.contains("run_blameless_review"));
    }
}
