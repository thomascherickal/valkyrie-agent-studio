pub fn map_code_owners(input: &str) -> String {
    format!("[map_code_owners] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-code-owner-mapper:gemini-4-hydrogen:low] {}", map_code_owners(input))
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
        assert!(out.contains("19-code-owner-mapper"));
        assert!(out.contains("map_code_owners"));
    }
}
