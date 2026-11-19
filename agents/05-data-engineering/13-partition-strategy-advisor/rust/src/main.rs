pub fn choose_partitioning(input: &str) -> String {
    format!("[choose_partitioning] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-partition-strategy-advisor:gemini-4-hydrogen:low] {}", choose_partitioning(input))
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
        assert!(out.contains("13-partition-strategy-advisor"));
        assert!(out.contains("choose_partitioning"));
    }
}
