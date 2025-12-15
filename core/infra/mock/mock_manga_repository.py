from typing import List, Optional

from core.domain.entity import Manga  # Assumindo que você usa esta entidade
from core.domain.repositories import IMangaRepository


class MockMangaRepository(IMangaRepository):
    """
    Implementação Mock robusta para testes de Manga, seguindo o padrão
    Singleton e usando métodos assíncronos.
    """

    def __init__(self):
        # Armazenamento em memória
        self.mangas: List[Manga] = []

    async def save(self, manga: Manga) -> None:
        """Adiciona um novo mangá ou atualiza um existente."""

        # 1. Tenta encontrar o índice do mangá existente pelo ID
        index = next((i for i, m in enumerate(self.mangas) if m.id == manga.id), None)

        if index is not None:
            # 2. Se encontrado, atualiza
            self.mangas[index] = manga
        else:
            # 3. Caso contrário, adiciona (nova inserção)
            self.mangas.append(manga)

    # O método 'update' não é estritamente necessário se 'save' fizer upsert
    # Mas se você quiser um método update explícito (como no MockUserRepository):
    async def update(self, manga: Manga) -> None:
        """Atualiza um mangá existente pelo ID."""
        index = next((i for i, m in enumerate(self.mangas) if m.id == manga.id), None)
        if index is not None:
            self.mangas[index] = manga

    async def delete(self, id: str) -> None:
        """Remove um mangá pelo ID."""
        # Filtra a lista, mantendo apenas os mangás que NÃO têm o ID fornecido
        self.mangas = [manga for manga in self.mangas if manga.id != id]

    # --- Métodos de Busca (Não alterados) ---

    async def find_by_id(self, id: str) -> Optional[Manga]:
        """Busca um mangá pelo ID, retornando None se não encontrado."""
        return next((manga for manga in self.mangas if manga.id == id), None)

    async def find_by_title(self, title: str) -> Optional[Manga]:
        """Busca um mangá pelo título, retornando None se não encontrado."""
        # Se title for um Value Object (como sugerido anteriormente), use .value
        # Caso contrário, use apenas .title
        return next(
            (manga for manga in self.mangas if manga.title.value == title), None
        )

    async def find_all(self) -> List[Manga]:
        """Retorna a lista de todos os mangás."""
        return list(self.mangas)

    async def find_by_author_name(self, author_name: str) -> List[Manga]:
        """Busca mangás pelo nome do autor."""
        return [manga for manga in self.mangas if manga.author_name == author_name]
