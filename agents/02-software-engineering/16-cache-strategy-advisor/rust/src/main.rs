pub fn design_cache_strategy(input: &str) -> String {
    format!("[design_cache_strategy] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-cache-strategy-advisor:gemini-4-hydrogen:low] {}", design_cache_strategy(input))
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
        assert!(out.contains("16-cache-strategy-advisor"));
        assert!(out.contains("design_cache_strategy"));
    }
}
