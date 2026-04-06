from abc import ABC, abstractmethod
from enum import Enum


class NotificationEvent(Enum):
    TASK_CREATED = "TASK_CREATED"
    STATUS_CHANGED = "STATUS_CHANGED"
    TASK_DONE = "TASK_DONE"


class NotificationPolicy(ABC):
    @abstractmethod
    def should_notify(self, event: NotificationEvent) -> bool:
        pass


class AlwaysNotify(NotificationPolicy):
    def should_notify(self, event: NotificationEvent) -> bool:
        return event in {
            NotificationEvent.TASK_CREATED,
            NotificationEvent.STATUS_CHANGED,
            NotificationEvent.TASK_DONE
        }


class NotifyOnDoneOnly(NotificationPolicy):
    def should_notify(self, event: NotificationEvent) -> bool:
        return event == NotificationEvent.TASK_DONE


class NotificationService:
    def __init__(self, policy: NotificationPolicy):
        self.policy = policy

    def notify(self, event: NotificationEvent, message: str) -> None:
        if self.policy.should_notify(event):
            print(f"Notificacion enviada: [{event.value}] {message}")
        else:
            print(f"No se envia notificacion para el evento: {event.value}")


if __name__ == "__main__":
    service1 = NotificationService(AlwaysNotify())
    service1.notify(NotificationEvent.TASK_CREATED, "Se ha creado una nueva tarea")
    service1.notify(NotificationEvent.STATUS_CHANGED, "La tarea cambió de estado")
    service1.notify(NotificationEvent.TASK_DONE, "La tarea fue completada")

    print("-----")

    service2 = NotificationService(NotifyOnDoneOnly())
    service2.notify(NotificationEvent.TASK_CREATED, "Se ha creado una nueva tarea")
    service2.notify(NotificationEvent.STATUS_CHANGED, "La tarea cambió de estado")
    service2.notify(NotificationEvent.TASK_DONE, "La tarea fue completada")
