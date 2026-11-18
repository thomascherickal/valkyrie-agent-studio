pub fn distill_decision_memo(input: &str) -> String {
    format!("[distill_decision_memo] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-tech-strategy-summarizer:gemini-4-hydrogen:low] {}", distill_decision_memo(input))
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
        assert!(out.contains("08-tech-strategy-summarizer"));
        assert!(out.contains("distill_decision_memo"));
    }
}
