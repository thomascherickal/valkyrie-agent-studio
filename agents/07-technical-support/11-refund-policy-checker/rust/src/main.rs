pub fn check_refund_policy(input: &str) -> String {
    format!("[check_refund_policy] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-refund-policy-checker:gemini-4-hydrogen:low] {}", check_refund_policy(input))
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
        assert!(out.contains("11-refund-policy-checker"));
        assert!(out.contains("check_refund_policy"));
    }
}
