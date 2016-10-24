from django.shortcuts import render
from models import Page
from django.http import HttpResponseNotFound , HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from forms import PageForm
# Create your views here.
from django.conf import settings
import os


def page(request,permalink):
    context = {}
    permalink
    context['link'] = permalink
    try:
        page = Page.objects.filter(url=permalink)[0]

        if page.publish:
            context['content'] = page.content
            context['title'] = page.title

            if (not request.user.is_authenticated() and page.access == 'public' ) or  request.user.is_authenticated():
                return render(request, page.template, context)
            else:
                return HttpResponseForbidden('<h1>Sorry, no access.</h1>')
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')


@login_required
def nanoadmin(request):
    pages = Page.objects.all()

    return  render(request, 'list.html', locals())

class NanoEdit(UpdateView):
    model = Page
    template_name = 'nanoEdit.html'
    form_class = PageForm
