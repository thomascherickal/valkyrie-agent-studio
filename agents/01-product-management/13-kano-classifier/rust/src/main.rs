pub fn classify_kano(input: &str) -> String {
    format!("[classify_kano] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-kano-classifier:gemini-4-hydrogen:low] {}", classify_kano(input))
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
        assert!(out.contains("13-kano-classifier"));
        assert!(out.contains("classify_kano"));
    }
}
