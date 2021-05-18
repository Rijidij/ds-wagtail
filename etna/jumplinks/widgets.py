from django import forms


class JumplinkWidget(forms.MultiWidget):
    label = forms.CharField()
    anchor = forms.CharField()

    template_name = "jumplink/forms/widgets/jumplink_widget.html"
