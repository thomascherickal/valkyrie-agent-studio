pub fn review_pricing_page(input: &str) -> String {
    format!("[review_pricing_page] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-pricing-page-reviewer:gemini-4-hydrogen:low] {}", review_pricing_page(input))
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
        assert!(out.contains("17-pricing-page-reviewer"));
        assert!(out.contains("review_pricing_page"));
    }
}
