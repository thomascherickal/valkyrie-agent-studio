pub fn analyze_az_traffic(input: &str) -> String {
    format!("[analyze_az_traffic] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-cross-az-traffic-analyst:gemini-4-hydrogen:low] {}", analyze_az_traffic(input))
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
        assert!(out.contains("13-cross-az-traffic-analyst"));
        assert!(out.contains("analyze_az_traffic"));
    }
}
