from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import  redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.core.paginator import Paginator

from Autores.forms import AutoresForm

from trabajosC.models import Autores
from usuario.mixins import IsSuperuserMixin
# Create your views here.


class registrarAutor(LoginRequiredMixin,IsSuperuserMixin,CreateView):
    ''' Clase CreateView para registrar Autores. 

    **Context**

        :model: Una instancia del modelo Autores creado en la app trabajosC.
        :form_class: Formulario para la creación de autores creado en forms.py de la app Autores.

    **Methods**

        :``get(self, request, *args, **kwargs)``: 

            Metodo para redireccionar al template obteniendo el context de get_context_data.

        :``get_context_data(self, **kwargs)``: 

            Envio del context al formulario de crear autores.
    
    **Template:**

        :template_name: Formulario para la creación de un autor.
            
    '''
    model = Autores
    form_class= AutoresForm
    template_name='createAutor.html'
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'Registrar Autor'
        context['form'] = self.form_class

        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

class AutorUpdate(LoginRequiredMixin,IsSuperuserMixin,UpdateView):
    ''' Clase UpdateView para actualizar los autores. 

    **Context** 
       
        :model:  Una instancia del modelo Autores creado en la app trabajosC.
        :form_class:  Formulario para la edición de autores creado en forms.py de la app Autores.
        :success_url:  Al ser exitoso la actualización del autor redirecciona al index.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de editar autores.
    
    **Template:**

        :template_name: Formulario para la edición de un autor.
            
    '''
    model = Autores
    form_class = AutoresForm
    template_name = 'autor_editModal.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Autor'
        context['autores'] = Autores.objects.all()        
        return context

class deleteAutor(LoginRequiredMixin,IsSuperuserMixin,DeleteView):
    ''' Clase DeleteView para eliminar los autores. 

    **Context**    

        :model:  Una instancia del modelo Autores creado en la app trabajosC.
        
    **Methods**
        
        :``post(self, request,pk, *args, **kwargs)``: 

            Metodo que recibe la información del autor a eliminar y al finalizar retorna al index.
    
    **Template:**

        :template_name: Formulario para la eliminación de un autor.
            
    '''
    model = Autores
    template_name = 'autor_eliminarModal.html'

    def post(self, request,pk, *args, **kwargs):        
        object = Autores.objects.get(id=pk)
        object.delete()
        return redirect('inicio')

@login_required
def designarEvaluador(request,pk):
    """Le asigna el rol de evaluador a un autor

    **Args**
        :request (): Parametro necesario para realizar la actualización.
        :pk (number): id del autor.

    **Returns**
        :redirect: Redirecciona al index.
    """
    Autores.objects.filter(id = pk).update(role_id = 2)
    return redirect('autor_list')

@login_required
def eliminarEvaluador(request,pk):
    """Le quita el rol de evaluador a un autor

    **Args**
        :request (): Parametro necesario para realizar la actualización.
        :pk (number): id del autor.

    **Returns**
        :redirect: Redirecciona al index.
    """
    Autores.objects.filter(id = pk).update(role_id = None)
    return redirect('autor_list')

class AutoresListView(LoginRequiredMixin,IsSuperuserMixin, ListView):
    ''' Clase ListView para listar los autores. 

    **Context** 
       
        :model:  Una instancia del modelo Autor .
        
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al template para listar autores.
    
    **Template:**

        :template_name: Template en donde se listarán a los autores.
            
    '''
    model = Autores
    template_name = 'list_autores.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Autores'
        context['list_url'] = reverse_lazy('autor_list')

        #autoresAll = Autores.objects.all().defer( "especialidad","direccion")
        #page = self.request.GET.get('page',1)
        #pag = Paginator(autoresAll,10)
        #autores = pag.get_page(page)
        #if self.request.method == 'POST':
        #    dato = self.request.POST.get('autorSearch')  
        #    autores = [objeto for objeto in autoresAll
        #                    if dato.lower() in objeto.ciudad.lower()
        #                        ]

        
        autores = Autores.objects.all().defer( "especialidad","direccion")
        context['autores'] = autores
        return context
class AutorDetailView(LoginRequiredMixin, IsSuperuserMixin, ListView):
    ''' Clase ListView para listar los autores por su ID. '''

    model = Autores
    template_name = 'list_autores.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Autor'
        context['list_url'] = reverse_lazy('autor_list')

        autor_id = self.kwargs.get('id')  # Obtén el id del autor desde la URL
        if autor_id:
            try:
                autor = Autores.objects.defer("especialidad", "direccion").get(id=autor_id)
                context['autores'] = [autor]
            except Autores.DoesNotExist:
                context['autores'] = []
        else:
            context['autores'] = []

        return context

