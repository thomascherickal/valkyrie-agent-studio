pub fn optimize_dag(input: &str) -> String {
    format!("[optimize_dag] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-ci-pipeline-optimizer:gemini-4-hydrogen:low] {}", optimize_dag(input))
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
        assert!(out.contains("06-ci-pipeline-optimizer"));
        assert!(out.contains("optimize_dag"));
    }
}
