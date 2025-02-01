class BaseException(Exception):
    def __init__(self, code, msg=""):
        super().__init__(f"Error {code}: {msg}")

# current max: 8
class ArgumentException(BaseException):
    def __init__(self, code: int, msg=None, wrong_argument=None, right_argument=None):
        if msg is None:
            msg: str = f"Argument Error!"
        if wrong_argument is not None:
            msg += f"\nWrong Argument: {wrong_argument}"
        if right_argument is not None:
            msg += f"\nRight Argument (Pattern): {right_argument}"
        self.wrong_argument = wrong_argument
        self.right_argument = right_argument
        self.msg = msg
        super().__init__(code, msg)
