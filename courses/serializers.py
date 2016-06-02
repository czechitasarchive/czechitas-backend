from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Course, Category, Couch
from venues.serializers import CitySerializer, CourseVenueSerializer
from django.contrib.auth.models import User
import time

class UserDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='get_user_email')
    dates = serializers.SerializerMethodField()
    states = serializers.SerializerMethodField()

    def get_dates(self, obj):
        temp = Couch.objects.get(id=obj.id).audit_log.last()
        try:
            return temp.action_date
        except:
            return "No changes"

    def get_states(self, obj):
        temp = Couch.objects.get(id=obj.id).audit_log.last()
        try:
            return temp.action_type
        except:
            return "No changes"

    class Meta:
        model = Couch
        fields = [
        'id',
         'user',
         'dates',
         'states',
		]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    states = serializers.SerializerMethodField()

    def get_states(self, obj):
        temp = Category.objects.get(id=obj.id).audit_log.first()
        try:
            if temp.active == True:
                return temp.action_type
            elif temp.active == False:
                return "D"
            else:
                pass
        except:
            return "No changes"

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'color_code',
            'states',
        )

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    course_category = CategorySerializer(many = False, read_only = True)
    course_venue = CitySerializer(many = False, read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name = 'course-detail', lookup_field = 'pk')


    class Meta:
        model = Course
        fields = (
            'id',
            'url',
            'title',
            'course_start_date',
            'course_end_date',
            'course_description',
            'course_venue',
            'updated_date',
            'course_category',


        )

class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    course_category = CategorySerializer(many = False, read_only = True)
    course_venue = CourseVenueSerializer(many = False, read_only = True)
    couch = UserDetailSerializer(many = False, read_only = True)
    dates = serializers.SerializerMethodField()
    states = serializers.SerializerMethodField()

    def get_dates(self, obj):
        temp = Course.objects.get(id=obj.id).audit_log.last()
        try:
            return temp.action_date
        except:
            return "No changes"

    def get_states(self, obj):
        temp = Course.objects.get(id=obj.id).audit_log.last()
        try:
            return temp.action_type
        except:
            return "No changes"

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'course_description',
            'course_start_date',
            'course_end_date',
            'course_price',
            'notes',
            'registration_form_link',
            'course_venue',
            'course_category',
            'couch',
            'dates',
            'states',
        )
