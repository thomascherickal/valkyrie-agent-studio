pub fn generate_setup_plan(input: &str) -> String {
    format!("[generate_setup_plan] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-onboarding-concierge:gemini-4-hydrogen:low] {}", generate_setup_plan(input))
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
        assert!(out.contains("08-onboarding-concierge"));
        assert!(out.contains("generate_setup_plan"));
    }
}
