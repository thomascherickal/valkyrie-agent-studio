pub fn verify_dns_change(input: &str) -> String {
    format!("[verify_dns_change] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-dns-change-verifier:gemini-4-hydrogen:low] {}", verify_dns_change(input))
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
        assert!(out.contains("19-dns-change-verifier"));
        assert!(out.contains("verify_dns_change"));
    }
}
