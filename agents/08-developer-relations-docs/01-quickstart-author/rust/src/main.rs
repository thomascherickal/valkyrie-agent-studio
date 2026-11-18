pub fn structure_quickstart(input: &str) -> String {
    format!("[structure_quickstart] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-quickstart-author:gemini-4-hydrogen:low] {}", structure_quickstart(input))
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
        assert!(out.contains("01-quickstart-author"));
        assert!(out.contains("structure_quickstart"));
    }
}
