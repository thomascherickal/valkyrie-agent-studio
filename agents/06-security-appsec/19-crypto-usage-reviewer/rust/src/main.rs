pub fn review_crypto_usage(input: &str) -> String {
    format!("[review_crypto_usage] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-crypto-usage-reviewer:gemini-4-hydrogen:low] {}", review_crypto_usage(input))
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
        assert!(out.contains("19-crypto-usage-reviewer"));
        assert!(out.contains("review_crypto_usage"));
    }
}
