pub fn rank_experiments(input: &str) -> String {
    format!("[rank_experiments] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-experiment-backlog-ranker:gemini-4-hydrogen:low] {}", rank_experiments(input))
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
        assert!(out.contains("13-experiment-backlog-ranker"));
        assert!(out.contains("rank_experiments"));
    }
}
