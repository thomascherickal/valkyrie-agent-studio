pub fn compose_community_reply(input: &str) -> String {
    format!("[compose_community_reply] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-community-qa-helper:gemini-4-hydrogen:low] {}", compose_community_reply(input))
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
        assert!(out.contains("05-community-qa-helper"));
        assert!(out.contains("compose_community_reply"));
    }
}
