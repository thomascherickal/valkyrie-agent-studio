pub fn run_stride_analysis(input: &str) -> String {
    format!("[run_stride_analysis] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-threat-modeler:gemini-4-hydrogen:low] {}", run_stride_analysis(input))
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
        assert!(out.contains("01-threat-modeler"));
        assert!(out.contains("run_stride_analysis"));
    }
}
