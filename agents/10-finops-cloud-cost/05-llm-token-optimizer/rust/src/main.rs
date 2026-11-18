pub fn recommend_model_tier(input: &str) -> String {
    format!("[recommend_model_tier] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-llm-token-optimizer:gemini-4-hydrogen:low] {}", recommend_model_tier(input))
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
        assert!(out.contains("05-llm-token-optimizer"));
        assert!(out.contains("recommend_model_tier"));
    }
}
