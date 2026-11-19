pub fn review_sql_style(input: &str) -> String {
    format!("[review_sql_style] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-sql-style-reviewer:gemini-4-hydrogen:low] {}", review_sql_style(input))
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
        assert!(out.contains("19-sql-style-reviewer"));
        assert!(out.contains("review_sql_style"));
    }
}
