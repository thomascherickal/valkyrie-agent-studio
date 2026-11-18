pub fn scan_secret_patterns(input: &str) -> String {
    format!("[scan_secret_patterns] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-secret-leak-scanner:gemini-4-hydrogen:low] {}", scan_secret_patterns(input))
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
        assert!(out.contains("04-secret-leak-scanner"));
        assert!(out.contains("scan_secret_patterns"));
    }
}
