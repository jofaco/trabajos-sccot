from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# USERS
from django.views.generic import ListView, UpdateView, DeleteView
from usuario.forms import UserForm
from django.shortcuts import  redirect, render
from usuario.mixins import IsSuperuserMixin
from django.contrib.auth.models import User
from django.contrib import messages
from pathlib import Path
from usuario.mixins import IsSuperuserMixin
from django.db import connections
#IA
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
import os
from django.http import HttpResponse
#from dotenv import load_dotenv
#env_path = Path(__file__).resolve().parent.parent / '.env'
#load_dotenv(dotenv_path=env_path)

#Configuración de la base de datos
secoundKay = '9DrUOBaKjRfeLX4XTJcG'
os.environ["OPENAI_API_KEY"] = 'sk-proj-blfbEtSvbbLI4famkcrWT3BlbkFJ' + secoundKay
#db = SQLDatabase.from_uri("mysql+mysqlconnector://root:vcc2022*WP@localhost:3306/trabajos")
#Configuración del modelo
db_uri = "mysql+mysqlconnector://root:vcc2022*WP@localhost:3306/trabajos"
#db_uri = "mysql+mysqlconnector://root2:123@localhost:3306/trabajostestmarlong1"

# Crear el objeto SQLDatabase usando la URI
db = SQLDatabase.from_uri(db_uri)
#llm = ChatOpenAI(temperature=0, model_name='gpt-4o-mini')
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
#cadena = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=False)
cadena = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)

formato = """
Data una pregunta del usuario:
1. Crea una consulta SQL para MySQL.
2. Elimina las marcas de código y asegúrate de que la consulta esté correctamente formateada.
3. Revisa los resultados.
4. Devuelve el dato en HTML organizado usando estilos Bootstrap.
5. Si vas a mostrar datos sobre trabajos, siempre incluye un link con la siguiente dirección: https://trabajos.sccot.org/Detalle_Trabajo/idTrabajo, donde `idTrabajo` lo vas a reemplazar por el id del trabajo.
6. Si vas a mostrar datos sobre autores, siempre incluye un link con la siguiente dirección: https://trabajos.sccot.org/Autor/detalleAutor/idAutor, donde `idAutor` lo vas a remplazar por el id del autor.
7. Siempre que se hable de trabajos o autores incluye link con los parametros dichos en el punto 5 y 6.
#{question}
"""

#7. si la consulta involucra datos de usuarios como (contraseña, username, password, is_superuser) retorna un mensaje indicando que no se pueden mostrar datos de usuarios
# FALTA COLOCAR HEADER Y MIRAR SI PODEMOS PROPORCIONAR LINK DE LOS TRABAJOS
class PreguntarChatGPT(LoginRequiredMixin, IsSuperuserMixin, View):
    template_name = 'preguntarChatGPT.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        resultado = ""
        cargando = True
        pregunta = request.POST.get('pregunta')
        max_intentos = 1  # Número máximo de intentos

        if pregunta:
            consulta_sql = formato.format(question=pregunta)
            intentos = 0
            
            while intentos < max_intentos:
                try:
                    # Ejecuta la consulta
                    resultado = cadena.run(consulta_sql)
                    print(f"Resultado: {resultado}")

                    # Guardar la pregunta y la respuesta en la sesión
                    preguntas = request.session.get('preguntas', [])
                    respuestas = request.session.get('respuestas', [])
                    
                    # Limitar el historial a las últimas 10 preguntas
                    if len(preguntas) >= 10:
                        preguntas.pop(0)
                        respuestas.pop(0)
                    
                    preguntas.append(pregunta)
                    respuestas.append(resultado)
                    
                    request.session['preguntas'] = preguntas
                    request.session['respuestas'] = respuestas
                    
                    break  # Salir del bucle si la consulta fue exitosa

                except Exception as e:

                    intentos += 1
                    if intentos >= max_intentos:
                        resultado = "<div class='d-flex justify-content-center'><p class='m-3 h5 text-center'>Lo sentimos, no fue posible responder la pregunta.<br/> intenta hacer tu pregunta mas especifica</p></div>"
                        break  # Salir del bucle si se alcanzó el máximo de intentos

                finally:
                    cargando = False  # Actualiza el estado después de procesar la consulta

        context = self.get_context_data(resultado=resultado, cargando=cargando)
        return render(request, self.template_name, context)


    def get_context_data(self, **kwargs):
        preguntas = self.request.session.get('preguntas', [])
        respuestas = self.request.session.get('respuestas', [])
        
        # Emparejar preguntas con respuestas en una lista de tuplas
        historial = zip(preguntas[::-1], respuestas[::-1])
        
        # Crear el contexto con la lista de historial
        context = {
            'historial': historial,
        }
        
        # Actualizar el contexto con cualquier otro dato
        context.update(kwargs)
        return context


def hola_mundo(request):
    return HttpResponse('<h1>Hola Mundo</h1>')
