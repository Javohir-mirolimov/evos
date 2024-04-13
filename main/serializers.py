from .models import *
from rest_framework import serializers


class BannerSer(serializers.ModelSerializer):
    class Meta:
        models = Banner
        fields = '__all__'


class ProductSer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = '__all__'


class TagSer(serializers.ModelSerializer):
    class Meta:
        models = Tag
        fields = '__all__'


class AdvantageSer(serializers.ModelSerializer):
    class Meta:
        models = Advantage
        fields = '__all__'


class Favorite_foodSer(serializers.ModelSerializer):
    class Meta:
        models = Favorite_food
        fields = '__all__'


class BranchSer(serializers.ModelSerializer):
    class Meta:
        models = Branch
        fields = '__all__'


class VacancySer(serializers.ModelSerializer):
    class Meta:
        models = Vacancy
        fields = '__all__'


class Send_requestSer(serializers.ModelSerializer):
    class Meta:
        models = Send_request
        fields = '__all__'


class Job_benefitSer(serializers.ModelSerializer):
    class Meta:
        models = Job_benefit
        fields = '__all__'


class CareerSer(serializers.ModelSerializer):
    class Meta:
        models = Career
        fields = '__all__'


class About_jobSer(serializers.ModelSerializer):
    class Meta:
        models = About_job
        fields = '__all__'


class NewSer(serializers.ModelSerializer):
    class Meta:
        models = New
        fields = '__all__'


class About_usSer(serializers.ModelSerializer):
    class Meta:
        models = About_us
        fields = '__all__'


class ResumeSer(serializers.ModelSerializer):
    class Meta:
        models = Resume
        fields = '__all__'

class TestimonialSer(serializers.ModelSerializer):
    class Meta:
        models = Testimonial
        fields = '__all__'


class ContactSer(serializers.ModelSerializer):
    class Meta:
        models = Contact
        fields = '__all__'


class InfoSer(serializers.ModelSerializer):
    class Meta:
        models = Info
        fields = '__all__'



