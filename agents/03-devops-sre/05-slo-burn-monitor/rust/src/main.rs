pub fn calc_burn_rate(input: &str) -> String {
    format!("[calc_burn_rate] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-slo-burn-monitor:gemini-4-hydrogen:low] {}", calc_burn_rate(input))
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
        assert!(out.contains("05-slo-burn-monitor"));
        assert!(out.contains("calc_burn_rate"));
    }
}
