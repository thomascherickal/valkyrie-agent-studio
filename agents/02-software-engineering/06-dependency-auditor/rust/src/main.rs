pub fn scan_licenses(input: &str) -> String {
    format!("[scan_licenses] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-dependency-auditor:gemini-4-hydrogen:low] {}", scan_licenses(input))
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
        assert!(out.contains("06-dependency-auditor"));
        assert!(out.contains("scan_licenses"));
    }
}
