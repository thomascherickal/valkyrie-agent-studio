pub fn review_docs_ia(input: &str) -> String {
    format!("[review_docs_ia] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-docs-ia-reviewer:gemini-4-hydrogen:low] {}", review_docs_ia(input))
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
        assert!(out.contains("14-docs-ia-reviewer"));
        assert!(out.contains("review_docs_ia"));
    }
}
