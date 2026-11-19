pub fn rank_board_risks(input: &str) -> String {
    format!("[rank_board_risks] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-board-risk-register-keeper:gemini-4-hydrogen:low] {}", rank_board_risks(input))
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
        assert!(out.contains("13-board-risk-register-keeper"));
        assert!(out.contains("rank_board_risks"));
    }
}
