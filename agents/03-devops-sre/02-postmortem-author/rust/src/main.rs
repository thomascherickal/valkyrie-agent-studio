pub fn generate_five_whys(input: &str) -> String {
    format!("[generate_five_whys] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-postmortem-author:gemini-4-hydrogen:low] {}", generate_five_whys(input))
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
        assert!(out.contains("02-postmortem-author"));
        assert!(out.contains("generate_five_whys"));
    }
}
