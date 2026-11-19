pub fn optimize_seats(input: &str) -> String {
    format!("[optimize_seats] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-saas-license-optimizer:gemini-4-hydrogen:low] {}", optimize_seats(input))
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
        assert!(out.contains("19-saas-license-optimizer"));
        assert!(out.contains("optimize_seats"));
    }
}
