class Lox(object):
    had_error = False

    @classmethod
    def run_file(cls, file_name: str):
        print(f"reading file {file_name}")
        with open(file_name, "r") as fp:
            cls.run(fp.read())
            if cls.had_error:
                exit(65)

    @classmethod
    def run_prompt(cls):
        while True:
            line = input(">> ")
            if line is None:
                break
            cls.run(line)
            cls.had_error = False

    @classmethod
    def run(cls, source: str):
        from lox_python.scanner import Scanner

        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for t in tokens:
            print(t)

    @classmethod
    def error(cls, line: int, msg: str):
        cls.report(line, "", msg)

    @classmethod
    def report(cls, line: int, where: str, msg: str):
        print(f"[line {line}] Error{where}: {msg}")
        cls.had_error = True
