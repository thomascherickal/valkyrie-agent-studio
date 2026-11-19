pub fn tune_db_cost(input: &str) -> String {
    format!("[tune_db_cost] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-database-cost-tuner:gemini-4-hydrogen:low] {}", tune_db_cost(input))
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
        assert!(out.contains("16-database-cost-tuner"));
        assert!(out.contains("tune_db_cost"));
    }
}
