"""Реализация сервиса для управления игрой Крестики-Нолики с алгоритмом Минимакс."""

from typing import Tuple

from domain.model.board import Board
from domain.model.game import Game
from domain.service.game_service import GameService


class GameServiceImpl(GameService):
    """Реализация сервиса игры с алгоритмом Минимакс."""
    
    # Игроки
    COMPUTER = 1  # X
    PLAYER = 2    # O
    
    def get_next_move(self, game: Game) -> Board:
        """Вычисляет следующий ход компьютера алгоритмом Минимакс.
        
        Args:
            game: Текущая игра.
            
        Returns:
            Новое игровое поле с ходом компьютера.
        """
        board = game.board
        best_move = self._find_best_move(board)
        
        if best_move is None:
            return board.copy()
        
        new_board = board.copy()
        new_board.set_cell(best_move[0], best_move[1], self.COMPUTER)
        return new_board
    
    def validate_board(self, original_game: Game, updated_game: Game) -> bool:
        """Проверяет, что в игровом поле изменены только допустимые ходы.
        
        Args:
            original_game: Оригинальная игра.
            updated_game: Игра с обновленным полем (ход игрока).
            
        Returns:
            True, если валидация успешна.
        """
        original_board = original_game.board
        updated_board = updated_game.board
        
        # UUID должны совпадать
        if original_game.id != updated_game.id:
            return False
        
        changes = 0
        changed_cell = None
        
        for row in range(3):
            for col in range(3):
                original_val = original_board.get_cell(row, col)
                updated_val = updated_board.get_cell(row, col)
                
                if original_val != updated_val:
                    changes += 1
                    changed_cell = (row, col)
                    
                    # Проверка: изменена только одна клетка
                    if changes > 1:
                        return False
                    
                    # Проверка: клетка была пустой и стала ходом игрока (O = 2)
                    if original_val != 0 or updated_val != self.PLAYER:
                        return False
        
        # Должен быть ровно один ход
        return changes == 1 and changed_cell is not None
    
    def check_game_end(self, game: Game) -> bool:
        """Проверяет, закончилась ли игра.
        
        Args:
            game: Текущая игра.
            
        Returns:
            True, если игра окончена (победа/поражение/ничья).
        """
        board = game.board
        
        # Проверка на победу
        if self._check_winner(board, self.COMPUTER) or self._check_winner(board, self.PLAYER):
            return True
        
        # Проверка на ничью (нет пустых клеток)
        for row in range(3):
            for col in range(3):
                if board.is_empty(row, col):
                    return False
        
        return True
    
    def _check_winner(self, board: Board, player: int) -> bool:
        """Проверяет, выиграл ли указанный игрок.
        
        Args:
            board: Игровое поле.
            player: Игрок (1 - компьютер, 2 - игрок).
            
        Returns:
            True, если игрок выиграл.
        """
        # Проверка строк
        for row in range(3):
            if all(board.get_cell(row, col) == player for col in range(3)):
                return True
        
        # Проверка столбцов
        for col in range(3):
            if all(board.get_cell(row, col) == player for row in range(3)):
                return True
        
        # Проверка диагоналей
        if all(board.get_cell(i, i) == player for i in range(3)):
            return True
        if all(board.get_cell(i, 2 - i) == player for i in range(3)):
            return True
        
        return False
    
    def _find_best_move(self, board: Board) -> Tuple[int, int]:
        """Находит лучший ход алгоритмом Минимакс.
        
        Args:
            board: Текущее игровое поле.
            
        Returns:
            Координаты лучшего хода (row, col) или None, если ходов нет.
        """
        best_score = float('-inf')
        best_move = None
        
        for row in range(3):
            for col in range(3):
                if board.is_empty(row, col):
                    board.set_cell(row, col, self.COMPUTER)
                    score = self._minimax(board, 0, False)
                    board.set_cell(row, col, 0)
                    
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        return best_move
    
    def _minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        """Алгоритм Минимакс.
        
        Args:
            board: Текущее игровое поле.
            depth: Глубина рекурсии.
            is_maximizing: Флаг максимизации (компьютер).
            
        Returns:
            Оценка позиции.
        """
        # Базовые случаи
        if self._check_winner(board, self.COMPUTER):
            return 10 - depth
        if self._check_winner(board, self.PLAYER):
            return depth - 10
        if all(not board.is_empty(row, col) for row in range(3) for col in range(3)):
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board.is_empty(row, col):
                        board.set_cell(row, col, self.COMPUTER)
                        score = self._minimax(board, depth + 1, False)
                        board.set_cell(row, col, 0)
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board.is_empty(row, col):
                        board.set_cell(row, col, self.PLAYER)
                        score = self._minimax(board, depth + 1, True)
                        board.set_cell(row, col, 0)
                        best_score = min(score, best_score)
            return best_score
