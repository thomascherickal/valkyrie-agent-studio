pub fn write_onboarding_guide(input: &str) -> String {
    format!("[write_onboarding_guide] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-codebase-onboarding-guide:gemini-4-hydrogen:low] {}", write_onboarding_guide(input))
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
        assert!(out.contains("20-codebase-onboarding-guide"));
        assert!(out.contains("write_onboarding_guide"));
    }
}
