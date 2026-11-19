pub fn assess_supply_chain(input: &str) -> String {
    format!("[assess_supply_chain] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-supply-chain-assessor:gemini-4-hydrogen:low] {}", assess_supply_chain(input))
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
        assert!(out.contains("12-supply-chain-assessor"));
        assert!(out.contains("assess_supply_chain"));
    }
}
