pub fn outline_tech_post(input: &str) -> String {
    format!("[outline_tech_post] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-tech-blog-outliner:gemini-4-hydrogen:low] {}", outline_tech_post(input))
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
        assert!(out.contains("16-tech-blog-outliner"));
        assert!(out.contains("outline_tech_post"));
    }
}
