import random
from dataclasses import dataclass, field
from typing import List, Callable, Optional

def sample_outputs(generator: Callable[[], str], count: int = 100) -> List[str]:
    """Generate a sample of model outputs."""
    return [generator() for _ in range(count)]

def is_hallucinated(output: str) -> bool:
    """Simple heuristic: consider output hallucinated if it contains the word 'hallucination'."""
    return "hallucination" in output.lower()

def hallucination_score(outputs: List[str]) -> float:
    """
    Calculate hallucination score as a percentage (0-100).
    Higher score means more hallucination.
    """
    if not outputs:
        raise ValueError("No outputs provided for scoring.")
    hallucinated = sum(1 for o in outputs if is_hallucinated(o))
    return (hallucinated / len(outputs)) * 100

@dataclass
class PromptVersion:
    """Represents a prompt version with its hallucination score."""
    prompt_id: str
    version: int
    generator: Callable[[], str]
    sample_size: int = 100
    threshold: float = 70.0
    _score: Optional[float] = field(default=None, init=False, repr=False)

    def compute_score(self) -> float:
        """Compute and store the hallucination score."""
        outputs = sample_outputs(self.generator, self.sample_size)
        self._score = hallucination_score(outputs)
        return self._score

    @property
    def score(self) -> float:
        if self._score is None:
            raise RuntimeError("Score not computed yet. Call compute_score() first.")
        return self._score

    def alert(self) -> bool:
        """Return True if score exceeds threshold."""
        return self.score > self.threshold
