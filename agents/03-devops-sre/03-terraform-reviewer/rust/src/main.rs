pub fn inspect_tf_blast(input: &str) -> String {
    format!("[inspect_tf_blast] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-terraform-reviewer:gemini-4-hydrogen:low] {}", inspect_tf_blast(input))
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
        assert!(out.contains("03-terraform-reviewer"));
        assert!(out.contains("inspect_tf_blast"));
    }
}
