pub fn score_partnership(input: &str) -> String {
    format!("[score_partnership] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-partnership-evaluator:gemini-4-hydrogen:low] {}", score_partnership(input))
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
        assert!(out.contains("15-partnership-evaluator"));
        assert!(out.contains("score_partnership"));
    }
}
