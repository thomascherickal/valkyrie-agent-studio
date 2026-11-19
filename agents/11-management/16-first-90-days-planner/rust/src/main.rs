pub fn plan_first_quarter(input: &str) -> String {
    format!("[plan_first_quarter] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-first-90-days-planner:gemini-4-hydrogen:low] {}", plan_first_quarter(input))
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
        assert!(out.contains("16-first-90-days-planner"));
        assert!(out.contains("plan_first_quarter"));
    }
}
