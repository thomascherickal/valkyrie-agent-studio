pub fn format_changelog(input: &str) -> String {
    format!("[format_changelog] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-release-notes-writer:gemini-4-hydrogen:low] {}", format_changelog(input))
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
        assert!(out.contains("09-release-notes-writer"));
        assert!(out.contains("format_changelog"));
    }
}
