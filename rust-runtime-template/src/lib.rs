//! Base runtime traits, Gemini 4 Hydrogen (Low) client config, and cost tracker.

pub mod mock_llm;

use serde::{Deserialize, Serialize};

pub const INPUT_COST_PER_M: f64 = 1.50;
pub const OUTPUT_COST_PER_M: f64 = 7.50;
pub const CACHE_READ_COST_PER_M: f64 = 0.075;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct ModelConfig {
    pub provider: String,
    pub model: String,
    pub thinking_level: String,
}

impl Default for ModelConfig {
    fn default() -> Self {
        Self {
            provider: "gemini".to_string(),
            model: "gemini-4-hydrogen".to_string(),
            thinking_level: "low".to_string(),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct AgentResult {
    pub content: String,
    pub input_tokens: u64,
    pub output_tokens: u64,
    pub cached_tokens: u64,
    pub cost_usd: f64,
}

pub fn calculate_cost_usd(
    provider: &str,
    input_tokens: u64,
    output_tokens: u64,
    cached_tokens: u64,
) -> f64 {
    if provider == "ollama" {
        return 0.0;
    }
    let uncached = input_tokens.saturating_sub(cached_tokens) as f64;
    (uncached / 1_000_000.0) * INPUT_COST_PER_M
        + (cached_tokens as f64 / 1_000_000.0) * CACHE_READ_COST_PER_M
        + (output_tokens as f64 / 1_000_000.0) * OUTPUT_COST_PER_M
}

pub trait ValkyrieAgent {
    fn id(&self) -> &str;
    fn execute(&self, prompt: &str) -> AgentResult;
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::mock_llm::MockGeminiAgent;

    #[test]
    fn test_default_model_config() {
        let cfg = ModelConfig::default();
        assert_eq!(cfg.provider, "gemini");
        assert_eq!(cfg.model, "gemini-4-hydrogen");
        assert_eq!(cfg.thinking_level, "low");
    }

    #[test]
    fn test_cost_calculation() {
        assert_eq!(calculate_cost_usd("ollama", 1_000_000, 1_000_000, 0), 0.0);
        let cost = calculate_cost_usd("gemini", 1_000_000, 1_000_000, 500_000);
        assert!((cost - 8.2875).abs() < 1e-6);
    }

    #[test]
    fn test_mock_agent_execution() {
        let agent = MockGeminiAgent::new("prd-architect");
        assert_eq!(agent.id(), "prd-architect");
        let res = agent.execute("Draft PRD");
        assert!(res.content.contains("gemini-4-hydrogen:low"));
        assert!(res.cost_usd > 0.0);
    }
}

