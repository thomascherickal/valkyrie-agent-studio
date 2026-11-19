pub fn plan_secret_rotation(input: &str) -> String {
    format!("[plan_secret_rotation] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-secret-rotation-planner:gemini-4-hydrogen:low] {}", plan_secret_rotation(input))
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
        assert!(out.contains("15-secret-rotation-planner"));
        assert!(out.contains("plan_secret_rotation"));
    }
}
