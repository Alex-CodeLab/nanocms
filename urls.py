from django.conf.urls import url, include
from nanocms.views import page,  nanoadmin, NanoEdit
from django.contrib.auth.decorators import login_required

urlpatterns =[
    url(r'admin$', nanoadmin),
    url(r'admin/(?P<pk>[0-9]+)$', login_required(NanoEdit.as_view()), name='nanoedit'),
    url(r'(?P<permalink>.+)$', page),
]
