pub fn calc_funnel_rates(input: &str) -> String {
    format!("[calc_funnel_rates] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-funnel-dropoff-analyst:gemini-4-hydrogen:low] {}", calc_funnel_rates(input))
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
        assert!(out.contains("01-funnel-dropoff-analyst"));
        assert!(out.contains("calc_funnel_rates"));
    }
}
