pub fn build_board_narrative(input: &str) -> String {
    format!("[build_board_narrative] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-board-deck-synthesizer:gemini-4-hydrogen:low] {}", build_board_narrative(input))
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
        assert!(out.contains("01-board-deck-synthesizer"));
        assert!(out.contains("build_board_narrative"));
    }
}
