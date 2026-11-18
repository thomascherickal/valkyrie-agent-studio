pub fn narrow_iam_actions(input: &str) -> String {
    format!("[narrow_iam_actions] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-iam-least-privilege:gemini-4-hydrogen:low] {}", narrow_iam_actions(input))
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
        assert!(out.contains("03-iam-least-privilege"));
        assert!(out.contains("narrow_iam_actions"));
    }
}
