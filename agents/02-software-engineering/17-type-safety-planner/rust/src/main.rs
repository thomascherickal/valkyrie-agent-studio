pub fn plan_type_hardening(input: &str) -> String {
    format!("[plan_type_hardening] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-type-safety-planner:gemini-4-hydrogen:low] {}", plan_type_hardening(input))
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
        assert!(out.contains("17-type-safety-planner"));
        assert!(out.contains("plan_type_hardening"));
    }
}
