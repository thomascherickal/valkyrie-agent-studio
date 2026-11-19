pub fn write_error_reference(input: &str) -> String {
    format!("[write_error_reference] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-error-reference-writer:gemini-4-hydrogen:low] {}", write_error_reference(input))
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
        assert!(out.contains("12-error-reference-writer"));
        assert!(out.contains("write_error_reference"));
    }
}
