from django import forms


class TableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas', required=True)
    columnas = forms.IntegerField(label='Columnas', required=True)
    minas = forms.IntegerField(label='Minas', required=True)


