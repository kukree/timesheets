from django import forms
from .models import Task, Client
from projects.models import Project


class CreateTask(forms.ModelForm):
    def __init__(self, editable_object=None, *args, **kwargs):
        super(CreateTask, self).__init__(*args, **kwargs)
        use_required_attribute = True
        self.fields['name'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            max_length=150,
            label='Name',
            required=True,
            initial=editable_object.name if editable_object else None
        )

    class Meta:
        model = Task
        fields = ('name',)


class CreateClient(forms.ModelForm):
    def __init__(self, editable_object=None, *args, **kwargs):
        super(CreateClient, self).__init__(*args, **kwargs)
        use_required_attribute = True
        self.fields['name'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            max_length=150,
            label='Name',
            required=True,
            initial=editable_object.name if editable_object else None
        )
        self.fields['email'] = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            required=False,
            label='Email',
            initial=editable_object.email if editable_object else None
        )
        self.fields['address'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            max_length=150,
            required=False,
            label='Address',
            initial=editable_object.address if editable_object else None
        )

    class Meta:
        model = Client
        fields = ('name', 'email', 'address',)
