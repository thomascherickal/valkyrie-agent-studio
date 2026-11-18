pub fn split_invest_stories(input: &str) -> String {
    format!("[split_invest_stories] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-user-story-splitter:gemini-4-hydrogen:low] {}", split_invest_stories(input))
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
        assert!(out.contains("03-user-story-splitter"));
        assert!(out.contains("split_invest_stories"));
    }
}
