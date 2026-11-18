pub fn estimate_rust_speedup(input: &str) -> String {
    format!("[estimate_rust_speedup] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-rust-port-advisor:gemini-4-hydrogen:low] {}", estimate_rust_speedup(input))
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
        assert!(out.contains("10-rust-port-advisor"));
        assert!(out.contains("estimate_rust_speedup"));
    }
}
