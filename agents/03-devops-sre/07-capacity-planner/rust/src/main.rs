pub fn model_headroom(input: &str) -> String {
    format!("[model_headroom] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-capacity-planner:gemini-4-hydrogen:low] {}", model_headroom(input))
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
        assert!(out.contains("07-capacity-planner"));
        assert!(out.contains("model_headroom"));
    }
}
