from django.contrib import admin
from testapp.models import Article

# Register your models here.
# admin.site.register(Language)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # pass
    # fields = ['title']
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     # form.base_fields["title"].label = "Article title ("+obj.title['en']+"):" 
    #     form.base_fields["title"].label = "Article title ("+obj.title['fr']+"):" 
    #     print(form.base_fields['title'].label)
    #     return form
    exclude = ('checking_name', )

admin.site.site_header = "Wodasoft Tasks"