pub fn justify_headcount(input: &str) -> String {
    format!("[justify_headcount] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-headcount-justifier:gemini-4-hydrogen:low] {}", justify_headcount(input))
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
        assert!(out.contains("15-headcount-justifier"));
        assert!(out.contains("justify_headcount"));
    }
}
