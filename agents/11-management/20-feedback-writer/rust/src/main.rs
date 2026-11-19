pub fn write_feedback(input: &str) -> String {
    format!("[write_feedback] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-feedback-writer:gemini-4-hydrogen:low] {}", write_feedback(input))
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
        assert!(out.contains("20-feedback-writer"));
        assert!(out.contains("write_feedback"));
    }
}
