pub fn review_dr_plan(input: &str) -> String {
    format!("[review_dr_plan] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-dr-plan-reviewer:gemini-4-hydrogen:low] {}", review_dr_plan(input))
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
        assert!(out.contains("13-dr-plan-reviewer"));
        assert!(out.contains("review_dr_plan"));
    }
}
