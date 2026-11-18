pub fn analyze_cohort_curve(input: &str) -> String {
    format!("[analyze_cohort_curve] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-cohort-retention-modeler:gemini-4-hydrogen:low] {}", analyze_cohort_curve(input))
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
        assert!(out.contains("02-cohort-retention-modeler"));
        assert!(out.contains("analyze_cohort_curve"));
    }
}
