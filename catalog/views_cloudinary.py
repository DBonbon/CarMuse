from django.shortcuts import render
from . models import Painter, Painting, Category, Support
# from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


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

def painting_index(request):

    # Note: the "sample.jpg" is a file that must be existing in your Cloudinary account
    # FORMAT 1
    url_example1_format1 = "https://res.cloudinary.com/demo/image/upload/c_crop,h_200,w_300/sample.jpg"

    #### OR ####

    # FORMAT 2
    url_example1_format2 = "sample.jpg"

    #### OR ####

    # FORMAT 3
    url_example1_format2 = CloudinaryImage("sample.jpg").image(transformation=[{'width': 350, 'height': 350, 'crop': "scale"}])




    # Sample code implementations (array list of images), make sure all formats used are consistent both in views.py and painting_index.html
    image1 = "You can select which format you want to implement, and it must match the format in your painting_index.html"
    image2 = "You can select which format you want to implement, and it must match the format in your painting_index.html"

    defaults = dict(format="jpg", height=150, width=150)
    samples = [
        dict(
            description="description1",
            medium="medium1",
            support="support1",
            location="location1",
            title="title1",
            id="id1",
            image={
                        'url': image1
                }
            ),
        dict(
            description="description2",
            medium="medium2",
            support="support2",
            location="location2",
            title="title2",
            id="id2",
            image={
                        'url': image2
                }
            ),
    ]

    return render(request, "catalog/painting_index.html", dict(samples=samples))
# def painting_index(request):
#     paintings = Painting.objects.all()
#     paginator = Paginator(paintings, 24)
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {'page_obj': page_obj}
#     return render(request, "catalog/painting_index.html", context)


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


def painter_index(request):
    painters = Painter.objects.all()
    context = {'painters': painters}
    return render(request, "catalog/painter_index.html", context)


def painter_detail(request, pk):
    painter = Painter.objects.get(pk=pk).count
    context = {"painter": painter}
    return render(request, "catalog/painter_detail.html", context)


