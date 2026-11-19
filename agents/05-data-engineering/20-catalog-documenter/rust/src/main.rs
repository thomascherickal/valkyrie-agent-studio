pub fn document_dataset(input: &str) -> String {
    format!("[document_dataset] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-catalog-documenter:gemini-4-hydrogen:low] {}", document_dataset(input))
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
        assert!(out.contains("20-catalog-documenter"));
        assert!(out.contains("document_dataset"));
    }
}
