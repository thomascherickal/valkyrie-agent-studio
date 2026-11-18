pub fn curate_dev_changelog(input: &str) -> String {
    format!("[curate_dev_changelog] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-changelog-curator:gemini-4-hydrogen:low] {}", curate_dev_changelog(input))
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
        assert!(out.contains("04-changelog-curator"));
        assert!(out.contains("curate_dev_changelog"));
    }
}
