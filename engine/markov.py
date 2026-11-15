import random
import re
from collections import defaultdict, Counter

def tokenize(text: str):
    return re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)

def generate(text: str, order: int = 1, length: int = 40, seed: int | None = None):
    if order not in (1, 2):
        raise ValueError("order must be 1 or 2")
    if not 1 <= length <= 300:
        raise ValueError("length must be between 1 and 300")
    tokens = tokenize(text)
    if len(tokens) <= order:
        raise ValueError("Corpus is too short for the selected order")
    rng = random.Random(seed)
    transitions = defaultdict(Counter)
    for i in range(order, len(tokens)):
        transitions[tuple(tokens[i-order:i])][tokens[i]] += 1
    states = list(transitions)
    state = rng.choice(states)
    output = list(state)
    for _ in range(length):
        choices = transitions.get(state)
        if not choices:
            state = rng.choice(states)
            choices = transitions[state]
        words, weights = zip(*choices.items())
        nxt = rng.choices(words, weights=weights, k=1)[0]
        output.append(nxt)
        state = tuple(output[-order:])
    result = " ".join(output)
    result = re.sub(r"\s+([,.;:!?])", r"\1", result)
    return result
