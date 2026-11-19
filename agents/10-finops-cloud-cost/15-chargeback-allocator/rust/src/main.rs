pub fn allocate_shared_cost(input: &str) -> String {
    format!("[allocate_shared_cost] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-chargeback-allocator:gemini-4-hydrogen:low] {}", allocate_shared_cost(input))
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
        assert!(out.contains("15-chargeback-allocator"));
        assert!(out.contains("allocate_shared_cost"));
    }
}
