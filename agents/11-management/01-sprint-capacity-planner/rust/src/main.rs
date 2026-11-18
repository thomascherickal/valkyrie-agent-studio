pub fn calc_net_capacity(input: &str) -> String {
    format!("[calc_net_capacity] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-sprint-capacity-planner:gemini-4-hydrogen:low] {}", calc_net_capacity(input))
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
        assert!(out.contains("01-sprint-capacity-planner"));
        assert!(out.contains("calc_net_capacity"));
    }
}
