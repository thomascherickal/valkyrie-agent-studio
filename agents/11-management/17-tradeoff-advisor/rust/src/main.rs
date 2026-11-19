pub fn weigh_tradeoffs(input: &str) -> String {
    format!("[weigh_tradeoffs] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-tradeoff-advisor:gemini-4-hydrogen:low] {}", weigh_tradeoffs(input))
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
        assert!(out.contains("17-tradeoff-advisor"));
        assert!(out.contains("weigh_tradeoffs"));
    }
}
