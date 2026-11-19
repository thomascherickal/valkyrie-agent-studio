pub fn map_developer_journey(input: &str) -> String {
    format!("[map_developer_journey] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-developer-journey-mapper:gemini-4-hydrogen:low] {}", map_developer_journey(input))
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
        assert!(out.contains("20-developer-journey-mapper"));
        assert!(out.contains("map_developer_journey"));
    }
}
