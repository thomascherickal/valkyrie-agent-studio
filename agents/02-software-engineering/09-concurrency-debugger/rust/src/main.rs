pub fn analyze_lock_graph(input: &str) -> String {
    format!("[analyze_lock_graph] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-concurrency-debugger:gemini-4-hydrogen:low] {}", analyze_lock_graph(input))
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
        assert!(out.contains("09-concurrency-debugger"));
        assert!(out.contains("analyze_lock_graph"));
    }
}
