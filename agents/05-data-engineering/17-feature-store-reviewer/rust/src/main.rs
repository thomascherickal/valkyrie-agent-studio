pub fn review_feature_store(input: &str) -> String {
    format!("[review_feature_store] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-feature-store-reviewer:gemini-4-hydrogen:low] {}", review_feature_store(input))
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
        assert!(out.contains("17-feature-store-reviewer"));
        assert!(out.contains("review_feature_store"));
    }
}
