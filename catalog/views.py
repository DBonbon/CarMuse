from django.shortcuts import render
from . models import Painter, Painting, Category, Support
# from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic
from django.views.generic import ListView


def index(request):
    num_ouevres = Painting.objects.all().count
    # num_painters = Painter.objects.all().count
    num_categories = Category.objects.all().count
    num_supports = Support.objects.all().count

    num_authors = Painter.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_ouevres': num_ouevres,
        'num_categories': num_categories,
        # 'num_painters': num_painters,
        'num_supports': num_supports,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context)


class PaintingListView(generic.ListView):
    model = Painting
    context_object_name = 'painting_list'   # your own name for the list as a template variable
    template_name = 'catalog/painting_list.html'  # Specify your own template name/location



class PaintingDetailView(generic.DetailView):
    model = Painting
    context_object_name = 'painting'
    template_name = 'catalog/painting_detail.html'

class SearchResultsView(ListView):
    model = Painting
    template_name = 'catalog/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Painting.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list


def painter_index(request):
    painters = Painter.objects.all()
    context = {'painters': painters}
    return render(request, "catalog/painter_index.html", context)


def painter_detail(request, pk):
    painter = Painter.objects.get(pk=pk).count
    context = {"painter": painter}
    return render(request, "catalog/painter_detail.html", context)


