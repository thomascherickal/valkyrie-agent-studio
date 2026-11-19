pub fn write_contributing_guide(input: &str) -> String {
    format!("[write_contributing_guide] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-contributing-guide-writer:gemini-4-hydrogen:low] {}", write_contributing_guide(input))
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
        assert!(out.contains("19-contributing-guide-writer"));
        assert!(out.contains("write_contributing_guide"));
    }
}
