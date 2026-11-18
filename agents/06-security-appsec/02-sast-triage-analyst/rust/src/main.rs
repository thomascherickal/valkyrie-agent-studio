pub fn assess_reachability(input: &str) -> String {
    format!("[assess_reachability] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-sast-triage-analyst:gemini-4-hydrogen:low] {}", assess_reachability(input))
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
        assert!(out.contains("02-sast-triage-analyst"));
        assert!(out.contains("assess_reachability"));
    }
}
