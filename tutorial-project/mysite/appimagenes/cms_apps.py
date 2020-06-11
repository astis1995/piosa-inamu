from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
#from django.conf.urls import url
#from polls.views import PollListView, PollDetailView

@apphook_pool.register  # register the application
class AppsimagenesApphook(CMSApp):
    app_name = "appimagenes"
    name = _("Carrusel Dinamico")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["appimagenes.urls"]
