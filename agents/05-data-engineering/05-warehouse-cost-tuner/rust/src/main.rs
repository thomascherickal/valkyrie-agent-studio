pub fn recommend_clustering(input: &str) -> String {
    format!("[recommend_clustering] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[05-warehouse-cost-tuner:gemini-4-hydrogen:low] {}", recommend_clustering(input))
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
        assert!(out.contains("05-warehouse-cost-tuner"));
        assert!(out.contains("recommend_clustering"));
    }
}
