pub fn find_egress_leaks(input: &str) -> String {
    format!("[find_egress_leaks] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-egress-cost-reducer:gemini-4-hydrogen:low] {}", find_egress_leaks(input))
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
        assert!(out.contains("06-egress-cost-reducer"));
        assert!(out.contains("find_egress_leaks"));
    }
}
