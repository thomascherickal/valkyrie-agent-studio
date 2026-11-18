pub fn design_lifecycle_rule(input: &str) -> String {
    format!("[design_lifecycle_rule] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-storage-tiering-planner:gemini-4-hydrogen:low] {}", design_lifecycle_rule(input))
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
        assert!(out.contains("07-storage-tiering-planner"));
        assert!(out.contains("design_lifecycle_rule"));
    }
}
