pub fn synthesize_feedback(input: &str) -> String {
    format!("[synthesize_feedback] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-perf-review-synthesizer:gemini-4-hydrogen:low] {}", synthesize_feedback(input))
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
        assert!(out.contains("05-perf-review-synthesizer"));
        assert!(out.contains("synthesize_feedback"));
    }
}
