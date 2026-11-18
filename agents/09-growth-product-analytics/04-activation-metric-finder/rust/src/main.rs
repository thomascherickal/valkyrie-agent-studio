pub fn rank_activation_signals(input: &str) -> String {
    format!("[rank_activation_signals] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-activation-metric-finder:gemini-4-hydrogen:low] {}", rank_activation_signals(input))
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
        assert!(out.contains("04-activation-metric-finder"));
        assert!(out.contains("rank_activation_signals"));
    }
}
