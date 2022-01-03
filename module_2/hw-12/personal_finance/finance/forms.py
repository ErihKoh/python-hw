from django import forms


class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()


class FilterForm(forms.Form):
    start = forms.CharField()
    end = forms.DateField()
