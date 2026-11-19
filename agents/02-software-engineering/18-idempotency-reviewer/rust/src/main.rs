pub fn check_idempotency(input: &str) -> String {
    format!("[check_idempotency] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-idempotency-reviewer:gemini-4-hydrogen:low] {}", check_idempotency(input))
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
        assert!(out.contains("18-idempotency-reviewer"));
        assert!(out.contains("check_idempotency"));
    }
}
