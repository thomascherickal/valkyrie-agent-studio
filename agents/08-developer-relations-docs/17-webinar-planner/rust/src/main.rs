pub fn plan_webinar(input: &str) -> String {
    format!("[plan_webinar] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-webinar-planner:gemini-4-hydrogen:low] {}", plan_webinar(input))
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
        assert!(out.contains("17-webinar-planner"));
        assert!(out.contains("plan_webinar"));
    }
}
