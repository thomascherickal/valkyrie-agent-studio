pub fn write_charters(input: &str) -> String {
    format!("[write_charters] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-exploratory-charter-writer:gemini-4-hydrogen:low] {}", write_charters(input))
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
        assert!(out.contains("17-exploratory-charter-writer"));
        assert!(out.contains("write_charters"));
    }
}
