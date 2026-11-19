pub fn review_mutation_survivors(input: &str) -> String {
    format!("[review_mutation_survivors] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-mutation-test-reviewer:gemini-4-hydrogen:low] {}", review_mutation_survivors(input))
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
        assert!(out.contains("13-mutation-test-reviewer"));
        assert!(out.contains("review_mutation_survivors"));
    }
}
