from crewai.events import (
    BaseEventListener,
    AgentExecutionStartedEvent,
    AgentExecutionCompletedEvent,
    AgentExecutionErrorEvent,
)



class Listener(BaseEventListener):
    def __init__(self):
        super().__init__()
        self.worker_actif = None

    def setup_listeners(self, crewai_event_bus):

        @crewai_event_bus.on(AgentExecutionStartedEvent)
        def _(source, event):
            if self.worker_actif:
                self.worker_actif.text_log.emit(f"[{event.agent.role}] démarre...")
                self.worker_actif.status_agent.emit(event.agent.role, "en_cours")

        @crewai_event_bus.on(AgentExecutionCompletedEvent)
        def _(source, event):
            if self.worker_actif:
                self.worker_actif.text_log.emit(f"[{event.agent.role}] terminé.")
                self.worker_actif.status_agent.emit(event.agent.role, "termine")

        @crewai_event_bus.on(AgentExecutionErrorEvent)
        def _(source, event):
            if self.worker_actif:
                self.worker_actif.text_log.emit(f"[{event.agent.role}] ERREUR : {event.error}")
                self.worker_actif.status_agent.emit(event.agent.role, "erreur")

listener = Listener()