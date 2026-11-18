pub fn validate_openapi_diff(input: &str) -> String {
    format!("[validate_openapi_diff] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-api-contract-designer:gemini-4-hydrogen:low] {}", validate_openapi_diff(input))
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
        assert!(out.contains("04-api-contract-designer"));
        assert!(out.contains("validate_openapi_diff"));
    }
}
