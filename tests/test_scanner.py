from lox_python.scanner import Scanner


def test_str():
    s = Scanner('"test string"')
    s.scan_tokens()


def test_dig():
    t = Scanner("12.5+1*18")
    t.scan_token()
