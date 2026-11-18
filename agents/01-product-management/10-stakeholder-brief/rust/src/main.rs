pub fn summarize_exec_digest(input: &str) -> String {
    format!("[summarize_exec_digest] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-stakeholder-brief:gemini-4-hydrogen:low] {}", summarize_exec_digest(input))
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
        assert!(out.contains("10-stakeholder-brief"));
        assert!(out.contains("summarize_exec_digest"));
    }
}
