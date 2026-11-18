pub fn cluster_verbatims(input: &str) -> String {
    format!("[cluster_verbatims] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-voice-of-customer:gemini-4-hydrogen:low] {}", cluster_verbatims(input))
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
        assert!(out.contains("05-voice-of-customer"));
        assert!(out.contains("cluster_verbatims"));
    }
}
