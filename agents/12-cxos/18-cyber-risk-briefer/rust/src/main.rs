pub fn brief_cyber_risk(input: &str) -> String {
    format!("[brief_cyber_risk] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-cyber-risk-briefer:gemini-4-hydrogen:low] {}", brief_cyber_risk(input))
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
        assert!(out.contains("18-cyber-risk-briefer"));
        assert!(out.contains("brief_cyber_risk"));
    }
}
