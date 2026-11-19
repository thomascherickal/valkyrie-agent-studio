pub fn forecast_pipeline(input: &str) -> String {
    format!("[forecast_pipeline] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-pipeline-forecaster:gemini-4-hydrogen:low] {}", forecast_pipeline(input))
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
        assert!(out.contains("18-pipeline-forecaster"));
        assert!(out.contains("forecast_pipeline"));
    }
}
