from wagtail.admin.edit_handlers import FieldPanel

from .widgets import JumplinkWidget


class JumplinkPanel(FieldPanel):
    def __init__(self, field_name, *args, **kwargs):
        self.label = kwargs.pop('label', "")
        self.anchor = kwargs.pop('anchor', "")
        super().__init__(field_name, *args, **kwargs)

    def widget_overrides(self):
        self.model._meta.get_field(self.field_name)

        return {self.field_name: JumplinkWidget()}
