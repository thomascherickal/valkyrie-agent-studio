pub fn find_segments(input: &str) -> String {
    format!("[find_segments] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-segment-discovery-analyst:gemini-4-hydrogen:low] {}", find_segments(input))
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
        assert!(out.contains("16-segment-discovery-analyst"));
        assert!(out.contains("find_segments"));
    }
}
