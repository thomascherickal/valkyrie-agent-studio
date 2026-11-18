pub fn check_failure_modes(input: &str) -> String {
    format!("[check_failure_modes] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-architecture-reviewer:gemini-4-hydrogen:low] {}", check_failure_modes(input))
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
        assert!(out.contains("01-architecture-reviewer"));
        assert!(out.contains("check_failure_modes"));
    }
}
