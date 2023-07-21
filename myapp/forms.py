from django import forms
from myapp.models import Customers, Books, UploadBookXLS


class CustomerForm (forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['cust_id', 'cust_name']


class UploadMasterBookForm (forms.ModelForm):
    class Meta:
        model = UploadBookXLS
        fields = ['files']


class BookForm (forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        ['book_id', 'title', 'category', 'num_page', 'book_audience', 'part_series', 'order_of_book',
         'version_number', 'price', 'description', 'cover', 'is_favourite', 'is_blocked', 'author', 'publisher',
         'isbn', 'language'
         ]

        widgets = {
            'book_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'book id'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'book title'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'num_page': forms.NumberInput(attrs={'class': 'form-control'}),
            'book_audience': forms.Select(attrs={'class': 'form-control'}),
            'part_series': forms.Select(attrs={'class': 'form-control'}),
            'order_of_book': forms.NumberInput(attrs={'class': 'form-control'}),
            'version_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Author'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Publisher'}),
            'isbn': forms.NumberInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
        }
