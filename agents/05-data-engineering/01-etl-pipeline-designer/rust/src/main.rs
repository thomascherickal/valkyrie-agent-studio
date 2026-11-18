pub fn design_idempotent_dag(input: &str) -> String {
    format!("[design_idempotent_dag] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-etl-pipeline-designer:gemini-4-hydrogen:low] {}", design_idempotent_dag(input))
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
        assert!(out.contains("01-etl-pipeline-designer"));
        assert!(out.contains("design_idempotent_dag"));
    }
}
