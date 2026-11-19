pub fn plan_exec_search(input: &str) -> String {
    format!("[plan_exec_search] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-exec-search-planner:gemini-4-hydrogen:low] {}", plan_exec_search(input))
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
        assert!(out.contains("16-exec-search-planner"));
        assert!(out.contains("plan_exec_search"));
    }
}
