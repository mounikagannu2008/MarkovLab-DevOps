from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from markov import generate

app = FastAPI(title="MarkovLab Engine", version="1.0.0")

class GenerateRequest(BaseModel):
    corpus: str = Field(min_length=10, max_length=100000)
    order: int = Field(default=1, ge=1, le=2)
    length: int = Field(default=40, ge=1, le=300)
    seed: int | None = None

@app.get("/health")
def health():
    return {"status": "ok", "service": "markov-engine"}

@app.post("/generate")
def generate_text(request: GenerateRequest):
    try:
        return {"text": generate(request.corpus, request.order, request.length, request.seed),
                "order": request.order, "tokens_requested": request.length}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
