pub fn compile_finops_brief(input: &str) -> String {
    format!("[compile_finops_brief] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-finops-monthly-brief:gemini-4-hydrogen:low] {}", compile_finops_brief(input))
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
        assert!(out.contains("10-finops-monthly-brief"));
        assert!(out.contains("compile_finops_brief"));
    }
}
