from baselinecore.plugin.forms import BasePluginSettingsForm
from django import forms

class AddthisSettingsForm(BasePluginSettingsForm):

    plugin = 'bl_plugin_addthis'

    profile_id = forms.CharField(help_text="Enter the AddThis profile ID you want to use, i.e.:  ra-1234567890")