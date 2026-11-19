pub fn draft_data_contract(input: &str) -> String {
    format!("[draft_data_contract] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-data-contract-author:gemini-4-hydrogen:low] {}", draft_data_contract(input))
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
        assert!(out.contains("12-data-contract-author"));
        assert!(out.contains("draft_data_contract"));
    }
}
