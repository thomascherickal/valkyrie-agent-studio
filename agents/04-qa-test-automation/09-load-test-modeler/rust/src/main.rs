pub fn build_k6_profile(input: &str) -> String {
    format!("[build_k6_profile] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-load-test-modeler:gemini-4-hydrogen:low] {}", build_k6_profile(input))
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
        assert!(out.contains("09-load-test-modeler"));
        assert!(out.contains("build_k6_profile"));
    }
}
