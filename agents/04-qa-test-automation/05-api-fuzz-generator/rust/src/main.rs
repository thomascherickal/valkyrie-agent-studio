pub fn generate_fuzz_corpus(input: &str) -> String {
    format!("[generate_fuzz_corpus] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-api-fuzz-generator:gemini-4-hydrogen:low] {}", generate_fuzz_corpus(input))
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
        assert!(out.contains("05-api-fuzz-generator"));
        assert!(out.contains("generate_fuzz_corpus"));
    }
}
