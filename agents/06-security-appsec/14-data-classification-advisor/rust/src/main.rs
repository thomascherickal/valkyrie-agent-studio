pub fn classify_data(input: &str) -> String {
    format!("[classify_data] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-data-classification-advisor:gemini-4-hydrogen:low] {}", classify_data(input))
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
        assert!(out.contains("14-data-classification-advisor"));
        assert!(out.contains("classify_data"));
    }
}
