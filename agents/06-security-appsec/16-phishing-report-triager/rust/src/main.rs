pub fn triage_phishing(input: &str) -> String {
    format!("[triage_phishing] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-phishing-report-triager:gemini-4-hydrogen:low] {}", triage_phishing(input))
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
        assert!(out.contains("16-phishing-report-triager"));
        assert!(out.contains("triage_phishing"));
    }
}
