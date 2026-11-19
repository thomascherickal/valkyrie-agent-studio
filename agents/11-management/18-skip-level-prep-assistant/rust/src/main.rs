pub fn prep_skip_level(input: &str) -> String {
    format!("[prep_skip_level] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-skip-level-prep-assistant:gemini-4-hydrogen:low] {}", prep_skip_level(input))
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
        assert!(out.contains("18-skip-level-prep-assistant"));
        assert!(out.contains("prep_skip_level"));
    }
}
