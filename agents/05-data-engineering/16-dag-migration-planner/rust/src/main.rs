pub fn plan_dag_migration(input: &str) -> String {
    format!("[plan_dag_migration] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-dag-migration-planner:gemini-4-hydrogen:low] {}", plan_dag_migration(input))
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
        assert!(out.contains("16-dag-migration-planner"));
        assert!(out.contains("plan_dag_migration"));
    }
}
