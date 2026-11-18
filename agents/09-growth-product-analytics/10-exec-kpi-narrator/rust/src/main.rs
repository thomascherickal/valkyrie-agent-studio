pub fn narrate_weekly_kpis(input: &str) -> String {
    format!("[narrate_weekly_kpis] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-exec-kpi-narrator:gemini-4-hydrogen:low] {}", narrate_weekly_kpis(input))
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
        assert!(out.contains("10-exec-kpi-narrator"));
        assert!(out.contains("narrate_weekly_kpis"));
    }
}
