class BasePatternMixin:
    REGEX = ""


class NumberPatternMixin(BasePatternMixin):
    REGEX = r"\d"


class UpperCasePatternMixin(BasePatternMixin):
    REGEX = r"[A-Z]"


class LowerCasePatternMixin(BasePatternMixin):
    REGEX = r"[a-z]"


class SymbolPatternMixin(BasePatternMixin):
    REGEX = r"[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]"
