pub fn compile_esg_metrics(input: &str) -> String {
    format!("[compile_esg_metrics] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-esg-metrics-reporter:gemini-4-hydrogen:low] {}", compile_esg_metrics(input))
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
        assert!(out.contains("19-esg-metrics-reporter"));
        assert!(out.contains("compile_esg_metrics"));
    }
}
