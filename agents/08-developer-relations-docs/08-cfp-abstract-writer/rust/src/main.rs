pub fn polish_cfp_abstract(input: &str) -> String {
    format!("[polish_cfp_abstract] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-cfp-abstract-writer:gemini-4-hydrogen:low] {}", polish_cfp_abstract(input))
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
        assert!(out.contains("08-cfp-abstract-writer"));
        assert!(out.contains("polish_cfp_abstract"));
    }
}
