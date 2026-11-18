pub fn format_investor_email(input: &str) -> String {
    format!("[format_investor_email] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-investor-update-writer:gemini-4-hydrogen:low] {}", format_investor_email(input))
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
        assert!(out.contains("06-investor-update-writer"));
        assert!(out.contains("format_investor_email"));
    }
}
