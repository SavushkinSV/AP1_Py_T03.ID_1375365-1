"""Модель игрового поля для Крестики-Нолики."""

from typing import List


class Board:
    """Игровое поле 3x3.
    
    Представляет собой матрицу, где:
    - 0: пустая клетка
    - 1: крестик (X)
    - 2: нолик (O)
    """
    
    def __init__(self, grid: List[List[int]] = None):
        """Инициализация доски.
        
        Args:
            grid: Двумерный массив 3x3. Если None, создается пустая доска.
        """
        if grid is None:
            self._grid = [[0 for _ in range(3)] for _ in range(3)]
        else:
            if len(grid) != 3 or any(len(row) != 3 for row in grid):
                raise ValueError("Grid must be 3x3")
            self._grid = [row[:] for row in grid]
    
    @property
    def grid(self) -> List[List[int]]:
        """Возвращает копию игровой сетки."""
        return [row[:] for row in self._grid]
    
    def get_cell(self, row: int, col: int) -> int:
        """Возвращает значение клетки.
        
        Args:
            row: Номер строки (0-2).
            col: Номер столбца (0-2).
            
        Returns:
            0 (пусто), 1 (X) или 2 (O).
        """
        return self._grid[row][col]
    
    def set_cell(self, row: int, col: int, value: int) -> None:
        """Устанавливает значение клетки.
        
        Args:
            row: Номер строки (0-2).
            col: Номер столбца (0-2).
            value: 0 (пусто), 1 (X) или 2 (O).
        """
        self._grid[row][col] = value
    
    def is_empty(self, row: int, col: int) -> bool:
        """Проверяет, пуста ли клетка.
        
        Args:
            row: Номер строки (0-2).
            col: Номер столбца (0-2).
            
        Returns:
            True, если клетка пустая.
        """
        return self._grid[row][col] == 0
    
    def copy(self) -> 'Board':
        """Создает копию доски."""
        return Board(self._grid)
    
    def __eq__(self, other: object) -> bool:
        """Сравнение досок."""
        if not isinstance(other, Board):
            return False
        return self._grid == other._grid
    
    def __repr__(self) -> str:
        return f"Board(grid={self._grid})"
