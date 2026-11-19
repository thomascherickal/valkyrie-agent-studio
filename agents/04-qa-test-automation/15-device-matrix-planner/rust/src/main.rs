pub fn build_device_matrix(input: &str) -> String {
    format!("[build_device_matrix] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-device-matrix-planner:gemini-4-hydrogen:low] {}", build_device_matrix(input))
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
        assert!(out.contains("15-device-matrix-planner"));
        assert!(out.contains("build_device_matrix"));
    }
}
