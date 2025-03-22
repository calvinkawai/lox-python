def test_str():
    from lox_python.scanner import Scanner

    s = Scanner('"test string"')
    s.scan_tokens()
    print(s.tokens)


def test_dig():
    from lox_python.scanner import Scanner

    t = Scanner("12.5")
    t.scan_token()
