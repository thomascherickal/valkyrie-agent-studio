pub fn analyze_org_topology(input: &str) -> String {
    format!("[analyze_org_topology] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-org-design-modeler:gemini-4-hydrogen:low] {}", analyze_org_topology(input))
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
        assert!(out.contains("09-org-design-modeler"));
        assert!(out.contains("analyze_org_topology"));
    }
}
