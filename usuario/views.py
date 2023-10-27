from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import  redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, DeleteView
from django.core.paginator import Paginator

#
from django.contrib.auth.models import User
from usuario.forms import UserForm

from usuario.mixins import IsSuperuserMixin


class UserListView(LoginRequiredMixin,IsSuperuserMixin, ListView):
    ''' Clase ListView para listar los usuarios. 

    **Context** 
       
        :model:  Una instancia del modelo Usuario .
        
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al template para listar usuarios.
    
    **Template:**

        :template_name: Template en donde se listarán a los usuarios.
            
    '''
    model = User
    template_name = 'list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['list_url'] = reverse_lazy('user:user_list')
        usuariosAll = User.objects.all()
        page = self.request.GET.get('page',1)
        pag = Paginator(usuariosAll,15)
        usuarios = pag.get_page(page)
        context['usuarios'] = usuarios
        return context

class UserUpdate(LoginRequiredMixin,IsSuperuserMixin,UpdateView):
    ''' Clase UpdateView para actualizar los usuarios. 

    **Context** 
       
        :model:  Una instancia del modelo Usuario .
        :form_class:  Formulario para la edición de usuarios creado en forms.py de la app usuario.
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de editar usuarios.
        
        :``post(self, request, *args, **kwargs)``: 
        
            Recibe los datos enviados desde el formulario y realiza la validación correspondiente para realizar el update.
    
    **Template:**

        :template_name: Formulario para la edición de un usuario.
            
    '''
    model = User
    form_class = UserForm
    template_name = 'user_editModal.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            pwd = form.cleaned_data['password']
            u = form.save(commit=False)
            user = User.objects.get(pk=u.pk)
            if user.is_superuser:
                messages.warning(request, 'El usuario es administrador, no se puede editar!')
                return redirect('user:user_list')
            else:
                if user.password != pwd:
                    u.set_password(pwd)
            u.save()
            messages.success(request, 'El usuario ha sido actualizado!')
            return redirect('user:user_list')
                
        else:
            messages.error(request, 'Error al actualizar al usuario!')
            return redirect('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Usuario'
        context['Usuarios'] = User.objects.all()        
        return context

class UserDeleteView(LoginRequiredMixin, IsSuperuserMixin, DeleteView):
    ''' Clase DeleteView para 'eliminar' usuarios. 
    :Nota: Un usuario no es eliminado, solo se desactiva.

    **Context** 
       
        :model:  Una instancia del modelo Usuario .
        
    **Methods**
        
        :``get_context_data(self, **kwargs)``: 
        
            Envio del context al formulario de eliminación usuarios.

        :``post(self, request, *args, **kwargs)``: 
        
            Recibe los datos enviados desde el formulario y realiza la validación correspondiente para realizar el update(delete).
    
    **Template:**

        :template_name: Formulario para la eliminación de un usuario.
            
    '''
    model = User
    template_name = 'user_deleteModal.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,pk, *args, **kwargs):        
        object = User.objects.get(id=pk)
        if object.is_superuser:
            messages.warning(request, 'El usuario es administrador, no se puede eliminar!')
            return redirect('user:user_list')
        else:
            object.is_active = False
            object.save()
        messages.success(request, 'El usuario ha sido desactivado!')
        return redirect('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Usuario'
        context['entity'] = 'Usuarios'
        return context
