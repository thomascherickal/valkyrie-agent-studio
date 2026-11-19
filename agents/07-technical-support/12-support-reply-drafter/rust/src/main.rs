pub fn draft_support_reply(input: &str) -> String {
    format!("[draft_support_reply] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-support-reply-drafter:gemini-4-hydrogen:low] {}", draft_support_reply(input))
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
        assert!(out.contains("12-support-reply-drafter"));
        assert!(out.contains("draft_support_reply"));
    }
}
