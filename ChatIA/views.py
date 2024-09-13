from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from usuario.mixins import IsSuperuserMixin
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
import os
from dotenv import load_dotenv

load_dotenv()
# Configuración de la base de datos
db = SQLDatabase.from_uri("mysql+mysqlconnector://root:vcc2022*WP@localhost:3306/trabajos")

# Configuración del modelo
api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = api_key
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
cadena = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=False)

formato = """
Data una pregunta del usuario:
1. crea una consulta SQL para MySQL
2. Elimina las marcas de código y asegúrate de que la consulta esté correctamente formateada
3. revisa los resultados
4. devuelve el dato en html organizado usando estilos bootstrap
5. Si puedes mostrar datos sobre trabajos, autores o evaluadores
5. si la consulta involucra datos de usuarios como (contraseña, username, password, is_superuser) retorna un mensaje indicando que no se pueden mostrar datos de usuarios

#{question}
"""
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

        if pregunta:
            consulta_sql = formato.format(question=pregunta)
            try:
                # Ejecuta la consulta
                resultado = cadena.run(consulta_sql)
                
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

            except Exception as e:
                resultado = "<div class='d-flex justify-content-center'><p class='m-3 h5 text-center'>Lo sentimos, no fue posible responder la pregunta.</p></div>"
            finally:
                cargando = False  # Esto asegura que se actualice el estado después de procesar la consulta

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
