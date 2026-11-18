pub fn model_viral_k_factor(input: &str) -> String {
    format!("[model_viral_k_factor] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-plg-loop-designer:gemini-4-hydrogen:low] {}", model_viral_k_factor(input))
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
        assert!(out.contains("09-plg-loop-designer"));
        assert!(out.contains("model_viral_k_factor"));
    }
}
