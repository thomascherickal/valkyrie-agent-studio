pub fn compute_churn_risk(input: &str) -> String {
    format!("[compute_churn_risk] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-churn-signal-spotter:gemini-4-hydrogen:low] {}", compute_churn_risk(input))
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
        assert!(out.contains("09-churn-signal-spotter"));
        assert!(out.contains("compute_churn_risk"));
    }
}
