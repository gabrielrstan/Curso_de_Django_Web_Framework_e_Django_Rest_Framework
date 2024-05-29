from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, TagSerializer
from recipes.views.site import PER_PAGE
from tag.models import Tag


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = PER_PAGE


class RecipeAPiv2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()  # type:ignore
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    def get_queryset(self):
        qs = super().get_queryset()  # type:ignore
        category_id = self.request.query_params.get('category_id', '')
        if category_id != '' and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)
        return qs

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        recipe = self.get_queryset().filter(pk=pk).first()  # type:ignore
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )


@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)
