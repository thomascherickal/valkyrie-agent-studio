pub fn find_stale_flags(input: &str) -> String {
    format!("[find_stale_flags] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-feature-flag-cleaner:gemini-4-hydrogen:low] {}", find_stale_flags(input))
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
        assert!(out.contains("13-feature-flag-cleaner"));
        assert!(out.contains("find_stale_flags"));
    }
}
