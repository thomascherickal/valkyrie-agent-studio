pub fn detect_antipatterns(input: &str) -> String {
    format!("[detect_antipatterns] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-pr-code-reviewer:gemini-4-hydrogen:low] {}", detect_antipatterns(input))
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
        assert!(out.contains("02-pr-code-reviewer"));
        assert!(out.contains("detect_antipatterns"));
    }
}
