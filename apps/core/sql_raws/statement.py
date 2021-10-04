class SQLStatement:
    def __init__(self, model, *fields, other=None):
        self.model = model
        self.fields = fields
        self.other = other

    @property
    def raw_query(self):
        return f"SELECT * from {self.model} {self.other}"

    def __repr__(self):
        return self.model


class SelectStatement(SQLStatement):
    @property
    def raw_query(self):
        fields = ",".join(self.fields)
        return f"SELECT {fields} from {self.model} {self.other}"
