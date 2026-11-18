pub fn compute_rice_score(input: &str) -> String {
    format!("[compute_rice_score] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-roadmap-prioritizer:gemini-4-hydrogen:low] {}", compute_rice_score(input))
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
        assert!(out.contains("02-roadmap-prioritizer"));
        assert!(out.contains("compute_rice_score"));
    }
}
