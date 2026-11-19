pub fn build_fundraise_story(input: &str) -> String {
    format!("[build_fundraise_story] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-fundraising-narrative-builder:gemini-4-hydrogen:low] {}", build_fundraise_story(input))
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
        assert!(out.contains("12-fundraising-narrative-builder"));
        assert!(out.contains("build_fundraise_story"));
    }
}
