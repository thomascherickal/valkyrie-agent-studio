pub fn model_scd(input: &str) -> String {
    format!("[model_scd] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-scd-modeler:gemini-4-hydrogen:low] {}", model_scd(input))
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
        assert!(out.contains("15-scd-modeler"));
        assert!(out.contains("model_scd"));
    }
}
