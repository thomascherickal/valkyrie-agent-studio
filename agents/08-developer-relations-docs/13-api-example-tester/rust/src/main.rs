pub fn test_api_examples(input: &str) -> String {
    format!("[test_api_examples] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-api-example-tester:gemini-4-hydrogen:low] {}", test_api_examples(input))
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
        assert!(out.contains("13-api-example-tester"));
        assert!(out.contains("test_api_examples"));
    }
}
