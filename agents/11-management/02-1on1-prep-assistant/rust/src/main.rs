pub fn structure_1on1_agenda(input: &str) -> String {
    format!("[structure_1on1_agenda] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-1on1-prep-assistant:gemini-4-hydrogen:low] {}", structure_1on1_agenda(input))
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
        assert!(out.contains("02-1on1-prep-assistant"));
        assert!(out.contains("structure_1on1_agenda"));
    }
}
