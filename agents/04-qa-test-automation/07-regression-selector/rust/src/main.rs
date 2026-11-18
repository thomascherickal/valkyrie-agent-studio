pub fn map_impacted_tests(input: &str) -> String {
    format!("[map_impacted_tests] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-regression-selector:gemini-4-hydrogen:low] {}", map_impacted_tests(input))
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
        assert!(out.contains("07-regression-selector"));
        assert!(out.contains("map_impacted_tests"));
    }
}
