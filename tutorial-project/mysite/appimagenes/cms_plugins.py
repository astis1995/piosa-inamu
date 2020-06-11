from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from appimagenes.models import ImagenesModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class AppimagenesPluginPublisher(CMSPluginBase):
    model = ImagenesModel  # model where plugin data are saved
    module = _("appimagenes")
    name = _("Carrusel Dinamico")  # name of the plugin in the interface
    render_template = "appimagenes/carrusel_prueba.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
