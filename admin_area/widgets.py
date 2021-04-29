from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInputImages(widgets.ClearableFileInput):
    clear_checkbox_label = _("Change")
    input_text = _("")
    template_name = "admin_area/custom_widget_templates/custom_clearable_file_input_images.html"
