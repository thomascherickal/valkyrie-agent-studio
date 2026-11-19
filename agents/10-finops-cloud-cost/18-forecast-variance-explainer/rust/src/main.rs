pub fn explain_cost_variance(input: &str) -> String {
    format!("[explain_cost_variance] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-forecast-variance-explainer:gemini-4-hydrogen:low] {}", explain_cost_variance(input))
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
        assert!(out.contains("18-forecast-variance-explainer"));
        assert!(out.contains("explain_cost_variance"));
    }
}
