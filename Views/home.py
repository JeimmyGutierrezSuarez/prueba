from django.http import HttpResponse
from django.template.loader import get_template


class homeRutas: #esta clase maneja todas las solicitudes HTTP que realiacen y devueleve una respuesta 
    
    def home(self): #se define este metodo con el nombre home
        plantilla = get_template('prueba.html')
        return HttpResponse(plantilla.render()) #Esto es un objeto Http el cual maneja lo que hay entre comilas

    def paginaUno(self):
        return HttpResponse('Holi');

    #def home(self):
     #   plantilla = get_Template('pruebi.html') # type: ignore
      #  return HttpResponse(plantilla.render)