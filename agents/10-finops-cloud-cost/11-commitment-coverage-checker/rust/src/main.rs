pub fn check_commitment_coverage(input: &str) -> String {
    format!("[check_commitment_coverage] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-commitment-coverage-checker:gemini-4-hydrogen:low] {}", check_commitment_coverage(input))
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
        assert!(out.contains("11-commitment-coverage-checker"));
        assert!(out.contains("check_commitment_coverage"));
    }
}
