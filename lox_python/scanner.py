from lox_python.lox import Lox
from lox_python.token import Token
from lox_python.token_type import TokenType


keywords = {
    TokenType.AND.value: TokenType.AND,
    TokenType.CLASS.value: TokenType.CLASS,
    TokenType.ELSE.value: TokenType.ELSE,
    TokenType.FALSE.value: TokenType.FALSE,
    TokenType.FOR.value: TokenType.FOR,
    TokenType.FUN.value: TokenType.FUN,
    TokenType.IF.value: TokenType.IF,
    TokenType.NIL.value: TokenType.NIL,
    TokenType.OR.value: TokenType.OR,
    TokenType.PRINT.value: TokenType.PRINT,
    TokenType.RETURN.value: TokenType.RETURN,
    TokenType.SUPER.value: TokenType.SUPER,
    TokenType.THIS.value: TokenType.THIS,
    TokenType.TRUE.value: TokenType.TRUE,
    TokenType.VAR.value: TokenType.VAR,
    TokenType.WHILE.value: TokenType.WHILE,
}


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 0

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, ""))
        return self.tokens

    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_token(self):
        c = self.advance()
        match c:
            case TokenType.LEFT_PAREN.value:
                self.add_token(TokenType.LEFT_PAREN)
            case TokenType.RIGHT_PAREN.value:
                self.add_token(TokenType.RIGHT_PAREN)
            case TokenType.LEFT_BRACE.value:
                self.add_token(TokenType.LEFT_BRACE)
            case TokenType.RIGHT_BRACE.value:
                self.add_token(TokenType.RIGHT_BRACE)
            case TokenType.COMMA.value:
                self.add_token(TokenType.COMMA)
            case TokenType.DOT.value:
                self.add_token(TokenType.DOT)
            case TokenType.MINUS.value:
                self.add_token(TokenType.MINUS)
            case TokenType.PLUS.value:
                self.add_token(TokenType.PLUS)
            case TokenType.SEMICOLON.value:
                self.add_token(TokenType.SEMICOLON)
            case TokenType.STAR.value:
                self.add_token(TokenType.STAR)
            case TokenType.BANG.value:
                self.add_token(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
            case TokenType.EQUAL.value:
                self.add_token(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL)
            case TokenType.LESS.value:
                self.add_token(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS)
            case TokenType.GREATER.value:
                self.add_token(TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER)
            case TokenType.SLASH.value:
                if self.match(TokenType.SLASH.value):
                    while self.peek() != "\n" and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case " ":
                pass
            case "\r":
                pass
            case "\t":
                pass
            case "\n":
                self.line += 1
            case '"':
                self.string()
            case _:
                if c.isdigit():
                    self.number()
                elif self.is_alpah(c):
                    self.identifier()
                else:
                    Lox.error(self.line, "Unexpected character.")

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        text = self.source[self.start : self.current]
        type = keywords.get(text)
        if type is None:
            type = TokenType.IDENTIFIER
        self.add_token(TokenType.IDENTIFIER)

    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == "." and self.peek_next().isdigit():
            self.advance()

            while self.peek().isdigit():
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start : self.current]))

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()
        if self.is_at_end():
            Lox.error(self.line, "Untermindated string.")

        # move to the closing "
        self.advance()

        # trim the surrounding quotes
        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value)

    def peek(self):
        """peeking the current"""
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def match(self, expected: str):
        if self.is_at_end:
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def advance(self):
        val = self.source[self.current]
        self.current += 1
        return val

    def add_token(self, type, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def is_alpah(self, c: str):
        return c.isalpha() or c == "_"

    def is_alpha_numeric(self, c: str):
        return self.is_alpah(c) or c.isdigit()
