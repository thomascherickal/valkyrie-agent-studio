"""100% coverage pytest suite for 06-tutorial-video-scripter."""

from agent import run_agent


def test_06_tutorial_video_scripter() -> None:
    res = run_agent({"topic": "Metaheuristic pymoo agent tuning every 3"})
    assert res["agent_id"] == "06-tutorial-video-scripter"
    assert res["tool_used"] == "script_video_beats"
    assert "script_video_beats" in res["video_script"]
