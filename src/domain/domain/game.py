"""Модель текущей игры для Крестики-Нолики."""

import uuid

from domain.domain.board import Board


class Game:
    """Модель игры с UUID и игровым полем."""
    
    def __init__(self, game_id: str = None, board: Board = None):
        """Инициализация игры.
        
        Args:
            game_id: UUID игры. Если None, генерируется новый.
            board: Игровое поле. Если None, создается пустая доска.
        """
        self._id = game_id if game_id else str(uuid.uuid4())
        self._board = board if board else Board()
    
    @property
    def id(self) -> str:
        """Возвращает UUID игры."""
        return self._id
    
    @property
    def board(self) -> Board:
        """Возвращает игровое поле."""
        return self._board
    
    @board.setter
    def board(self, value: Board) -> None:
        """Устанавливает игровое поле."""
        self._board = value
    
    def copy(self) -> 'Game':
        """Создает копию игры."""
        return Game(game_id=self._id, board=self._board.copy())
    
    def __eq__(self, other: object) -> bool:
        """Сравнение игр."""
        if not isinstance(other, Game):
            return False
        return self._id == other._id and self._board == other._board
    
    def __repr__(self) -> str:
        return f"Game(id='{self._id}', board={self._board})"
