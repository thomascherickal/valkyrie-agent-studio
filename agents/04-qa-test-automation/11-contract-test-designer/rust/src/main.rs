pub fn design_contract_tests(input: &str) -> String {
    format!("[design_contract_tests] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-contract-test-designer:gemini-4-hydrogen:low] {}", design_contract_tests(input))
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
        assert!(out.contains("11-contract-test-designer"));
        assert!(out.contains("design_contract_tests"));
    }
}
