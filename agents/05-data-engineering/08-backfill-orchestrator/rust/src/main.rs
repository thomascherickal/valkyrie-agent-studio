pub fn chunk_date_windows(input: &str) -> String {
    format!("[chunk_date_windows] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-backfill-orchestrator:gemini-4-hydrogen:low] {}", chunk_date_windows(input))
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
        assert!(out.contains("08-backfill-orchestrator"));
        assert!(out.contains("chunk_date_windows"));
    }
}
