from lox_python.token_type import TokenType


class Token:
    def __init__(self, type: TokenType, lexeme: str, literal=None, line=None) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return f"{self.type} {self.lexeme} {self.literal if self.literal else ''}"

    def __repr__(self) -> str:
        return f"{self.type} {self.lexeme} {self.literal if self.literal else ''}"
