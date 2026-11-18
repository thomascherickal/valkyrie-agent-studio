pub fn extract_requirements(input: &str) -> String {
    format!("[extract_requirements] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-prd-architect:gemini-4-hydrogen:low] {}", extract_requirements(input))
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
        assert!(out.contains("01-prd-architect"));
        assert!(out.contains("extract_requirements"));
    }
}
