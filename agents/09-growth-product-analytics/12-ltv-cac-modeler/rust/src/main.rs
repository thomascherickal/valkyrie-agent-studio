pub fn model_ltv_cac(input: &str) -> String {
    format!("[model_ltv_cac] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-ltv-cac-modeler:gemini-4-hydrogen:low] {}", model_ltv_cac(input))
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
        assert!(out.contains("12-ltv-cac-modeler"));
        assert!(out.contains("model_ltv_cac"));
    }
}
