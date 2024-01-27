from django import forms
from django.db.models import Q

from .models import *
from django.forms import ModelForm
from django import forms


CHOICES =(
    ("0","------------"),
    ("eccForm", "Plantilla ECC"),
    ("pruebasDXForm", "Plantilla Pruebas Diagnósticas"),
    ("RSyMAForm", "Plantilla Revisión sistemática y Metaanálisis"),
    ("plantillaSCForm", "Plantilla Serie casos"),
    ("plantillaCTForm", "Plantilla Corte Transversal"),
    ("casosyControlesForm", "Plantilla Casos y Controles"),
    ("cohortesForm", "Plantilla Cohortes"),
    ("ANATOMICOForm", "Plantilla Anatómico y técnica en cadáver"),
    ("validacionEscalasForm", "Plantilla Validación de escalas - Evidencia"),
    ("CongresoForm", "Plantilla Especial - Congreso"),
    ("CONGRESOESPECIAL2Form", "Plantilla Especial 2 - Congreso"),
    ("epForm", "Plantilla EPoster"),
)

class eccForm(ModelForm):
    class Meta:
        model= plantillaECC
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'pcmeISE':'Presentación clara de manejo de equipoise',
            'comite_de_etica':'Comité de ética',
            'registroClinica':'Registrado en clinicaltrials.gov',
            'doeEvP':'Definición de orientación del estudio: explicativo vs. pragmático',
            'dcve':'Definición clara de variables de estudio',
            'Tam_muestra':'¿Justificado por variables de interés?',
            'cdm':'Cálculo descrito en el manuscrito',
            'dca':'Descripción clara de aleatorización',
            'dici':'Descripción de intervenciones clara - inequívoca',
            'daijc':'Definición de análisis interino, justificación, mecanismos',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'pcmeISE':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'registroClinica':forms.Select(attrs={'class':'form-control'}),
            'doeEvP':forms.Select(attrs={'class':'form-control'}),
            'dcve':forms.Select(attrs={'class':'form-control'}),
            'Tam_muestra':forms.Select(attrs={'class':'form-control'}),
            'cdm':forms.Select(attrs={'class':'form-control'}),
            'dca':forms.Select(attrs={'class':'form-control'}),
            'dici':forms.Select(attrs={'class':'form-control'}),
            'daijc':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class pruebasDXForm(ModelForm):
    class Meta:
        model= plantillaPruebasDX
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'ccpor':'¿Comparación con un patrón de oro reconocido?',
            'enmascaramiento':'¿Hubo enmascaramiento?',
            'sappceaee':'¿Se aplicó las pruebas en una población con espectro amplio de la enfermedad de estudio?',
            'Tam_muestra':'¿Tamaño de la muestra explicado?',
            'srp':'¿Se repitieron las pruebas?',
            'pecej':'¿Pruebas estadísticas claramente explicadas y justificadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'ccpor':forms.Select(attrs={'class':'form-control'}),
            'enmascaramiento':forms.Select(attrs={'class':'form-control'}),
            'sappceaee':forms.Select(attrs={'class':'form-control'}),
            'Tam_muestra':forms.Select(attrs={'class':'form-control'}),
            'srp':forms.Select(attrs={'class':'form-control'}),
            'pecej':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class RSyMAForm(ModelForm):
    class Meta:
        model= plantillaRSyMA
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'dcepi':'Definición clara y explícita de preguntas de investigación',
            'debPMBIM':'Descripción de estrategia de búsqueda: palabras, Mesh, bases de datos, idiomas, marco de tiempo',
            'dcdpep':'Descripción clara de proceso de depuración',
            'dmeca':'Descripción de métodos de evaluación de calidad de artículos',
            'dmeh':'Descripción de métodos de evaluación de homogeneidad',
            'dcme':'Descripción clara de métodos estadísticos',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'dcepi':forms.Select(attrs={'class':'form-control'}),
            'debPMBIM':forms.Select(attrs={'class':'form-control'}),
            'dcdpep':forms.Select(attrs={'class':'form-control'}),
            'dmeca':forms.Select(attrs={'class':'form-control'}),
            'dmeh':forms.Select(attrs={'class':'form-control'}),
            'dcme':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class plantillaSCForm(ModelForm):
    class Meta:
        model= plantillaSERIECASOS
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'def_muestra':'Definición de la muestra: tamaño y probabilística vs conveniencia',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'def_muestra':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class plantillacorteTrasversalForm(ModelForm):
    class Meta:
        model= plantillaCORTETRANSVERSAL
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'def_muestra':'Definición de la muestra: tamaño y probabilística vs conveniencia',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'def_muestra':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class casosyControlesForm(ModelForm):
    class Meta:
        model= plantillaCASOSyCONTROLES
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'def_muestra':'Definición de la muestra: tamaño y probabilística vs conveniencia',
            'dsc':'Descripción de selección de controles',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'ecvc':'Estrategias para control de variables de confusión',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'def_muestra':forms.Select(attrs={'class':'form-control'}),
            'dsc':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'ecvc':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class cohortesForm(ModelForm):
    class Meta:
        model= plantillaCOHORTES
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'dmr':'Descripción de método de reclutamiento',
            'mpddred':'Mecanismos para definición y detección de riesgo, exposición y desenlaces',
            'ecs':'Estrategia de control de sesgos',
            'spsiGT':'Seguimiento (Porcentaje de sujetos incluidos/grupo total)',
            'dve':'Definición de variables estudiadas',
            'ecvc':'Estrategias para control de variables de confusión',
            'pea':'¿Pruebas estadísticas adecuadas?',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'cryo': 'Construcción, redacción y ortografía',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'dmr':forms.Select(attrs={'class':'form-control'}),
            'mpddred':forms.Select(attrs={'class':'form-control'}),
            'ecs':forms.Select(attrs={'class':'form-control'}),
            'spsiGT':forms.Select(attrs={'class':'form-control'}),
            'dve':forms.Select(attrs={'class':'form-control'}),
            'ecvc':forms.Select(attrs={'class':'form-control'}),
            'pea':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'cryo':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class selectPlantillaForm(forms.Form):
    required_css_class = 'textLabel'
    plantilla = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label="Plantillas de calificación",choices=CHOICES)

