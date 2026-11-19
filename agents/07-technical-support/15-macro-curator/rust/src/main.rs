pub fn curate_macros(input: &str) -> String {
    format!("[curate_macros] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-macro-curator:gemini-4-hydrogen:low] {}", curate_macros(input))
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
        assert!(out.contains("15-macro-curator"));
        assert!(out.contains("curate_macros"));
    }
}
