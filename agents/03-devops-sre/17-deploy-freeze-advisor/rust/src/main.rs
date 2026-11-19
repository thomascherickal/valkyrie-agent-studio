pub fn decide_freeze(input: &str) -> String {
    format!("[decide_freeze] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-deploy-freeze-advisor:gemini-4-hydrogen:low] {}", decide_freeze(input))
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
        assert!(out.contains("17-deploy-freeze-advisor"));
        assert!(out.contains("decide_freeze"));
    }
}
