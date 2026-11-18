pub fn map_compliance_gaps(input: &str) -> String {
    format!("[map_compliance_gaps] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-regulatory-horizon-watch:gemini-4-hydrogen:low] {}", map_compliance_gaps(input))
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
        assert!(out.contains("08-regulatory-horizon-watch"));
        assert!(out.contains("map_compliance_gaps"));
    }
}
