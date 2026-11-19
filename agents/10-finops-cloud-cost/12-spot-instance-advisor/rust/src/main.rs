pub fn assess_spot_fit(input: &str) -> String {
    format!("[assess_spot_fit] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-spot-instance-advisor:gemini-4-hydrogen:low] {}", assess_spot_fit(input))
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
        assert!(out.contains("12-spot-instance-advisor"));
        assert!(out.contains("assess_spot_fit"));
    }
}
