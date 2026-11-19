pub fn plan_product_ops_cadence(input: &str) -> String {
    format!("[plan_product_ops_cadence] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-product-ops-cadence-planner:gemini-4-hydrogen:low] {}", plan_product_ops_cadence(input))
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
        assert!(out.contains("20-product-ops-cadence-planner"));
        assert!(out.contains("plan_product_ops_cadence"));
    }
}
