pub fn emit_polyglot_samples(input: &str) -> String {
    format!("[emit_polyglot_samples] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-sdk-sample-generator:gemini-4-hydrogen:low] {}", emit_polyglot_samples(input))
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
        assert!(out.contains("03-sdk-sample-generator"));
        assert!(out.contains("emit_polyglot_samples"));
    }
}
