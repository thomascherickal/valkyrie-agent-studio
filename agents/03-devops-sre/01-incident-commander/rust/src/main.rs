pub fn build_ics_timeline(input: &str) -> String {
    format!("[build_ics_timeline] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-incident-commander:gemini-4-hydrogen:low] {}", build_ics_timeline(input))
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
        assert!(out.contains("01-incident-commander"));
        assert!(out.contains("build_ics_timeline"));
    }
}
