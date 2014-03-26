from django.contrib import admin

from models import Category,CodeSnippet,Project,Publication,Conference,ProjectAdmin,Code,Article,ArticleAdmin


class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(CodeSnippet)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Publication)
admin.site.register(Conference)
admin.site.register(Code)
admin.site.register(Article,ArticleAdmin)
