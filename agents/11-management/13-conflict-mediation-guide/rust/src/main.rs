pub fn plan_mediation(input: &str) -> String {
    format!("[plan_mediation] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-conflict-mediation-guide:gemini-4-hydrogen:low] {}", plan_mediation(input))
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
        assert!(out.contains("13-conflict-mediation-guide"));
        assert!(out.contains("plan_mediation"));
    }
}
