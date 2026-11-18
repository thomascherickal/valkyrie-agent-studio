pub fn compile_runbook(input: &str) -> String {
    format!("[compile_runbook] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-runbook-generator:gemini-4-hydrogen:low] {}", compile_runbook(input))
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
        assert!(out.contains("08-runbook-generator"));
        assert!(out.contains("compile_runbook"));
    }
}
