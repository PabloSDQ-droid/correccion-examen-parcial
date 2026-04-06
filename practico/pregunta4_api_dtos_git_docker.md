# Pregunta 4A - Endpoints con DTOs

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

app = FastAPI()


class TaskCreateRequest(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    priority: str
    assignee_id: Optional[int] = None


class TaskResponse(BaseModel):
    id: str
    title: str
    priority: str
    status: str
    created_at: datetime


class Task:
    def __init__(
        self,
        id: str,
        title: str,
        description: Optional[str],
        priority: str,
        status: str,
        assignee_id: Optional[int],
        created_at: datetime
    ):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.assignee_id = assignee_id
        self.created_at = created_at


class TaskService:
    def create_task(self, request: TaskCreateRequest) -> Task:
        valid_priorities = {"LOW", "MEDIUM", "HIGH"}
        if request.priority not in valid_priorities:
            raise ValueError("priority debe ser LOW, MEDIUM o HIGH")

        return Task(
            id=str(uuid.uuid4()),
            title=request.title,
            description=request.description,
            priority=request.priority,
            status="OPEN",
            assignee_id=request.assignee_id,
            created_at=datetime.utcnow()
        )


task_service = TaskService()


@app.post("/tasks", response_model=TaskResponse)
def create_task(request: TaskCreateRequest) -> TaskResponse:
    task = task_service.create_task(request)
    return TaskResponse(
        id=task.id,
        title=task.title,
        priority=task.priority,
        status=task.status,
        created_at=task.created_at
    )
```

# Pregunta 4B - Comandos Git + Docker

```bash
git init
git checkout -b feature/tasks
git add .
git commit -m "feat: add exam correction practical solutions"
git remote add origin https://github.com/PabloSDQ-droid/correccion-examen-parcial.git
git push -u origin feature/tasks
```

```bash
docker compose up -d
docker compose down
```
