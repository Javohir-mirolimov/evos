from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from main.serializers import *
from main.models import *

"""//////////<<<< Banner model CRUD start >>>>////////////////"""

#   get all
class GetAllBanner_view(ListAPIView):
    queryset = Banner.objects.all().order_by('-id')
    serializer_class = BannerSer



#   create
class CreateBanner_view(CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSer


#   update
class UpdateBanner_view(UpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSer


#   delete
class DeleteBanner_view(DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSer


"""////////// Banner model CRUD end ////////////////"""


"""//////////<<<< Product model CRUD start >>>>////////////////"""

#   get all
class GetAllProduct_view(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSer


#   create
class CreateProduct_view(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSer


#   update
class Updateprodoct_view(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSer


#   delete
class DeleteProduct_view(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSer


"""////////// Product model CRUD end ////////////////"""


"""//////////<<<< Tag model CRUD start >>>>////////////////"""


#   get all
class GetAllTag_view(ListAPIView):
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSer


#   create
class CreateTag_view(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSer


#   update
class UpdateTag_view(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSer


#   delete
class DeleteTag_view(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSer


"""////////// Tag model CRUD end ////////////////"""


"""//////////<<<< Advantage model CRUD start >>>>////////////////"""

#   get all
class GetAllAdventage_view(ListAPIView):
    queryset = Advantage.objects.all().order_by('-id')
    serializer_class = AdvantageSer


#   create
class CreateAdventage_view(CreateAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSer


#   update
class UpdateAdventage_view(UpdateAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSer


#   delete
class DeleteAdventage_view(DestroyAPIView):
    queryset = Advantage.objects.all()
    serializer_view = AdvantageSer


"""////////// Advantage model CRUD end ////////////////"""


"""//////////<<<< Favorite_food model CRUD start >>>>////////////////"""

#   get all
class GetAllFavorite_food_view(ListAPIView):
    queryset = Favorite_food.objects.all().order_by('-id')
    serializer_class = Favorite_foodSer


#   create
class CreateFavorite_food_view(CreateAPIView):
    queryset = Favorite_food.objects.all()
    serializer_class = Favorite_foodSer


#   update
class UpdateFavorite_food_view(UpdateAPIView):
    queryset = Favorite_food.objects.all()
    serializer_class = Favorite_foodSer


#delete
class DeleteFavorite_foot_view(DestroyAPIView):
    queryset = Favorite_food.objects.all()
    serializer_class = Favorite_foodSer


"""////////// Favorite_food model CRUD end ////////////////"""


"""//////////<<<< Branch model CRUD start >>>>////////////////"""

#   get all
class GetAllBranch_view(ListAPIView):
    queryset = Branch.objects.all().order_by('-id')
    serializer_class = BranchSer


#   create
class CreateBranch_view(CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSer


#   update
class UpdateBranch_view(UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSer


# delete
class DeleteBranch_view(DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSer



"""////////// Branch model CRUD end ////////////////"""


"""//////////<<<< Vacancy model CRUD start >>>>////////////////"""

#   get all
class GetAllVacancy_view(ListAPIView):
    queryset = Vacancy.objects.all().order_by('-id')
    serializer_class = VacancySer


#   create
class CreateVacancy_view(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySer


#   update
class UpdateVacancy_view(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySer


#   deleted
class DeleteVacancy_view(DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySer


"""////////// Vacancy model CRUD end ////////////////"""


"""//////////<<<< Send_request model CRUD start >>>>////////////////"""

#   get all
class GetAllSend_request_view(ListAPIView):
    queryset = Send_request.objects.all().order_by('-id')
    serializer_class = Send_requestSer


#   create
class CreateSend_request_view(CreateAPIView):
    queryset = Send_request.objects.all()
    serializer_class = Send_requestSer


#   update
class UpdateSend_request_view(UpdateAPIView):
    queryset = Send_request.objects.all()
    serializer_class = Send_requestSer


#   delete
class DeleteSend_ruquest_view(DestroyAPIView):
    queryset = Send_request.objects.all()
    serializer_class = Send_requestSer


"""////////// Send_request model CRUD end ////////////////"""


"""//////////<<<< Send_request model CRUD start >>>>////////////////"""

#   get all
class GetAllJob_benefit_view(ListAPIView):
    queryset = Job_benefit.objects.all().order_by('-id')
    serializer_class = Job_benefitSer


#   create
class CreateJob_benefit_view(CreateAPIView):
    queryset = Job_benefit.objects.all()
    serializer_class = Job_benefitSer


#   update
class UpdateJob_benefit_view(UpdateAPIView):
    queryset = Job_benefit.objects.all()
    serializer_class = Job_benefitSer


#   delete
class DeleteJob_benefit_view(DestroyAPIView):
    queryset = Job_benefit.objects.all()
    serializer_class = Job_benefitSer


"""////////// Job_benefit model CRUD end ////////////////"""


"""//////////<<<< Career model CRUD start >>>>////////////////"""

#   get all
class GetAllCareer_view(ListAPIView):
    queryset = Career.objects.all().order_by('-id')
    serializer_class = CareerSer


#   create
class CreateCareer_view(CreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSer

#   update
class UpdateCareer_view(UpdateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSer

#   delete
class DeleteCareer_view(DestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSer


"""////////// Career model CRUD end ////////////////"""


"""//////////<<<< About_job model CRUD start >>>>////////////////"""

#   get all
class GetAllAbout_job_view(ListAPIView):
    queryset = About_job.objects.all().order_by('-id')
    serializer_class = About_jobSer


#   create
class CreateAbout_job_view(CreateAPIView):
    queryset = About_us.objects.all()
    serializer_class = About_jobSer


#   update
class UpdateAbout_job_view(UpdateAPIView):
    queryset = About_us.objects.all()
    serializer_class = About_jobSer

#   delete
class DeleteAbout_job_view(DestroyAPIView):
    queryset = About_us.objects.all()
    serializer_class = About_jobSer


"""////////// About_us model CRUD end ////////////////"""


"""//////////<<<< New model CRUD start >>>>////////////////"""

#   get all
class GetAllNew_view(ListAPIView):
    queryset = New.objects.all().order_by('-id')
    serializer_class = NewSer


# Create
class CreateNew_view(CreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSer


# Update
class UpdateNew_view(UpdateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSer

# delete
class DeleteNew_view(DestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSer


"""////////// New model CRUD end ////////////////"""


"""//////////<<<< About_us model CRUD start >>>>////////////////"""

#   get all
class GetAllAbout_us_view(ListAPIView):
    queryset = About_us.objects.all().order_by('-id')
    serializer_class = About_usSer


# Create
class CreateAbout_us_view(CreateAPIView):
    queryset = About_us.objects.all()
    serializer_class = About_usSer


#   update
class UpdateAbout_us_view(UpdateAPIView):
    queryset = About_us.objects.all().order_by('-id')
    serializer_class = About_usSer


#   delete
class DeleteAbout_us_view(DestroyAPIView):
    queryset = About_us.objects.all()
    serializer_class = About_usSer


"""////////// About_us model CRUD end ////////////////"""


"""//////////<<<< Resume model CRUD start >>>>////////////////"""

#  get all
class GetAllResume_view(ListAPIView):
    queryset = Resume.objects.all().order_by('-id')
    serializer_class = ResumeSer


# create
class CreateResume_view(CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSer


#   Update
class UpdateResume_view(UpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSer


#   Delete
class DeleteResume_view(DestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSer


"""////////// Resume model CRUD end ////////////////"""


"""//////////<<<< Testimonial model CRUD start >>>>////////////////"""

#  get all
class GetAllTestimonial_view(ListAPIView):
    queryset = Testimonial.objects.all().order_by('-id')
    serializer_class = TestimonialSer


# create
class CreateTestimonial_view(CreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSer


# update
class UpdateTestimonial_view(UpdateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSer


# update
class DeleteTestimonial_view(DestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSer


"""////////// Testimonial model CRUD end ////////////////"""


"""//////////<<<< Contact model CRUD start >>>>////////////////"""

#  get all
class GetAllContact_view(ListAPIView):
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSer


#   create
class CreateContact_view(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSer


#   update
class UpdateContact_view(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSer


#   delete
class DeleteContact_view(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSer


"""////////// Contact model CRUD end ////////////////"""


"""//////////<<<< Info model CRUD start >>>>////////////////"""

#  get all
class GetAllInfo_view(ListAPIView):
    queryset = Info.objects.all().order_by('-id')
    serializer_class = InfoSer


#   create
class CreateInfo_view(CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSer


#   create
class UpdateInfo_view(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSer


#   delete
class DeleteInfo_view(DestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSer


"""////////// Info model CRUD end ////////////////"""




