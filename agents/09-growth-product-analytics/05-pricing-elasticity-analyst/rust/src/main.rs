pub fn simulate_paywall(input: &str) -> String {
    format!("[simulate_paywall] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-pricing-elasticity-analyst:gemini-4-hydrogen:low] {}", simulate_paywall(input))
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
        assert!(out.contains("05-pricing-elasticity-analyst"));
        assert!(out.contains("simulate_paywall"));
    }
}
