import django_filters

from .models import Event, Project
from core.models import Type

import operator
from django.db.models import Q
from functools import reduce


def selected_projects(request):
    """
    Limit project choice
    """

    if request is None:
        return Project.objects.none()

    # Filter out projects that do not include any events
    projects = Project.objects.filter(events__isnull=False).distinct()

    # Follower user group: show all projects that include published events
    if 'follower' in request.path:
        return projects.filter(events__status='p')

    # Coordinator and Custom user group: show all projects from user organization
    # that include published events
    elif 'all' in request.path:
        return projects.filter(supervisor__organization=request.user.organization) \
            .filter(events__status='p')

    # Coordinator user group: show only those supervised by user
    return projects.filter(supervisor=request.user)


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", method='filter_title')
    project = django_filters.ModelMultipleChoiceFilter(queryset=selected_projects)
    audiences = django_filters.CharFilter(field_name='audiences', method='filter_audiences')
    type = django_filters.ModelMultipleChoiceFilter(queryset=Type.objects.all())
    # start_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Event
        fields = (
            'title',
            'project',
            'audiences',
            'type',
            'status',
        )

    def filter_title(self, queryset, name, title):
        return queryset.filter(reduce(operator.or_, (Q(title__icontains=x.strip()) for x in title.split(','))))

    def filter_audiences(self, queryset, name, audiences):
        return queryset.filter(reduce(operator.or_, (Q(audiences__icontains=x.strip()) for x in audiences.split(','))))


class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", method='filter_title')

    class Meta:
        model = Project
        fields = (
            'title',
        )

    def filter_title(self, queryset, name, title):
        return queryset.filter(reduce(operator.or_, (Q(title__icontains=x.strip()) for x in title.split(','))))
