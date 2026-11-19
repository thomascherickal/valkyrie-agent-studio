pub fn compare_build_buy(input: &str) -> String {
    format!("[compare_build_buy] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[19-build-buy-evaluator:gemini-4-hydrogen:low] {}", compare_build_buy(input))
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
        assert!(out.contains("19-build-buy-evaluator"));
        assert!(out.contains("compare_build_buy"));
    }
}
