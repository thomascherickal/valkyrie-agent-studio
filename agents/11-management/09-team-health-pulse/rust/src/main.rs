pub fn evaluate_dora_tier(input: &str) -> String {
    format!("[evaluate_dora_tier] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-team-health-pulse:gemini-4-hydrogen:low] {}", evaluate_dora_tier(input))
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
        assert!(out.contains("09-team-health-pulse"));
        assert!(out.contains("evaluate_dora_tier"));
    }
}
