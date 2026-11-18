pub fn build_dq_assertions(input: &str) -> String {
    format!("[build_dq_assertions] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-data-quality-guardian:gemini-4-hydrogen:low] {}", build_dq_assertions(input))
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
        assert!(out.contains("04-data-quality-guardian"));
        assert!(out.contains("build_dq_assertions"));
    }
}
