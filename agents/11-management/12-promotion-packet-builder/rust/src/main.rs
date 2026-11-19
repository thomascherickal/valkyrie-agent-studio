pub fn build_promo_packet(input: &str) -> String {
    format!("[build_promo_packet] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-promotion-packet-builder:gemini-4-hydrogen:low] {}", build_promo_packet(input))
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
        assert!(out.contains("12-promotion-packet-builder"));
        assert!(out.contains("build_promo_packet"));
    }
}
