pub fn propose_branch_tests(input: &str) -> String {
    format!("[propose_branch_tests] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-coverage-gap-finder:gemini-4-hydrogen:low] {}", propose_branch_tests(input))
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
        assert!(out.contains("06-coverage-gap-finder"));
        assert!(out.contains("propose_branch_tests"));
    }
}
