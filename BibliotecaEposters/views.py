from django.shortcuts import render
from django.views.generic.base import View
from trabajosC.models import Manuscritos
from BibliotecaEposters.vimeoAPI import cons_vim_api

# Create your views here.

# def getList(request):
#     manuscritos = Manuscritos.objects.all()

#     return render(request,'listadoEposters.html',{'manuscritos':manuscritos})
# def getListCapitulo(request,capitulo):
#     manuscritos = Manuscritos.objects.all()
#     response = cons_vim_api(846405674) 

#     return render(request,'listadoEposters.html',{'manuscritos':manuscritos,'capitulo':capitulo,'video':response})
# def post():
#     return True

# def getVideosVimeo():
#     response = cons_vim_api(846405674) 
#     return response



    #model = User
    #template_name = 'list.html'

    #@method_decorator(csrf_exempt)
    #def dispatch(self, request, *args, **kwargs):
    #    return super().dispatch(request, *args, **kwargs)

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['title'] = 'Listado de Usuarios'
        #context['list_url'] = reverse_lazy('user:user_list')
        #usuariosAll = User.objects.all()
        #page = self.request.GET.get('page',1)
        #pag = Paginator(usuariosAll,15)
        #usuarios = pag.get_page(page)
        #usuarios = User.objects.all()

        #context['usuarios'] = usuarios
        #return context
