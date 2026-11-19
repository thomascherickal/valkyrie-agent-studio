pub fn analyze_gpu_use(input: &str) -> String {
    format!("[analyze_gpu_use] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-gpu-utilization-analyst:gemini-4-hydrogen:low] {}", analyze_gpu_use(input))
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
        assert!(out.contains("20-gpu-utilization-analyst"));
        assert!(out.contains("analyze_gpu_use"));
    }
}
