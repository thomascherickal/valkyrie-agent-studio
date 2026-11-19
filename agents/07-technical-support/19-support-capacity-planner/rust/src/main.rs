pub fn plan_support_staffing(input: &str) -> String {
    format!("[plan_support_staffing] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-support-capacity-planner:gemini-4-hydrogen:low] {}", plan_support_staffing(input))
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
        assert!(out.contains("19-support-capacity-planner"));
        assert!(out.contains("plan_support_staffing"));
    }
}
