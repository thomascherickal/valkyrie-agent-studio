pub fn compute_channel_roi(input: &str) -> String {
    format!("[compute_channel_roi] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-attribution-mapper:gemini-4-hydrogen:low] {}", compute_channel_roi(input))
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
        assert!(out.contains("06-attribution-mapper"));
        assert!(out.contains("compute_channel_roi"));
    }
}
