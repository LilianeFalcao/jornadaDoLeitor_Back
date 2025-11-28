from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

class ReadingStatus(Enum):
    """
    Enum que representa o status de leitura de um mangá.
    Corresponde a 'export enum Reading_Status'.
    """
    READING = "reading"
    COMPLETED = "completed"
    ALL = "all"

@dataclasses.dataclass
class Reading:
    id: str
    id_user: Optional[str] = None
    id_manga: Optional[str] = None
    start_date: datetime
    _current_chapter: int = field(init=True, repr=False)
    _progress: float = field(init=True, repr=False) # Usando float para progresso (0.0 a 1.0)
    _status: ReadingStatus = field(init=True, repr=False)
    _notes: str = field(init=True, repr=False)

    @property
    def current_chapter(self) -> int:
        """Retorna o capítulo atual da leitura."""
        return self._current_chapter

    @property
    def progress(self) -> float:
        """Retorna o progresso da leitura (0.0 a 1.0)."""
        return self._progress

    @property
    def status(self) -> ReadingStatus:
        """Retorna o status atual da leitura (READING, COMPLETED, ALL)."""
        return self._status

    @property
    def notes(self) -> str:
        """Retorna as anotações sobre a leitura."""
        return self._notes
    
    # ----------------------------------------------------
    # Métodos de Atualização (Setters Funcionais)
    # Correspondem aos métodos 'update' do seu código original.
    # ----------------------------------------------------

    def update_progress(self, current_chapter: int, progress: float, status: ReadingStatus) -> None:
        """
        Atualiza o capítulo atual, progresso e status da leitura.
        Corresponde a updateProgress().
        """
        # Adicione validação, se necessário (ex: if 0.0 <= progress <= 1.0:)
        self._current_chapter = current_chapter
        self._progress = progress
        self._status = status

    def update_notes(self, notes: str) -> None:
        """
        Atualiza as anotações da leitura.
        Corresponde a updateNotes().
        """
        self._notes = notes