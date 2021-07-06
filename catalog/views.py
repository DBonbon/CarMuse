from django.shortcuts import render
from . models import Painter, Painting, Category, Support
# from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

import cloudinary
from cloudinary import utils
from cloudinary.exceptions import GeneralError
from cloudinary.cache import responsive_breakpoints_cache
from cloudinary.http_client import HttpClient
from cloudinary.compat import urlparse, parse_qs


def index(request):
    context = {'latest_question_list': "latest_question_list"}

    return render(request, 'index.html', context)

#CLOUDINARY FUNCTIONS
def painting_index_sample1(request):
    # Note: All Delivery URL have to be prepared before rendering it to the template
    url_example1_format11 = "https://res.cloudinary.com/ecpdemo/image/upload/h_350,w_350,c_fill/lady.jpg"
    url_example1_format12 = "https://res.cloudinary.com/ecpdemo/image/upload/h_350,w_350,c_fill/sample.jpg"
    url_example1_format13 = "https://res.cloudinary.com/ecpdemo/image/upload/h_350,w_350,c_fill/actor.jpg"

    imageUrl1 = url_example1_format11
    imageUrl2 = url_example1_format12
    imageUrl3 = url_example1_format13

    defaults = dict(format="jpg", height=150, width=150)
    page_obj = [
        dict(
            description="description1",
            medium="medium1",
            support="support1",
            location="location1",
            title="title1",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id1",
            image={
                'url': imageUrl1
            }
        ),
        dict(
            description="description2",
            medium="medium2",
            support="support2",
            location="location2",
            title="title2",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id2",
            image={
                'url': imageUrl2
            }
        ),
        dict(
            description="description3",
            medium="medium3",
            support="support3",
            location="location3",
            title="title3",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id3",
            image={
                'url': imageUrl3
            }
        ),
    ]

    return render(request, "catalog/painting_index_sample1.html", dict(page_obj=page_obj))


def painting_index_sample2(request):
    cloudinary.config(
        cloud_name="bonbons",
        api_key="411736333884953",
        api_secret="SdLt_7Vy37CL9v4KBpxO1B3m9l0"
    )

    # Note: All Delivery URL have to be prepared using the Cloudinary SDK
    # You may need to insert the class="img-fluid img-thumbnail" into <ima ... />

    url_example1_format11 = cloudinary.CloudinaryImage("lady.jpg").image(transformation=[
        {'height': 350, 'width': 350, 'crop': "fill"},
    ])
    url_example1_format12 = cloudinary.CloudinaryImage("sample.jpg").image(transformation=[
        {'height': 350, 'width': 350, 'crop': "fill"},
    ])
    url_example1_format13 = cloudinary.CloudinaryImage("actor.jpg").image(transformation=[
        {'height': 350, 'width': 350, 'crop': "fill"},
    ])

    imageUrl1 = "<img class=\"img-fluid img-thumbnail\"" + url_example1_format11.lstrip("<img")
    imageUrl2 = "<img class=\"img-fluid img-thumbnail\"" + url_example1_format12.lstrip("<img")
    imageUrl3 = "<img class=\"img-fluid img-thumbnail\"" + url_example1_format13.lstrip("<img")

    defaults = dict(format="jpg", height=150, width=150)
    page_obj = [
        dict(
            description="description1",
            medium="medium1",
            support="support1",
            location="location1",
            title="title1",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id1",
            image={
                'url': imageUrl1
            }
        ),
        dict(
            description="description2",
            medium="medium2",
            support="support2",
            location="location2",
            title="title2",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id2",
            image={
                'url': imageUrl2
            }
        ),
        dict(
            description="description3",
            medium="medium3",
            support="support3",
            location="location3",
            title="title3",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id3",
            image={
                'url': imageUrl3
            }
        ),
    ]

    return render(request, "catalog/painting_index_sample2.html", dict(page_obj=page_obj))


def painting_index_sample3(request):
    cloudinary.config(
        cloud_name="bonbons",
        api_key="411736333884953",
        api_secret="SdLt_7Vy37CL9v4KBpxO1B3m9l0"
    )

    # Note: All Delivery URL have to be prepared using the Cloudinary SDK

    url_example1_format11 = "lady.jpg"
    url_example1_format12 = "sample.jpg"
    url_example1_format13 = "actor.jpg"

    # All Delivery URL have to be prepared using the Cloudinary SDK

    imageUrl1 = url_example1_format11
    imageUrl2 = url_example1_format12
    imageUrl3 = url_example1_format13

    defaults = dict(format="jpg", height=150, width=150)
    page_obj = [
        dict(
            description="description1",
            medium="medium1",
            support="support1",
            location="location1",
            title="title1",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id1",
            image={
                'url': imageUrl1
            }
        ),
        dict(
            description="description2",
            medium="medium2",
            support="support2",
            location="location2",
            title="title2",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id2",
            image={
                'url': imageUrl2
            }
        ),
        dict(
            description="description3",
            medium="medium3",
            support="support3",
            location="location3",
            title="title3",
            modal_width_placeholder="350px",
            modal_height_placeholder="350px",
            id="id3",
            image={
                'url': imageUrl3
            }
        ),
    ]

    return render(request, "catalog/painting_index_sample3.html", dict(page_obj=page_obj))

#END CLOUDINARY FUNCTIONS


def painting_index(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 24)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, "catalog/painting_index.html", context)

"""
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        paintings = Painting.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

        context = {
                'search': search,
                'paintings': paintings,

        }

        return render(request, "catalog/art_search.html", context)
"""


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


