from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="TaskFlow API")

# Active automatiquement l'endpoint /metrics pour Prometheus
Instrumentator().instrument(app).expose(app)

class Task(BaseModel):
    title: str
    done: bool = False

tasks_db = []

@app.get("/health")
def health_check():
    """Utilisé par les sondes Liveness et Readiness de Kubernetes."""
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks():
    return {"tasks": tasks_db}

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    tasks_db.append(task.model_dump())
    return task