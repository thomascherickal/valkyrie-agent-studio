pub fn route_budget_warning(input: &str) -> String {
    format!("[route_budget_warning] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-budget-alert-router:gemini-4-hydrogen:low] {}", route_budget_warning(input))
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
        assert!(out.contains("09-budget-alert-router"));
        assert!(out.contains("route_budget_warning"));
    }
}
