pub fn build_rubric_grid(input: &str) -> String {
    format!("[build_rubric_grid] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-hiring-rubric-builder:gemini-4-hydrogen:low] {}", build_rubric_grid(input))
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
        assert!(out.contains("04-hiring-rubric-builder"));
        assert!(out.contains("build_rubric_grid"));
    }
}
