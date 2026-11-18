pub fn diff_feature_matrix(input: &str) -> String {
    format!("[diff_feature_matrix] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-competitive-intel:gemini-4-hydrogen:low] {}", diff_feature_matrix(input))
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
        assert!(out.contains("04-competitive-intel"));
        assert!(out.contains("diff_feature_matrix"));
    }
}
