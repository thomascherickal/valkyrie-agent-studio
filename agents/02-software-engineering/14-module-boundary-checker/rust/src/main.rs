pub fn check_module_boundaries(input: &str) -> String {
    format!("[check_module_boundaries] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-module-boundary-checker:gemini-4-hydrogen:low] {}", check_module_boundaries(input))
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
        assert!(out.contains("14-module-boundary-checker"));
        assert!(out.contains("check_module_boundaries"));
    }
}
