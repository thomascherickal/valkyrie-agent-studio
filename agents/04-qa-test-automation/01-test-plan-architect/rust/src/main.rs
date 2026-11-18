pub fn derive_test_matrix(input: &str) -> String {
    format!("[derive_test_matrix] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-test-plan-architect:gemini-4-hydrogen:low] {}", derive_test_matrix(input))
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
        assert!(out.contains("01-test-plan-architect"));
        assert!(out.contains("derive_test_matrix"));
    }
}
