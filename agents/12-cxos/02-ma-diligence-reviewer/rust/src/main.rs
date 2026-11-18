pub fn score_diligence_risks(input: &str) -> String {
    format!("[score_diligence_risks] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-ma-diligence-reviewer:gemini-4-hydrogen:low] {}", score_diligence_risks(input))
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
        assert!(out.contains("02-ma-diligence-reviewer"));
        assert!(out.contains("score_diligence_risks"));
    }
}
