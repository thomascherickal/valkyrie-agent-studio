pub fn explain_api_error(input: &str) -> String {
    format!("[explain_api_error] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-api-error-explainer:gemini-4-hydrogen:low] {}", explain_api_error(input))
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
        assert!(out.contains("07-api-error-explainer"));
        assert!(out.contains("explain_api_error"));
    }
}
