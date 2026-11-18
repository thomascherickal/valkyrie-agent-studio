pub fn plan_strangler_steps(input: &str) -> String {
    format!("[plan_strangler_steps] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-refactor-planner:gemini-4-hydrogen:low] {}", plan_strangler_steps(input))
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
        assert!(out.contains("03-refactor-planner"));
        assert!(out.contains("plan_strangler_steps"));
    }
}
