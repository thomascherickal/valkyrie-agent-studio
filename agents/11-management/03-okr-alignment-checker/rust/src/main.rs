pub fn score_okr_fit(input: &str) -> String {
    format!("[score_okr_fit] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-okr-alignment-checker:gemini-4-hydrogen:low] {}", score_okr_fit(input))
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
        assert!(out.contains("03-okr-alignment-checker"));
        assert!(out.contains("score_okr_fit"));
    }
}
