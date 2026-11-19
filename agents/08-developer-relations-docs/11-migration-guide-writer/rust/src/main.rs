pub fn write_migration_guide(input: &str) -> String {
    format!("[write_migration_guide] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-migration-guide-writer:gemini-4-hydrogen:low] {}", write_migration_guide(input))
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
        assert!(out.contains("11-migration-guide-writer"));
        assert!(out.contains("write_migration_guide"));
    }
}
