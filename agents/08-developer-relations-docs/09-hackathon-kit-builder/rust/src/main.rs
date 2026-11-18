pub fn assemble_kit_manifest(input: &str) -> String {
    format!("[assemble_kit_manifest] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[09-hackathon-kit-builder:gemini-4-hydrogen:low] {}", assemble_kit_manifest(input))
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
        assert!(out.contains("09-hackathon-kit-builder"));
        assert!(out.contains("assemble_kit_manifest"));
    }
}
