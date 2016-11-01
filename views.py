from django.shortcuts import render
from .models import Page
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .forms import PageForm
from django.http import Http404
# Create your views here.

def page(request,permalink):
    context = {}
    context['link'] = permalink
    try:
        page = Page.objects.filter(url=permalink).first()
        if page.published:
            context['content'] = page.content
            context['title'] = page.title
            if (not request.user.is_authenticated() and page.access == 'public' ) or  request.user.is_authenticated():
                return render(request, page.template, context)
            else:
                return HttpResponseForbidden('<h1>Sorry, no access.</h1>')
        else:
            raise Http404
    except:
        raise Http404


@login_required
def nanoadmin(request):
    pages = Page.objects.all()
    return  render(request, 'list.html', locals())


class NanoEdit(UpdateView):
    model = Page
    template_name = 'nanoEdit.html'
    form_class = PageForm


class NanoNew(CreateView):
    model = Page
    template_name = 'nanoEdit.html'
    form_class = PageForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(NanoNew, self).form_valid(form)


class NanoDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('nanoadmin')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
