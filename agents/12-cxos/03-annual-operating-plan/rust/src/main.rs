pub fn project_aop_scenarios(input: &str) -> String {
    format!("[project_aop_scenarios] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-annual-operating-plan:gemini-4-hydrogen:low] {}", project_aop_scenarios(input))
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
        assert!(out.contains("03-annual-operating-plan"));
        assert!(out.contains("project_aop_scenarios"));
    }
}
