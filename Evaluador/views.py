from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView
from django.urls import  reverse_lazy
from django.views.generic.base import TemplateView
from django.db.models import Q,F, Sum
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  redirect, render
import pandas as pd
from statistics import mean

from Evaluador.forms import RSyMAForm, casosyControlesForm, cohortesForm, eccForm, plantillaSCyCTForm, pruebasDXForm
from Evaluador.models import plantillaCASOSyCONTROLES, plantillaCOHORTES, plantillaECC, plantillaPruebasDX, plantillaRSyMA, plantillaSERIECASOSyCORTETRANSVERSAL

from trabajosC.models import Autores, Manuscritos, Trabajos

# Create your views here.

class TrabajosAsignados(TemplateView):
    """Clase TemplateView para ver la información de los trabajos científicos asignados al evaluador.

    **Context**    

        ``trabajos``:  Una instancia modelo del Trabajos creado en la app trabajosC`.

    **Template:**

        :template_name: Template para ver la información de los trabajos científicos.
    """
    model = Trabajos
    template_name = "trabajos_evaluador.html"
   
    def get_context_data(self, **kwargs):
        if self.request.user.is_superuser:
            Evaluador= Autores.objects.filter(role_id=2)
            context = super().get_context_data(**kwargs)
            context['trabajos'] = Trabajos.objects.all()       
            context['manuscritos'] = Manuscritos.objects.filter(Q(tituloM__icontains= 'pdf')|Q(tituloM__icontains= 'pptx')).select_related('trabajo')
            context['plantillaECC'] = plantillaECC.objects.all().select_related('trabajo')
            context['plantillaPruebasDX'] = plantillaPruebasDX.objects.all().select_related('trabajo')
            context['plantillaRSyMA'] = plantillaRSyMA.objects.all().select_related('trabajo')
            context['plantillaSERIECASOSyCORTETRANSVERSAL'] = plantillaSERIECASOSyCORTETRANSVERSAL.objects.all().select_related('trabajo')
            context['plantillaCASOSyCONTROLES'] = plantillaCASOSyCONTROLES.objects.all().select_related('trabajo')
            context['plantillaCOHORTES'] = plantillaCOHORTES.objects.all().select_related('trabajo')

            return context
        else:
            Evaluador = Autores.objects.get(email = self.request.user.email)     
            context = super().get_context_data(**kwargs)
            context['trabajos'] = Trabajos.objects.filter(evaluador = Evaluador)       
            context['manuscritos'] = Manuscritos.objects.filter(tituloM__icontains= 'pdf').select_related('trabajo')
            context['plantillaECC'] = plantillaECC.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaPruebasDX'] = plantillaPruebasDX.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaRSyMA'] = plantillaRSyMA.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaSERIECASOSyCORTETRANSVERSAL'] = plantillaSERIECASOSyCORTETRANSVERSAL.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaCASOSyCONTROLES'] = plantillaCASOSyCONTROLES.objects.filter(user=self.request.user).select_related('trabajo')
            context['plantillaCOHORTES'] = plantillaCOHORTES.objects.filter(user=self.request.user).select_related('trabajo')
            return context

class plantilla1_evaluacion(UpdateView):

    model = plantillaECC
    form_class = eccForm
    template_name = "plantillas_evaluacion/plantilla1.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo = Trabajos.objects.get(id = self.object.trabajo_id)
            d = form.cleaned_data
            d.pop('comite_de_etica')
            d.pop('registroClinica')
            total = sum(d[x] for x in d) 
            promedio = round(total*100/(len(d)*5), 2)
            form.save()
            trabajo.calificacion= promedio
            trabajo.save()
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla2_evaluacion(UpdateView):

    model = plantillaPruebasDX
    form_class = pruebasDXForm
    template_name = "plantillas_evaluacion/plantilla2.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo = Trabajos.objects.get(id = self.object.trabajo_id)
            d = form.cleaned_data
            d.pop('comite_de_etica')
            total = sum(d[x] for x in d) 
            promedio = round(total*100/(len(d)*5), 2)
            form.save()
            trabajo.calificacion= promedio
            trabajo.save()
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla3_evaluacion(UpdateView):

    model = plantillaRSyMA
    form_class = RSyMAForm
    template_name = "plantillas_evaluacion/plantilla3.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo = Trabajos.objects.get(id = self.object.trabajo_id)
            d = form.cleaned_data
            d.pop('comite_de_etica')
            total = sum(d[x] for x in d) 
            promedio = round(total*100/(len(d)*5), 2)
            form.save()
            trabajo.calificacion= promedio
            trabajo.save()
            return redirect('misEvaluaciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla4_evaluacion(UpdateView):

    model = plantillaSERIECASOSyCORTETRANSVERSAL
    form_class = plantillaSCyCTForm
    template_name = "plantillas_evaluacion/plantilla4.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo = Trabajos.objects.get(id = self.object.trabajo_id)
            d = form.cleaned_data
            d.pop('comite_de_etica')
            total = sum(d[x] for x in d) 
            promedio = round(total*100/(len(d)*5), 2)
            form.save()
            trabajo.calificacion= promedio
            trabajo.save()
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla5_evaluacion(UpdateView):

    model = plantillaCASOSyCONTROLES
    form_class = casosyControlesForm
    template_name = "plantillas_evaluacion/plantilla5.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo = Trabajos.objects.get(id = self.object.trabajo_id)
            d = form.cleaned_data
            d.pop('comite_de_etica')
            total = sum(d[x] for x in d) 
            promedio = round(total*100/(len(d)*5), 2)
            form.save()
            trabajo.calificacion= promedio
            trabajo.save()
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context

class plantilla6_evaluacion(UpdateView):

    model = plantillaCOHORTES
    form_class = cohortesForm
    template_name = "plantillas_evaluacion/plantilla6.html"
    success_url = reverse_lazy('misEvaluaciones')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            trabajo = Trabajos.objects.get(id = self.object.trabajo_id)
            d = form.cleaned_data
            d.pop('Comite_de_etica')
            total = sum(d[x] for x in d) 
            promedio = round(total*100/(len(d)*5), 2)
            form.save()
            trabajo.calificacion= promedio
            trabajo.save()
            return redirect('misEvaluaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Realizar Evaluación'
        context['autores'] = Autores.objects.all()        
        return context