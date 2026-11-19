pub fn rank_noisy_alerts(input: &str) -> String {
    format!("[rank_noisy_alerts] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-alert-noise-reducer:gemini-4-hydrogen:low] {}", rank_noisy_alerts(input))
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
        assert!(out.contains("12-alert-noise-reducer"));
        assert!(out.contains("rank_noisy_alerts"));
    }
}
