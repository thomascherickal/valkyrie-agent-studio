pub fn project_runway(input: &str) -> String {
    format!("[project_runway] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-cash-runway-analyst:gemini-4-hydrogen:low] {}", project_runway(input))
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
        assert!(out.contains("11-cash-runway-analyst"));
        assert!(out.contains("project_runway"));
    }
}
