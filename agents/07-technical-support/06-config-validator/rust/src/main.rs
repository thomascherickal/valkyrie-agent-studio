pub fn validate_customer_yaml(input: &str) -> String {
    format!("[validate_customer_yaml] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-config-validator:gemini-4-hydrogen:low] {}", validate_customer_yaml(input))
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
        assert!(out.contains("06-config-validator"));
        assert!(out.contains("validate_customer_yaml"));
    }
}