class epForm(ModelForm):
    class Meta:
        model= plantillaEP
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Es conciso pero explica suficientemente el trabajo.',
            'introduccion_justificacion':'Explica el interés especial del caso, por el diagnóstico poco usual, novedad del tratamiento o del desenlace.',
            'material_metodos' : 'Reporta adecuadamente las pruebas diagnósticas pertinentes e intervenciones.',
            'redaccion_ortografia' : 'Redacción y ortografia',
            'resultado':'Se reporta en forma objetiva los resultados.',
            'discusion':'Se expone el interés del caso o casos y se contrasta los resultados en contexto con la literatura pertinente.',
            'presentacion': 'Distribución de texto, tamaño de fuentes, Calidad de fotografías.',
            'referencias': 'Referencias pertinentes incluidas en el texto presentado.',
            'comentario':'Comentarios y/o observaciones.',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'introduccion_justificacion':forms.Select(attrs={'class':'form-control'}),
            'material_metodos':forms.Select(attrs={'class':'form-control'}),
            'redaccion_ortografia':forms.Select(attrs={'class':'form-control'}),
            'resultado':forms.Select(attrs={'class':'form-control'}),
            'discusion':forms.Select(attrs={'class':'form-control'}),
            'presentacion':forms.Select(attrs={'class':'form-control'}),
            'referencias':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class plantillaANATOMICOForm(ModelForm):
    class Meta:
        model= plantillaANATOMICOyTC
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'def_muestra':'Definición de la muestra: Número de especímenes suficiente para controlar variaciones anatómicas descritas',
            'dcpdcd':'Descripción completa de procedimiento y diferencias con conocimiento disponible',
            'dcde':'Descripción completa de demografía de los especímentes',
            'dchape':'Descripción clara de hallazgos anatómicos y/o de procedimiento estudiado',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'def_muestra':forms.Select(attrs={'class':'form-control'}),
            'dcpdcd':forms.Select(attrs={'class':'form-control'}),
            'dcde':forms.Select(attrs={'class':'form-control'}),
            'dchape':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class validacionEscalasForm(ModelForm):
    class Meta:
        model= plantillaVALIDACIONESCALAS
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'ptct':'Proceso de traducción / contratraducción (si aplica)',
            'dpeupcpv':'Descripción de pruebas estadísticas a usar para  cada proceso de la validación',
            'dtmape':'Determinación de tamaño de muestra de acuerdo con pruebas  estadísticas',
            'cpoevnm':'Comparación pertinente con otras escalas válidas en nuestro medio',
            'dcdp':'Descripción completa de demografía de los participantes',
            'rsapps':'Reporte de sujetos que no aceptaron participar o se perdieron en el seguimiento',
            'peprfce':'Pruebas estadísticas pertinentes reportadas en forma concreta pero explícita',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'acar':'Análisis del contexto y aplicabilidad de los resultados',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'ptct':forms.Select(attrs={'class':'form-control'}),
            'dpeupcpv':forms.Select(attrs={'class':'form-control'}),
            'dtmape':forms.Select(attrs={'class':'form-control'}),
            'cpoevnm':forms.Select(attrs={'class':'form-control'}),
            'dcdp':forms.Select(attrs={'class':'form-control'}),
            'rsapps':forms.Select(attrs={'class':'form-control'}),
            'peprfce':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'acar':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class CONGRESOForm(ModelForm):
    class Meta:
        model= plantillaCONGRESO
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'dcve':'Definición clara de variables de estudio',
            'Tam_muestra':'Tamaño de Muestra',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'comentario':'Observaciones y/o comentarios',
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'dcve':forms.Select(attrs={'class':'form-control'}),
            'Tam_muestra':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }

