from django import forms


class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    dateExpense = forms.DateField()
    category = forms.CharField()


class FilterForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()
    # categories = forms.CheckboxSelectMultiple()
