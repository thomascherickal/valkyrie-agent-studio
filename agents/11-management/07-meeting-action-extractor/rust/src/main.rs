pub fn extract_action_items(input: &str) -> String {
    format!("[extract_action_items] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-meeting-action-extractor:gemini-4-hydrogen:low] {}", extract_action_items(input))
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
        assert!(out.contains("07-meeting-action-extractor"));
        assert!(out.contains("extract_action_items"));
    }
}
