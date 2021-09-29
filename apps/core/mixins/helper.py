class BaseErrorMessage:
    message = ""
    code = ""


class MissingNumberMessage(BaseErrorMessage):
    message = "The password must contain at least 1 digit, 0-9."
    code = "password_no_number"


class MissingUpperMessage(BaseErrorMessage):
    message = "The password must contain at least 1 uppercase letter, A-Z."
    code = "password_no_upper"


class MissingLowerMessage(BaseErrorMessage):
    message = "The password must contain at least 1 lowercase letter, a-z."
    code = "password_no_lower"


class MissingSymbolMessage(BaseErrorMessage):
    message = (
        r"The password must contain at least 1 symbol: ()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
    )
    code = "password_no_symbol"
