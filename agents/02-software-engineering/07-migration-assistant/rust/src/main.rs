pub fn gen_expand_contract(input: &str) -> String {
    format!("[gen_expand_contract] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-migration-assistant:gemini-4-hydrogen:low] {}", gen_expand_contract(input))
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
        assert!(out.contains("07-migration-assistant"));
        assert!(out.contains("gen_expand_contract"));
    }
}
