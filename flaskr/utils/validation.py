class Validation(object):
    error_message = {}
    has_error = False

    def __init__(self, rule: dict, form: dict) -> None:
        self.rule = rule
        self.form = form
        self.__validate()

    def __validate(self) -> None:
        for name, value in self.form.items():
            for rule in self.rule[name]:
                if rule == 'required':
                    self.error_message[name] = self.__required(value)

    def __required(self, value) -> str | None:
        if value == '':
            self.has_error = True
            return '*This field is required'
        else:
            return None
