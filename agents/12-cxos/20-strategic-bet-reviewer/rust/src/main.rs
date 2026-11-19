pub fn review_strategic_bet(input: &str) -> String {
    format!("[review_strategic_bet] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-strategic-bet-reviewer:gemini-4-hydrogen:low] {}", review_strategic_bet(input))
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
        assert!(out.contains("20-strategic-bet-reviewer"));
        assert!(out.contains("review_strategic_bet"));
    }
}
