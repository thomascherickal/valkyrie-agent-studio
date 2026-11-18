pub fn format_kb_markdown(input: &str) -> String {
    format!("[format_kb_markdown] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[04-kb-article-drafter:gemini-4-hydrogen:low] {}", format_kb_markdown(input))
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
        assert!(out.contains("04-kb-article-drafter"));
        assert!(out.contains("format_kb_markdown"));
    }
}
