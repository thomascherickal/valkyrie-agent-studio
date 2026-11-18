pub fn emit_playwright_spec(input: &str) -> String {
    format!("[emit_playwright_spec] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-playwright-scripter:gemini-4-hydrogen:low] {}", emit_playwright_spec(input))
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
        assert!(out.contains("03-playwright-scripter"));
        assert!(out.contains("emit_playwright_spec"));
    }
}
