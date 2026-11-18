//! Deterministic mock transport for 100% offline cargo test.

use crate::{calculate_cost_usd, AgentResult, ModelConfig, ValkyrieAgent};

pub struct MockGeminiAgent {
    id: String,
    config: ModelConfig,
}

impl MockGeminiAgent {
    pub fn new(id: &str) -> Self {
        Self {
            id: id.to_string(),
            config: ModelConfig::default(),
        }
    }
}

impl ValkyrieAgent for MockGeminiAgent {
    fn id(&self) -> &str {
        &self.id
    }

    fn execute(&self, prompt: &str) -> AgentResult {
        let input_tokens = 120;
        let output_tokens = 48;
        AgentResult {
            content: format!(
                "[{}:{}] {} -> {}",
                self.config.model, self.config.thinking_level, self.id, prompt
            ),
            input_tokens,
            output_tokens,
            cached_tokens: 0,
            cost_usd: calculate_cost_usd(&self.config.provider, input_tokens, output_tokens, 0),
        }
    }
}

