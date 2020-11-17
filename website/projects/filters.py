import django_filters

from .models import Event, Project
# from core.models import Type

import operator
from django.db.models import Q
from functools import reduce


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", method='filter_title')
    # audiences = django_filters.CharFilter(field_name='audiences', method='filter_audiences')
    # type = django_filters.ModelChoiceFilter(queryset=Type.objects.all())

    class Meta:
        model = Event
        fields = (
            'title',
            # 'audiences',
            # 'type',
        )

    def filter_title(self, queryset, name, title):
        return queryset.filter(reduce(operator.or_, (Q(title__icontains=x.strip()) for x in title.split(','))))
    #
    # def filter_audiences(self, queryset, name, audiences):
    #     return queryset.filter(reduce(operator.or_, (Q(audiences__icontains=x.strip()) for x in audiences.split(','))))


class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", method='filter_title')

    class Meta:
        model = Project
        fields = (
            'title',
        )

    def filter_title(self, queryset, name, title):
        return queryset.filter(reduce(operator.or_, (Q(title__icontains=x.strip()) for x in title.split(','))))
