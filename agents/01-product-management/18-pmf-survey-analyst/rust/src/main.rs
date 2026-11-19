pub fn score_pmf_survey(input: &str) -> String {
    format!("[score_pmf_survey] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-pmf-survey-analyst:gemini-4-hydrogen:low] {}", score_pmf_survey(input))
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
        assert!(out.contains("18-pmf-survey-analyst"));
        assert!(out.contains("score_pmf_survey"));
    }
}
