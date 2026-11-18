pub fn extract_root_exception(input: &str) -> String {
    format!("[extract_root_exception] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-log-bundle-analyzer:gemini-4-hydrogen:low] {}", extract_root_exception(input))
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
        assert!(out.contains("02-log-bundle-analyzer"));
        assert!(out.contains("extract_root_exception"));
    }
}
