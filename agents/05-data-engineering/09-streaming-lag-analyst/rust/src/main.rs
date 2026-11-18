pub fn diagnose_partition_skew(input: &str) -> String {
    format!("[diagnose_partition_skew] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-streaming-lag-analyst:gemini-4-hydrogen:low] {}", diagnose_partition_skew(input))
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
        assert!(out.contains("09-streaming-lag-analyst"));
        assert!(out.contains("diagnose_partition_skew"));
    }
}
