from django import forms


from .models import ExpenseCategory


class GetStatementForm(forms.Form):
    account_category = forms.ModelChoiceField(
        queryset=ExpenseCategory.objects.all(),
        empty_label=None,
        label="Account Category",
    )
    start_date = forms.DateField(label="Start Date")
    end_date = forms.DateField(label="End Date")
