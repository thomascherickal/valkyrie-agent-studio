"""100% coverage pytest suite for 19-crypto-usage-reviewer."""

from agent import run_agent


def test_19_crypto_usage_reviewer() -> None:
    res = run_agent({"code_snippet": "hash = md5(password); key = 'hardcoded-secret'; token = random.randint(100000, 999999); AES in ECB mode"})
    assert res["agent_id"] == "19-crypto-usage-reviewer"
    assert res["tool_used"] == "review_crypto_usage"
    assert "review_crypto_usage" in res["crypto_findings"]
