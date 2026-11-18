pub fn eval_canary_gate(input: &str) -> String {
    format!("[eval_canary_gate] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-rollback-verifier:gemini-4-hydrogen:low] {}", eval_canary_gate(input))
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
        assert!(out.contains("10-rollback-verifier"));
        assert!(out.contains("eval_canary_gate"));
    }
}
