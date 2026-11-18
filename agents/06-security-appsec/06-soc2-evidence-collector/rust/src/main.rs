pub fn collect_control_proof(input: &str) -> String {
    format!("[collect_control_proof] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-soc2-evidence-collector:gemini-4-hydrogen:low] {}", collect_control_proof(input))
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
        assert!(out.contains("06-soc2-evidence-collector"));
        assert!(out.contains("collect_control_proof"));
    }
}
