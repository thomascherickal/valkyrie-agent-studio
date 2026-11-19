pub fn design_cdc_flow(input: &str) -> String {
    format!("[design_cdc_flow] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-cdc-pipeline-designer:gemini-4-hydrogen:low] {}", design_cdc_flow(input))
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
        assert!(out.contains("11-cdc-pipeline-designer"));
        assert!(out.contains("design_cdc_flow"));
    }
}
