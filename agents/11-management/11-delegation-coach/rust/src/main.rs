pub fn plan_delegation(input: &str) -> String {
    format!("[plan_delegation] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-delegation-coach:gemini-4-hydrogen:low] {}", plan_delegation(input))
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
        assert!(out.contains("11-delegation-coach"));
        assert!(out.contains("plan_delegation"));
    }
}
