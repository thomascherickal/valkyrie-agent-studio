pub fn calc_unit_cogs(input: &str) -> String {
    format!("[calc_unit_cogs] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[08-unit-economics-tracker:gemini-4-hydrogen:low] {}", calc_unit_cogs(input))
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
        assert!(out.contains("08-unit-economics-tracker"));
        assert!(out.contains("calc_unit_cogs"));
    }
}
