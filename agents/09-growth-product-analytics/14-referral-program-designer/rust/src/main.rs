pub fn design_referral(input: &str) -> String {
    format!("[design_referral] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-referral-program-designer:gemini-4-hydrogen:low] {}", design_referral(input))
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
        assert!(out.contains("14-referral-program-designer"));
        assert!(out.contains("design_referral"));
    }
}
