pub fn lint_dockerfile(input: &str) -> String {
    format!("[lint_dockerfile] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-container-hardener:gemini-4-hydrogen:low] {}", lint_dockerfile(input))
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
        assert!(out.contains("08-container-hardener"));
        assert!(out.contains("lint_dockerfile"));
    }
}
