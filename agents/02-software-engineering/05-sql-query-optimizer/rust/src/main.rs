pub fn suggest_indexes(input: &str) -> String {
    format!("[suggest_indexes] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-sql-query-optimizer:gemini-4-hydrogen:low] {}", suggest_indexes(input))
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
        assert!(out.contains("05-sql-query-optimizer"));
        assert!(out.contains("suggest_indexes"));
    }
}
