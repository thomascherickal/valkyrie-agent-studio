pub fn format_qbr_brief(input: &str) -> String {
    format!("[format_qbr_brief] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-quarterly-roadmap-brief:gemini-4-hydrogen:low] {}", format_qbr_brief(input))
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
        assert!(out.contains("10-quarterly-roadmap-brief"));
        assert!(out.contains("format_qbr_brief"));
    }
}
