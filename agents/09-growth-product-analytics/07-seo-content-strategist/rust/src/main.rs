pub fn score_keyword_gaps(input: &str) -> String {
    format!("[score_keyword_gaps] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-seo-content-strategist:gemini-4-hydrogen:low] {}", score_keyword_gaps(input))
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
        assert!(out.contains("07-seo-content-strategist"));
        assert!(out.contains("score_keyword_gaps"));
    }
}
