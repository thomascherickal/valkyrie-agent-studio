pub fn flag_idle_assets(input: &str) -> String {
    format!("[flag_idle_assets] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[03-idle-resource-reaper:gemini-4-hydrogen:low] {}", flag_idle_assets(input))
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
        assert!(out.contains("03-idle-resource-reaper"));
        assert!(out.contains("flag_idle_assets"));
    }
}
