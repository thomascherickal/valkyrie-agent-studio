pub fn review_cloud_posture(input: &str) -> String {
    format!("[review_cloud_posture] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-cloud-posture-reviewer:gemini-4-hydrogen:low] {}", review_cloud_posture(input))
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
        assert!(out.contains("17-cloud-posture-reviewer"));
        assert!(out.contains("review_cloud_posture"));
    }
}
