from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, ListView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from hw28.settings import TOTAL_ON_PAGE
from .models import Ad
from .permissions import IsOwner, IsAdminOrModerator
from .serializers import AdRetrieveSerializer, AdUpdateSerializer, AdDestroySerializer, AdCreateSerializer, \
    AdListSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.order_by('-price')
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        cat = request.GET.get('cat', None)
        if cat:
            self.queryset = self.queryset.filter(category=cat)

        text = request.GET.get('text', None)
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location', None)
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from and price_to:
            price_q = Q(price__gte=price_from) & Q(price__lte=price_to)
            self.queryset = self.queryset.filter(price_q)

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdRetrieveSerializer
    permission_classes = [IsAuthenticated, ]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminOrModerator | IsOwner, ]


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ['name', 'image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author.id,
            'author': self.object.name,
            'price': self.object.price,
            'desc': self.object.desc,
            'is_published': self.object.is_published,
            'category_id': self.object.category.id,
            'image': self.object.image.name
        })


class AdDestroyView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [IsAuthenticated, IsAdminOrModerator | IsOwner, ]
