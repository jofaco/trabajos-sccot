import requests

def cons_vim_api(videoid):
    """Función para consumir la API de vimeo de la sccot con la cual podremos acceder a los videos y sus estadisticas

    Args:
        videoid (int): Código del video en vimeo

    Returns:
        response: Información completa del video en vimeo(Duration, created_time, etc)
    """
    headers = {
        'Authorization': 'Bearer 438a13e91fb038b956189c3eba8becdc',
        'Content-Type': 'application/json',
    }
    response = requests.get('https://api.vimeo.com/videos/' + str(videoid), headers=headers)
    return response.json()

# Ejemplo de uso:
info_video = cons_vim_api(922161785)  # Reemplaza 123456789 con tu ID de video de Vimeo real
print(info_video)
