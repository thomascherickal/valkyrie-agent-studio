pub fn map_jobs_to_be_done(input: &str) -> String {
    format!("[map_jobs_to_be_done] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[12-jtbd-mapper:gemini-4-hydrogen:low] {}", map_jobs_to_be_done(input))
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
        assert!(out.contains("12-jtbd-mapper"));
        assert!(out.contains("map_jobs_to_be_done"));
    }
}
