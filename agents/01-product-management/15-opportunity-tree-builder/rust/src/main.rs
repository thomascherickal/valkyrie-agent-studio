pub fn build_ost(input: &str) -> String {
    format!("[build_ost] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-opportunity-tree-builder:gemini-4-hydrogen:low] {}", build_ost(input))
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
        assert!(out.contains("15-opportunity-tree-builder"));
        assert!(out.contains("build_ost"));
    }
}
