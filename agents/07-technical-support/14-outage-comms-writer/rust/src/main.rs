pub fn write_outage_comms(input: &str) -> String {
    format!("[write_outage_comms] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-outage-comms-writer:gemini-4-hydrogen:low] {}", write_outage_comms(input))
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
        assert!(out.contains("14-outage-comms-writer"));
        assert!(out.contains("write_outage_comms"));
    }
}
