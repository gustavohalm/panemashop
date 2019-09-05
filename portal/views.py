from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic import ( TemplateView, ListView, DetailView,CreateView, UpdateView)
from . import models
from . import forms
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
import algoliasearch_django as algoliasearch

# Create your views here.


def home(request):
    categories = models.Category.objects.filter(parent__isnull=True).order_by('name')
    leasts = models.Product.objects.all()[:10]

    context = {
        'categories': categories,
        'leasts': leasts,
    }

    return render(request, 'portal/home.html', context )


class MyProducts(ListView):
    template_name = 'portal/my_products.html'
    model = models.Product

    def get_queryset(self):
        queryset = models.Product.objects.filter(user= self.request.user)
        return queryset

class ProductDetail(DetailView):
    model = models.Product
    template_name = 'portal/product_detail.html'


class ProductCreate(CreateView):
    form_class = forms.Product
    template_name = 'portal/product_create.html'
    model = models.Product

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('my_products'))

class ProductUpdate(UpdateView):
    model = models.Product
    form_class = forms.Product
    template_name = 'portal/product_update.html'
     
    def get_success_url(self):
        return HttpResponseRedirect(reverse('my_products'))

def product_question(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    if request.method == 'POST':
        form = forms.ProductQuestion(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.product = product
            question.save()

    url = '/produto/' + str(slug)

    return redirect(url)

def product_answer(request, slug, pk):
    question = get_object_or_404(models.ProductQuestion, id=pk)
    if request.method == 'POST':
        print( 'id: ' + str(pk ))
        form = forms.ProductAnswer( request.POST )
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
    url = '/produto/' + str(slug)

    return redirect(url)


def search(request):
    categories = models.Category.objects.filter(parent__isnull=True).order_by('name')

    qs = request.GET.get('q', '')
    str_category = request.GET.get('categoria', '')
    page = request.GET.get('page', 0)
    results = None
    if qs:
        params = {'hitsPerPage':1, 'page': page}
        results = algoliasearch.raw_search(models.Product, qs, params)

    if str_category:
        category = get_object_or_404(models.Category, slug=str_category)
        result = models.Product.objects.filter( category=category)
        paginator = Paginator(result, 1)
        page = request.GET.get('page', 1)

        try:
            results = paginator.page(page)

        except EmptyPage:
            results = paginator.page(paginator.num_pages)

    try:
        totalpages = range(results['nbPages'])
    except:
        totalpages = range(1)


    context = {
        'categories': categories,
        'results': results,
        'q': qs,
        'page': page,
        'previous_page':int(page)-1,
        'next_page': int(page)+1,
        'nPages': totalpages,
    }
    return render(request, 'portal/search.html', context)