pub fn synthesize_personas(input: &str) -> String {
    format!("[synthesize_personas] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-persona-builder:gemini-4-hydrogen:low] {}", synthesize_personas(input))
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
        assert!(out.contains("11-persona-builder"));
        assert!(out.contains("synthesize_personas"));
    }
}
