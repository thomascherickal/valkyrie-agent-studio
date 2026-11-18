pub fn score_debt_roi(input: &str) -> String {
    format!("[score_debt_roi] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-tech-debt-triager:gemini-4-hydrogen:low] {}", score_debt_roi(input))
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
        assert!(out.contains("08-tech-debt-triager"));
        assert!(out.contains("score_debt_roi"));
    }
}
