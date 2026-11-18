pub fn detect_spend_spike(input: &str) -> String {
    format!("[detect_spend_spike] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-cloud-bill-anomaly:gemini-4-hydrogen:low] {}", detect_spend_spike(input))
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
        assert!(out.contains("01-cloud-bill-anomaly"));
        assert!(out.contains("detect_spend_spike"));
    }
}
