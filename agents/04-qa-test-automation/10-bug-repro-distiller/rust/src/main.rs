pub fn distill_min_repro(input: &str) -> String {
    format!("[distill_min_repro] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-bug-repro-distiller:gemini-4-hydrogen:low] {}", distill_min_repro(input))
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
        assert!(out.contains("10-bug-repro-distiller"));
        assert!(out.contains("distill_min_repro"));
    }
}
