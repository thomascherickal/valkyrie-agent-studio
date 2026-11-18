pub fn rank_ai_roi(input: &str) -> String {
    format!("[rank_ai_roi] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-ai-transformation-advisor:gemini-4-hydrogen:low] {}", rank_ai_roi(input))
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
        assert!(out.contains("05-ai-transformation-advisor"));
        assert!(out.contains("rank_ai_roi"));
    }
}
