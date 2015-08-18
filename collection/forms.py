from django.forms import ModelForm

from collection.models import PrivateLabel

class PrivateLabelForm(ModelForm):
	class Meta:
		model = PrivateLabel
		fields = ('name', 'description',)
