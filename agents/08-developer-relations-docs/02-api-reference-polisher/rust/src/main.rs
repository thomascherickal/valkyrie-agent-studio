pub fn enrich_api_examples(input: &str) -> String {
    format!("[enrich_api_examples] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-api-reference-polisher:gemini-4-hydrogen:low] {}", enrich_api_examples(input))
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
        assert!(out.contains("02-api-reference-polisher"));
        assert!(out.contains("enrich_api_examples"));
    }
}
