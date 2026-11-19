pub fn prep_earnings_call(input: &str) -> String {
    format!("[prep_earnings_call] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-earnings-call-prep-coach:gemini-4-hydrogen:low] {}", prep_earnings_call(input))
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
        assert!(out.contains("17-earnings-call-prep-coach"));
        assert!(out.contains("prep_earnings_call"));
    }
}
