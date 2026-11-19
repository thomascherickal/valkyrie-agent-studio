pub fn plan_retention(input: &str) -> String {
    format!("[plan_retention] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-data-retention-planner:gemini-4-hydrogen:low] {}", plan_retention(input))
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
        assert!(out.contains("18-data-retention-planner"));
        assert!(out.contains("plan_retention"));
    }
}
