pub fn detect_doc_drift(input: &str) -> String {
    format!("[detect_doc_drift] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-docs-freshness-checker:gemini-4-hydrogen:low] {}", detect_doc_drift(input))
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
        assert!(out.contains("07-docs-freshness-checker"));
        assert!(out.contains("detect_doc_drift"));
    }
}
