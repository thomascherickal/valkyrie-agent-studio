pub fn find_duplicate_tickets(input: &str) -> String {
    format!("[find_duplicate_tickets] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[13-duplicate-ticket-merger:gemini-4-hydrogen:low] {}", find_duplicate_tickets(input))
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
        assert!(out.contains("13-duplicate-ticket-merger"));
        assert!(out.contains("find_duplicate_tickets"));
    }
}
