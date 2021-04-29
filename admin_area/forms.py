from django import forms

from bag.models import DeliveryOptions, DiscountCode


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
