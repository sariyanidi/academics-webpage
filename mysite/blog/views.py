from django.views.generic import TemplateView
from django.db.models.query import QuerySet
from django.conf import settings
from models import Publication, Project, Code, CodeSnippet, Article, Category
from mysite.blog.models import ProjectImage, ProjectVideo

class PublicationsView(TemplateView):
    
    template_name = 'publications.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'publications'
        context['title'] = 'Publications'
        
        from django.db.models import Min,Max
        pubData = Publication.objects.all().aggregate(Min('year'),Max('year'))
        
        years = [y for y in range(pubData['year__min'],pubData['year__max']+1) if Publication.objects.filter(year__exact=y).count()>0]
        context['years'] = years
        context['pubs'] = [(y,Publication.objects.filter(year__exact=y)) for y in reversed(years)]
        return context



class ResourcesView(TemplateView):
    
    template_name = 'resources.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'resources'
        context['title'] = 'Resources'
                
        context['resources'] = [code  for code in Code.objects.all()]
        return context
    
    


class CodeSnippetsView(TemplateView):
    
    template_name = 'code_snippets.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'code_snippets'
        context['title'] = "Code Snippets"
        
        context['code_snippets'] = [snippet for snippet in CodeSnippet.objects.all()]
        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'about'
        context['title'] = 'About '
        
        return context
    
    

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'index'
        context['title'] = 'Home page'
        
        
        context['categories'] =  Category.objects.all()
        context['article'] =  Article.objects.all()[0]#.get()
        context['article2'] =  Article.objects.all()[1]#.get()
        context['projects'] = [project for project in Project.objects.all()]
        context['projects'] = context['projects'][0:2:1]
        return context
    
    
    
    

class ProjectView(TemplateView):
    
    template_name = 'project.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'projects'
        
        from django.db.models import Min,Max
        projectId=int(kwargs['id'])
        
        if projectId != 0:
            context['cproject'] = Project.objects.get(id=projectId)
            context['title'] = context['cproject'].title + " - Projects "
        return context
    

class ProjectsView(TemplateView):
    
    template_name = 'projects.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'projects'
        context['title'] = 'Projects'
        
        from django.db.models import Min,Max
        context['projects'] = (project for project in Project.objects.all())
    
        return context
    
    

class ArticleView(TemplateView):
    
    template_name = 'article.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'articles'
        context['articles'] = [article for article in Article.objects.all()]

        articleId=int(kwargs['id'])
        
        if articleId != 0:
            context['article'] = Article.objects.get(id=articleId)
            context['title'] =  context['article'].title + ' - Articles'

        return context
    

class ArticlesView(TemplateView):
    
    template_name = 'articles.html'
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page'] = 'article'
        context['title'] = 'Articles'

        catId = 0
        
        if 'id' in kwargs.keys():
            catId=int(kwargs['id'])
        
        from django.db.models import Min,Max
        context['categories'] = [c for c in Category.objects.all()]
        context['cat_id'] = catId
        
        if catId == 0:
            context['articles'] = [article for article in Article.objects.all()]
        else:
            context['articles'] = [c for c in Article.objects.filter(category_id_id__exact=catId)]
            
        return context
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
