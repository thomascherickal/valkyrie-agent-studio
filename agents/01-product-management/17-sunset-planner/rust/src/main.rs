pub fn plan_sunset(input: &str) -> String {
    format!("[plan_sunset] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-sunset-planner:gemini-4-hydrogen:low] {}", plan_sunset(input))
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
        assert!(out.contains("17-sunset-planner"));
        assert!(out.contains("plan_sunset"));
    }
}
