pub fn plan_beta_program(input: &str) -> String {
    format!("[plan_beta_program] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-beta-program-manager:gemini-4-hydrogen:low] {}", plan_beta_program(input))
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
        assert!(out.contains("16-beta-program-manager"));
        assert!(out.contains("plan_beta_program"));
    }
}
