pub fn tune_log_retention(input: &str) -> String {
    format!("[tune_log_retention] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-log-retention-tuner:gemini-4-hydrogen:low] {}", tune_log_retention(input))
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
        assert!(out.contains("18-log-retention-tuner"));
        assert!(out.contains("tune_log_retention"));
    }
}
