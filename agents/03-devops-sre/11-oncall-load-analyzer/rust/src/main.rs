pub fn analyze_oncall_load(input: &str) -> String {
    format!("[analyze_oncall_load] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-oncall-load-analyzer:gemini-4-hydrogen:low] {}", analyze_oncall_load(input))
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
        assert!(out.contains("11-oncall-load-analyzer"));
        assert!(out.contains("analyze_oncall_load"));
    }
}
