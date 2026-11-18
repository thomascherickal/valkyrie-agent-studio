pub fn explain_churn_drivers(input: &str) -> String {
    format!("[explain_churn_drivers] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-churn-cohort-explainer:gemini-4-hydrogen:low] {}", explain_churn_drivers(input))
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
        assert!(out.contains("08-churn-cohort-explainer"));
        assert!(out.contains("explain_churn_drivers"));
    }
}
