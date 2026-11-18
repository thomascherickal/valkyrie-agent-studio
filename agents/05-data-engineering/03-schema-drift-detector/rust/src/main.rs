pub fn analyze_schema_drift(input: &str) -> String {
    format!("[analyze_schema_drift] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-schema-drift-detector:gemini-4-hydrogen:low] {}", analyze_schema_drift(input))
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
        assert!(out.contains("03-schema-drift-detector"));
        assert!(out.contains("analyze_schema_drift"));
    }
}
