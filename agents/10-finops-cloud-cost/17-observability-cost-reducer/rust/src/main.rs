pub fn trim_telemetry_cost(input: &str) -> String {
    format!("[trim_telemetry_cost] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[17-observability-cost-reducer:gemini-4-hydrogen:low] {}", trim_telemetry_cost(input))
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
        assert!(out.contains("17-observability-cost-reducer"));
        assert!(out.contains("trim_telemetry_cost"));
    }
}
