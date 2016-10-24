from django.conf.urls import url, include
from nanocms.views import page,  nanoadmin, NanoEdit, NanoNew, NanoDelete
from django.contrib.auth.decorators import login_required

urlpatterns =[
    url(r'admin$', nanoadmin, name='nanoadmin'),
    url(r'admin/(?P<pk>[0-9]+)$', login_required(NanoEdit.as_view()), name='nanoedit'),
    url(r'admin/delete/(?P<pk>[0-9]+)$', login_required(NanoDelete.as_view()), name='nanodelete'),
    url(r'admin/newpage$', login_required(NanoNew.as_view()), name='nanonew'),

    url(r'(?P<permalink>.+)$', page),
]
