pub fn simulate_unit_margin(input: &str) -> String {
    format!("[simulate_unit_margin] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-pricing-modeler:gemini-4-hydrogen:low] {}", simulate_unit_margin(input))
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
        assert!(out.contains("07-pricing-modeler"));
        assert!(out.contains("simulate_unit_margin"));
    }
}
