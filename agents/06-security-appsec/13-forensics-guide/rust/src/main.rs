pub fn plan_forensics(input: &str) -> String {
    format!("[plan_forensics] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-forensics-guide:gemini-4-hydrogen:low] {}", plan_forensics(input))
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
        assert!(out.contains("13-forensics-guide"));
        assert!(out.contains("plan_forensics"));
    }
}
