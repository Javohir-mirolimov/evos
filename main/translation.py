from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description' )

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',  'description' , 'retsept' , 'tag')

@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title',  'description' , )

@register(Favorite_food)
class Favorite_foodTranslationOptions(TranslationOptions):
    fields = (  'description'  )

@register(Branch)
class BranchTranslationOptions(TranslationOptions):
    fields = (  'name' , 'adress' )


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = (  'title' , 'desciption', 'text' )

@register(Job_benefit)
class Job_benefittTranslationOptions(TranslationOptions):
    fields = (  'title' ,  'text' )

@register(Career)
class CareertTranslationOptions(TranslationOptions):
    fields = (  'bio',)

@register(About_job)
class About_jobTranslationOptions(TranslationOptions):
    fields = (  'title', 'text')

@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = (  'title', 'text')


@register(About_us)
class About_usTranslationOptions(TranslationOptions):
    fields = (  'title', 'text', 'desciption')


@register(Resume)
class ResumeTranslationOptions(TranslationOptions):
    fields = (  'title', 'text')