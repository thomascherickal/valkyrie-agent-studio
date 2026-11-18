pub fn score_sla_risk(input: &str) -> String {
    format!("[score_sla_risk] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-sla-breach-predictor:gemini-4-hydrogen:low] {}", score_sla_risk(input))
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
        assert!(out.contains("05-sla-breach-predictor"));
        assert!(out.contains("score_sla_risk"));
    }
}
