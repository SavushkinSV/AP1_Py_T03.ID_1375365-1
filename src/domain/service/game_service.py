"""Интерфейс сервиса для управления игрой Крестики-Нолики."""

from abc import ABC, abstractmethod

from domain.model.board import Board
from domain.model.game import Game


class GameService(ABC):
    """Абстрактный сервис для управления игрой.
    
    Определяет интерфейс для:
    - Получения следующего хода (алгоритм Минимакс)
    - Валидации игрового поля
    - Проверки окончания игры
    """
    
    @abstractmethod
    def get_next_move(self, game: Game) -> Board:
        """Вычисляет следующий ход компьютера алгоритмом Минимакс.
        
        Args:
            game: Текущая игра.
            
        Returns:
            Новое игровое поле с ходом компьютера.
        """
        pass
    
    @abstractmethod
    def validate_board(self, original_game: Game, updated_game: Game) -> bool:
        """Проверяет, что в игровом поле изменены только допустимые ходы.
        
        Args:
            original_game: Оригинальная игра.
            updated_game: Игра с обновленным полем (ход игрока).
            
        Returns:
            True, если валидация успешна.
        """
        pass
    
    @abstractmethod
    def check_game_end(self, game: Game) -> bool:
        """Проверяет, закончилась ли игра.
        
        Args:
            game: Текущая игра.
            
        Returns:
            True, если игра окончена (победа/поражение/ничья).
        """
        pass
