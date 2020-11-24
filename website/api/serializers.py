from rest_framework import serializers
from projects.models import Event, Project


class ProjectSerializer(serializers.ModelSerializer):
    activity = serializers.StringRelatedField()
    supervisor = serializers.StringRelatedField()
    events = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='events-detail'
    )

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'place',
            'description',
            'activity',
            'supervisor',
            'events',
        )


class NestedProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='projects-detail',
    )

    class Meta:
        model = Project
        fields = ['title', 'url']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    project = NestedProjectSerializer(many=False, read_only=True)
    status = serializers.CharField(source='get_status_display')
    web_url = serializers.SerializerMethodField()

    def get_web_url(self, obj):
        obj_url = obj.get_absolute_url()
        return self.context["request"].build_absolute_uri(obj_url)

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'project',
            'audiences',
            'status',
            'web_url',
        )
