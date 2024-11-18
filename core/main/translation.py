from .models import Qaxaq, Mayla, Poxoc
from modeltranslation.translator import register, TranslationOptions

@register(Qaxaq)
class QaxaqTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Mayla)
class MaylaTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Poxoc)
class PoxocTranslationOptions(TranslationOptions):
    fields = ('name',)