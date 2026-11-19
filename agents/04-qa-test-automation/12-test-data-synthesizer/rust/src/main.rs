pub fn synthesize_test_data(input: &str) -> String {
    format!("[synthesize_test_data] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-test-data-synthesizer:gemini-4-hydrogen:low] {}", synthesize_test_data(input))
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
        assert!(out.contains("12-test-data-synthesizer"));
        assert!(out.contains("synthesize_test_data"));
    }
}
