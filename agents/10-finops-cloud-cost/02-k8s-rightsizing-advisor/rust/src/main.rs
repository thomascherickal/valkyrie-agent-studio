pub fn compute_rightsize(input: &str) -> String {
    format!("[compute_rightsize] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-k8s-rightsizing-advisor:gemini-4-hydrogen:low] {}", compute_rightsize(input))
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
        assert!(out.contains("02-k8s-rightsizing-advisor"));
        assert!(out.contains("compute_rightsize"));
    }
}
