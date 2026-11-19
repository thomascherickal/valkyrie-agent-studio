pub fn facilitate_retro(input: &str) -> String {
    format!("[facilitate_retro] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-retro-facilitator:gemini-4-hydrogen:low] {}", facilitate_retro(input))
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
        assert!(out.contains("14-retro-facilitator"));
        assert!(out.contains("facilitate_retro"));
    }
}
