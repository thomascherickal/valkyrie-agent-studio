pub fn lint_k8s_spec(input: &str) -> String {
    format!("[lint_k8s_spec] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-k8s-manifest-linter:gemini-4-hydrogen:low] {}", lint_k8s_spec(input))
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
        assert!(out.contains("04-k8s-manifest-linter"));
        assert!(out.contains("lint_k8s_spec"));
    }
}