class CONGRESOESPECIAL2Form(ModelForm):
    class Meta:
        model= plantillaCONGRESOESPECIAL2
        exclude = ('trabajo','user','calificacion')

        labels = {
            'titulo' : 'Título',
            'Resumen_estructurado' : 'Resumen estructurado',
            'Palabras_claves':'Palabras claves',
            'Descripcion_de_justificacion':'Descripción de la justificación',
            'Descripcion_de_objetivos': 'Descripción de objetivos',
            'daprpi': 'Diseño adecuado para responder pregunta de investigación',
            'comite_de_etica':'Comité de ética',
            'dcve':'Definición clara de variables de estudio',
            'Tam_muestra':'Tamaño de Muestra',
            'sarclr':'Suficiente análisis de los resultados, comparación con la literatura más reciente',
            'lrcdpcr':'Las referencias citadas son discutidas y puestas en contexto con los resultados',
            'asevc':'Análisis de sesgos, efecto de variables de confusión',
            'avear':'Análisis de la validez externa (aplicabilidad) de los resultados',
            'dcira' :'Definición de todos los costos importantes y relevantes para cada alternativa',
            'lecac' :'La efectividad clínica de cada alternativa es conocida?',
            'qecmc':'Qué tan exacta y creíble es la medición de los costos?',
            'qecmd' :'Qué tan exacta y creíble es la medición de los desenlaces?',
            'cci' :'Se consideró y controló la incertidumbre?',
            'ritiiu' :'Los resultados incluyen todos los items de importancia para los usuarios?',
            'rg' :'Los resultados son generalizables?',
            'comentario':'Observaciones y/o comentarios'
        }
        widgets = {

            'titulo':forms.Select(attrs={'class':'form-control'}),
            'Resumen_estructurado':forms.Select(attrs={'class':'form-control'}),
            'Palabras_claves':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_justificacion':forms.Select(attrs={'class':'form-control'}),
            'Descripcion_de_objetivos':forms.Select(attrs={'class':'form-control'}),
            'daprpi':forms.Select(attrs={'class':'form-control'}),
            'comite_de_etica':forms.Select(attrs={'class':'form-control'}),
            'dcve':forms.Select(attrs={'class':'form-control'}),
            'Tam_muestra':forms.Select(attrs={'class':'form-control'}),
            'sarclr':forms.Select(attrs={'class':'form-control'}),
            'lrcdpcr':forms.Select(attrs={'class':'form-control'}),
            'asevc':forms.Select(attrs={'class':'form-control'}),
            'avear':forms.Select(attrs={'class':'form-control'}),
            'dcira':forms.Select(attrs={'class':'form-control'}),
            'lecac':forms.Select(attrs={'class':'form-control'}),
            'qecmc':forms.Select(attrs={'class':'form-control'}),
            'qecmd':forms.Select(attrs={'class':'form-control'}),
            'cci':forms.Select(attrs={'class':'form-control'}),
            'ritiiu':forms.Select(attrs={'class':'form-control'}),
            'rg':forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','rows': 3}),
        }
