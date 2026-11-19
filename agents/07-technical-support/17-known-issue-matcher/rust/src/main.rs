pub fn match_known_issues(input: &str) -> String {
    format!("[match_known_issues] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-known-issue-matcher:gemini-4-hydrogen:low] {}", match_known_issues(input))
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
        assert!(out.contains("17-known-issue-matcher"));
        assert!(out.contains("match_known_issues"));
    }
}
