pub fn calc_ab_sample_size(input: &str) -> String {
    format!("[calc_ab_sample_size] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-experiment-designer:gemini-4-hydrogen:low] {}", calc_ab_sample_size(input))
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
        assert!(out.contains("08-experiment-designer"));
        assert!(out.contains("calc_ab_sample_size"));
    }
}
