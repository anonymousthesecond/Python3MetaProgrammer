class CodeTemplate:
    def __init__(self, template):
        self.template = template
        self.values = {}

    def set_value(self, key, value):
        self.values[key] = value

    def render(self):
        rendered_template = self.template.format(**self.values)
        return rendered_template
