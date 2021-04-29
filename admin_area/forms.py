from django import forms

from admin_area.widgets import CustomClearableFileInputImages
from bag.models import DeliveryOptions, DiscountCode
from products.models import (
    Product,
    ProductStock
)


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryOptions
        fields = "option", "description", "price", "active"

    option = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'active':
                field.widget.attrs[
                    "class"
                ] = "border-0 rounded-0 w-100 h-100 no-active bg-transparent"
            else:
                field.widget.attrs[
                    "class"
                ] = "border-0 rounded-0 w-100 h-100 no-active"


DeliveryFormset = forms.modelformset_factory(
    DeliveryOptions,
    form=DeliveryForm,
)


class DiscountForm(forms.ModelForm):
    class Meta:
        model = DiscountCode
        fields = "code", "discount", "active", "expiry", "quantity"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'active':
                field.widget.attrs[
                    "class"
                ] = "border-0 rounded-0 w-100 h-100 no-active bg-transparent"
            else:
                field.widget.attrs[
                    "class"
                ] = "border-0 rounded-0 w-100 h-100 no-active"


DiscountFormset = forms.modelformset_factory(
    DiscountCode,
    form=DiscountForm,
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = 'name', 'description', 'price', 'image', 'category', 'active'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInputImages)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductStockForm(forms.ModelForm):

    class Meta:
        model = ProductStock
        fields = 'available_stock',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
