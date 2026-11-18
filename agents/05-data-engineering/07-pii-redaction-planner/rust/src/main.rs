pub fn classify_pii_columns(input: &str) -> String {
    format!("[classify_pii_columns] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-pii-redaction-planner:gemini-4-hydrogen:low] {}", classify_pii_columns(input))
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
        assert!(out.contains("07-pii-redaction-planner"));
        assert!(out.contains("classify_pii_columns"));
    }
}
