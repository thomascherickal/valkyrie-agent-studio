pub fn emit_dbt_model(input: &str) -> String {
    format!("[emit_dbt_model] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[02-dbt-model-generator:gemini-4-hydrogen:low] {}", emit_dbt_model(input))
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
        assert!(out.contains("02-dbt-model-generator"));
        assert!(out.contains("emit_dbt_model"));
    }
}
