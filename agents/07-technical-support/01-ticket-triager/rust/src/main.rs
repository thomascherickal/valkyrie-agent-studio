pub fn classify_ticket_sla(input: &str) -> String {
    format!("[classify_ticket_sla] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[01-ticket-triager:gemini-4-hydrogen:low] {}", classify_ticket_sla(input))
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
        assert!(out.contains("01-ticket-triager"));
        assert!(out.contains("classify_ticket_sla"));
    }
}
