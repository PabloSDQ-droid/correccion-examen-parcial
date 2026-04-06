from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid


class TaskStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class TaskPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class Task:
    id: str
    title: str
    description: Optional[str]
    priority: str
    status: TaskStatus
    assignee_id: Optional[int]
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("title no puede estar vacio")

        valid_priorities = {p.value for p in TaskPriority}
        if self.priority not in valid_priorities:
            raise ValueError("priority debe ser LOW, MEDIUM o HIGH")

        if self.status != TaskStatus.OPEN:
            raise ValueError("el estado inicial siempre debe ser OPEN")


class TaskFactory:
    @staticmethod
    def create_task(
        title: str,
        description: Optional[str] = None,
        priority: str = "MEDIUM",
        assignee_id: Optional[int] = None
    ) -> Task:
        if not title or not title.strip():
            raise ValueError("title no puede estar vacio")

        valid_priorities = {p.value for p in TaskPriority}
        if priority not in valid_priorities:
            raise ValueError("priority debe ser LOW, MEDIUM o HIGH")

        return Task(
            id=str(uuid.uuid4()),
            title=title.strip(),
            description=description,
            priority=priority,
            status=TaskStatus.OPEN,
            assignee_id=assignee_id,
            created_at=datetime.utcnow()
        )


if __name__ == "__main__":
    task = TaskFactory.create_task(
        title="Revisar inventario",
        description="Contar productos en bodega",
        priority="HIGH",
        assignee_id=101
    )
    print(task)
