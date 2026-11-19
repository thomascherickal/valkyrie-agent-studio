pub fn analyze_win_loss(input: &str) -> String {
    format!("[analyze_win_loss] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-win-loss-analyst:gemini-4-hydrogen:low] {}", analyze_win_loss(input))
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
        assert!(out.contains("20-win-loss-analyst"));
        assert!(out.contains("analyze_win_loss"));
    }
}
