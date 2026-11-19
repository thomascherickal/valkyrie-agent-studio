pub fn map_blast_radius(input: &str) -> String {
    format!("[map_blast_radius] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-blast-radius-mapper:gemini-4-hydrogen:low] {}", map_blast_radius(input))
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
        assert!(out.contains("16-blast-radius-mapper"));
        assert!(out.contains("map_blast_radius"));
    }
}
