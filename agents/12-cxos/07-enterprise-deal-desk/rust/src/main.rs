pub fn score_deal_margin(input: &str) -> String {
    format!("[score_deal_margin] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-enterprise-deal-desk:gemini-4-hydrogen:low] {}", score_deal_margin(input))
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
        assert!(out.contains("07-enterprise-deal-desk"));
        assert!(out.contains("score_deal_margin"));
    }
}
