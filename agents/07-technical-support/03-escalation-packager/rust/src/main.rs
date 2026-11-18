pub fn package_l3_handoff(input: &str) -> String {
    format!("[package_l3_handoff] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-escalation-packager:gemini-4-hydrogen:low] {}", package_l3_handoff(input))
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
        assert!(out.contains("03-escalation-packager"));
        assert!(out.contains("package_l3_handoff"));
    }
}
