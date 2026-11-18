pub fn summarize_dx_metrics(input: &str) -> String {
    format!("[summarize_dx_metrics] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-dev-survey-analyst:gemini-4-hydrogen:low] {}", summarize_dx_metrics(input))
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
        assert!(out.contains("10-dev-survey-analyst"));
        assert!(out.contains("summarize_dx_metrics"));
    }
}
