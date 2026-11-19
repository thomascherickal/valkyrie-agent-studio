pub fn report_devrel_metrics(input: &str) -> String {
    format!("[report_devrel_metrics] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-devrel-metrics-reporter:gemini-4-hydrogen:low] {}", report_devrel_metrics(input))
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
        assert!(out.contains("15-devrel-metrics-reporter"));
        assert!(out.contains("report_devrel_metrics"));
    }
}
