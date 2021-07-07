from django.shortcuts import render
from . models import Painter, Painting, Category, Support
from django.core.paginator import Paginator
from django.db.models import Q


def painting_index(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 24)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, "catalog/painting_index.html", context)


def art_search(request):
        if request.method=="GET":
            query=request.GET.get('q')
            paintings=Painting.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        context = {
            'query': query,
            'paintings': paintings,
        }

        return render(request, "catalog/art_search.html", context)


def painting_detail(request, pk):
    painting = Painting.objects.get(pk=pk).count
    context = {"painting": painting}
    return render(request, "catalog/painting_detail.html", context)

