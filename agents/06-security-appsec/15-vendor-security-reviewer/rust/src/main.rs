pub fn review_vendor_security(input: &str) -> String {
    format!("[review_vendor_security] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-vendor-security-reviewer:gemini-4-hydrogen:low] {}", review_vendor_security(input))
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
        assert!(out.contains("15-vendor-security-reviewer"));
        assert!(out.contains("review_vendor_security"));
    }
}
