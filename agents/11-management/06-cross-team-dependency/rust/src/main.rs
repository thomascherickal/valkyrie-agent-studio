pub fn map_critical_path(input: &str) -> String {
    format!("[map_critical_path] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-cross-team-dependency:gemini-4-hydrogen:low] {}", map_critical_path(input))
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
        assert!(out.contains("06-cross-team-dependency"));
        assert!(out.contains("map_critical_path"));
    }
}
