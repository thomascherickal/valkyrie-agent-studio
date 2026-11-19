pub fn build_release_checklist(input: &str) -> String {
    format!("[build_release_checklist] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-qa-release-checklist-builder:gemini-4-hydrogen:low] {}", build_release_checklist(input))
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
        assert!(out.contains("18-qa-release-checklist-builder"));
        assert!(out.contains("build_release_checklist"));
    }
}
