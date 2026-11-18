pub fn enumerate_boundaries(input: &str) -> String {
    format!("[enumerate_boundaries] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-edge-case-hunter:gemini-4-hydrogen:low] {}", enumerate_boundaries(input))
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
        assert!(out.contains("02-edge-case-hunter"));
        assert!(out.contains("enumerate_boundaries"));
    }
}
