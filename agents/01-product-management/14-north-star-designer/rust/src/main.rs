pub fn define_north_star(input: &str) -> String {
    format!("[define_north_star] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[14-north-star-designer:gemini-4-hydrogen:low] {}", define_north_star(input))
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
        assert!(out.contains("14-north-star-designer"));
        assert!(out.contains("define_north_star"));
    }
}
