pub fn define_semantic_metric(input: &str) -> String {
    format!("[define_semantic_metric] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-metric-layer-definer:gemini-4-hydrogen:low] {}", define_semantic_metric(input))
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
        assert!(out.contains("10-metric-layer-definer"));
        assert!(out.contains("define_semantic_metric"));
    }
}
