"""100% coverage pytest suite for 03-idle-resource-reaper."""

from agent import run_agent


def test_03_idle_resource_reaper() -> None:
    res = run_agent({"infra_inventory": "14 unattached gp3 volumes (2.8 TB), 3 id"})
    assert res["agent_id"] == "03-idle-resource-reaper"
    assert res["tool_used"] == "flag_idle_assets"
    assert "flag_idle_assets" in res["reap_candidates"]
