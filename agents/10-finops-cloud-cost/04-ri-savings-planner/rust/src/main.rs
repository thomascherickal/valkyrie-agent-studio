pub fn model_commitment_roi(input: &str) -> String {
    format!("[model_commitment_roi] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-ri-savings-planner:gemini-4-hydrogen:low] {}", model_commitment_roi(input))
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
        assert!(out.contains("04-ri-savings-planner"));
        assert!(out.contains("model_commitment_roi"));
    }
}
