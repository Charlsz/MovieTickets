'''
select the movie, the time, 
the seat position and 
the number of tickets you want to sell. 
There are two types of tickets, VIP and regular.
'''
peliculas=[]
horas=[]
class movie():
    
    def __init__(self,pelicula):
        self.pelicula = pelicula
    
    def registrarPelicula():
        '''
        registramos las peliculas disponibles
        '''
        nombrePelicula = input("Ingresa nombre de pelicula a transmitir: ")
        peliculas.append(nombrePelicula)
        print("Las peliculas disponibles son:", *peliculas, sep = "\n")
        
    def registrarHoras():
        '''
        registramos las horas disponibles
        '''
        print("TIEMPO EN HORA MILITAR")
        print("tenga en cuenta que solo será a horas puntuales")
        try:
            times = input("Ingresa la hora a la que se reproducira la pelicula: ")
            if (times == 25):
                print("Error, hora no valida")
                times = input("Escriba de nuevo la hora: ")
            else:
                horas.append(times)
            print("Las horas disponibles son: ", *horas)
        except TypeError:
            print("No se aceptan letras en las horas")
        
    def mostrarPeliculas():
        print("Las peliculas disponibles son:", *peliculas, sep = "\n")
        
    def mostrarHoras():
        print("Las horas disponibles son: ", *horas)