pub fn triage_bounty_report(input: &str) -> String {
    format!("[triage_bounty_report] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-bug-bounty-triager:gemini-4-hydrogen:low] {}", triage_bounty_report(input))
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
        assert!(out.contains("20-bug-bounty-triager"));
        assert!(out.contains("triage_bounty_report"));
    }
}
