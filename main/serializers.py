from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class BannerSer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 2
        fields = '__all__'


class TagSer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        depth = 2
        fields = '__all__'


class AdvantageSer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class Favorite_foodSer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_food
        fields = '__all__'


class BranchSer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class VacancySer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class Send_requestSer(serializers.ModelSerializer):
    class Meta:
        model = Send_request
        fields = '__all__'


class Job_benefitSer(serializers.ModelSerializer):
    class Meta:
        model = Job_benefit
        fields = '__all__'


class CareerSer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'


class About_jobSer(serializers.ModelSerializer):
    class Meta:
        model = About_job
        fields = '__all__'


class NewSer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class About_usSer(serializers.ModelSerializer):
    class Meta:
        model = About_us
        fields = '__all__'


class ResumeSer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class TestimonialSer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class InfoSer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'



class BasketSer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        depth = 4
        fields = ('id', 'user', 'product')
