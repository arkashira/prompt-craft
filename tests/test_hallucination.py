import pytest
from hallucination import (
    sample_outputs,
    is_hallucinated,
    hallucination_score,
    PromptVersion,
)

def always_hallucinate() -> str:
    return "This is a hallucination."

def never_hallucinate() -> str:
    return "This is a real answer."

def test_sample_outputs_length():
    outputs = sample_outputs(always_hallucinate, 10)
    assert len(outputs) == 10
    assert all(o == "This is a hallucination." for o in outputs)

def test_is_hallucinated_true():
    assert is_hallucinated("I think this is a hallucination.") is True

def test_is_hallucinated_false():
    assert is_hallucinated("This is a real answer.") is False

def test_hallucination_score_all_hallucinated():
    outputs = [always_hallucinate() for _ in range(50)]
    score = hallucination_score(outputs)
    assert score == 100.0

def test_hallucination_score_mixed():
    outputs = [always_hallucinate() for _ in range(30)] + [never_hallucinate() for _ in range(70)]
    score = hallucination_score(outputs)
    assert score == 30.0

def test_hallucination_score_empty():
    with pytest.raises(ValueError):
        hallucination_score([])

def test_prompt_version_compute_and_alert():
    pv = PromptVersion(prompt_id="p1", version=1, generator=always_hallucinate, sample_size=20, threshold=70)
    score = pv.compute_score()
    assert score == 100.0
    assert pv.alert() is True

def test_prompt_version_threshold_edge():
    pv = PromptVersion(prompt_id="p2", version=2, generator=never_hallucinate, sample_size=20, threshold=0)
    score = pv.compute_score()
    assert score == 0.0
    assert pv.alert() is False

def test_prompt_version_score_not_computed():
    pv = PromptVersion(prompt_id="p3", version=3, generator=never_hallucinate)
    with pytest.raises(RuntimeError):
        _ = pv.score
