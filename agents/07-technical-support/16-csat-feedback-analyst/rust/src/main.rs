pub fn analyze_csat(input: &str) -> String {
    format!("[analyze_csat] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-csat-feedback-analyst:gemini-4-hydrogen:low] {}", analyze_csat(input))
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
        assert!(out.contains("16-csat-feedback-analyst"));
        assert!(out.contains("analyze_csat"));
    }
}
