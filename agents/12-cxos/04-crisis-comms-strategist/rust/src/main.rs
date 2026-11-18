pub fn draft_comms_matrix(input: &str) -> String {
    format!("[draft_comms_matrix] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-crisis-comms-strategist:gemini-4-hydrogen:low] {}", draft_comms_matrix(input))
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
        assert!(out.contains("04-crisis-comms-strategist"));
        assert!(out.contains("draft_comms_matrix"));
    }
}
