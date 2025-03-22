from lox_python.token_type import TokenType
from lox_python.token import Token


def test_token():
    token = Token(TokenType.LEFT_PAREN, "(")
    assert(str(token)=="LEFT_PAREN ( ")
