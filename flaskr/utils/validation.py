class Validation(object):
    error_message = {}
    has_error = False

    def __init__(self, rule: dict, request) -> None:
        self.rule = rule
        self.request = request
        self.__validate()

    def __validate(self) -> None:
        for name, rules in self.rule.items():
            for rule in rules:
                if rule == 'required':
                    self.error_message[name] = self.__required(name)

                if rule == 'required:file':
                    self.error_message[name] = self.__required_file(name)

    def __required(self, name) -> str:
        error_message = '*This field is required'

        if name not in self.request.form:
            self.has_error = True
            return error_message
        elif self.request.form[name] == '':
            self.has_error = True
            return error_message
        else:
            return ''

    def __required_file(self, name) -> str:
        error_message = '*This field is required'

        is_file_uploaded = (name in self.request.files and self.request.files[name].filename != '')

        if not is_file_uploaded:
            self.has_error = True
            return error_message
        else:
            return ''
