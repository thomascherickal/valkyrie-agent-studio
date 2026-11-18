pub fn design_chaos_drill(input: &str) -> String {
    format!("[design_chaos_drill] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-chaos-test-designer:gemini-4-hydrogen:low] {}", design_chaos_drill(input))
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
        assert!(out.contains("09-chaos-test-designer"));
        assert!(out.contains("design_chaos_drill"));
    }
}
