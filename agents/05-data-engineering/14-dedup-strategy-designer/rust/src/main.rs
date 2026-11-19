pub fn design_dedup(input: &str) -> String {
    format!("[design_dedup] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-dedup-strategy-designer:gemini-4-hydrogen:low] {}", design_dedup(input))
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
        assert!(out.contains("14-dedup-strategy-designer"));
        assert!(out.contains("design_dedup"));
    }
}
