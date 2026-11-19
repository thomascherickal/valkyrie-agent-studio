pub fn triage_visual_diffs(input: &str) -> String {
    format!("[triage_visual_diffs] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-visual-regression-triager:gemini-4-hydrogen:low] {}", triage_visual_diffs(input))
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
        assert!(out.contains("14-visual-regression-triager"));
        assert!(out.contains("triage_visual_diffs"));
    }
}
