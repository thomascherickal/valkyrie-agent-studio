pub fn trace_column_lineage(input: &str) -> String {
    format!("[trace_column_lineage] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-lineage-documenter:gemini-4-hydrogen:low] {}", trace_column_lineage(input))
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
        assert!(out.contains("06-lineage-documenter"));
        assert!(out.contains("trace_column_lineage"));
    }
}
