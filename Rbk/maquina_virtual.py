# maquina_virtual.py
from cubo import Cubo
import pycuber as pc
import random
import kociemba
import keyboard

class MaquinaVirtual:
    def __init__(self):
        self.pila_movimientos_no_realizados = []
        self.pila_movimientos_realizados = []  # Asegúrate de que esta línea esté presente
        self.pila_todos_movimientos = []
        self.cubo = Cubo()
        self.instrucciones = []
        self.cube_state_valid = False


    def cargar_programa(self, fuente, instrucciones_por_defecto=None):
     """Carga un programa desde un archivo o lista de instrucciones."""
     if isinstance(fuente, str):  # Se asume que es un nombre de archivo
        try:
            print()
            print("========================================================================")
            print(f"=====   Intentando cargar el programa desde: {fuente}   =====")
            print("========================================================================")
            print()
            with open(fuente, 'r') as file:
                # Cargar las instrucciones desde el archivo
                self.instrucciones = [tuple(linea.strip().split()) for linea in file if linea.strip()]
            
            if not self.instrucciones:  # Verifica si las instrucciones están vacías
                print()
                print("=================================================================================================================")
                print(f"=====   Advertencia: El archivo {fuente} está vacío. Cargando instrucciones predeterminadas...   =====")
                print("=================================================================================================================")
                print()
                self.instrucciones = instrucciones_por_defecto if instrucciones_por_defecto else []
            else:
                print()
                print("======================================================================")
                print(f"=====   Programa cargado desde el archivo: {fuente}   =====")
                print("======================================================================")
                print()
                print("==========================================================================================================")
                print(f"Instrucciones cargadas: {self.instrucciones}")
                print("==========================================================================================================")
                print()
                
        except FileNotFoundError:
            print()
            print("========================================================================================================")
            print(f"=====   Error: El archivo {fuente} no fue encontrado. Cargando instrucciones predeterminadas...   =====")
            print("========================================================================================================")
            print()
            self.instrucciones = instrucciones_por_defecto if instrucciones_por_defecto else []
     elif isinstance(fuente, list):  # Si es una lista, se asigna directamente
        self.instrucciones = fuente
        print()
        print("=================================================================")
        print("=====   Programa cargado desde la lista de instrucciones.   =====")
        print("=================================================================")
        print()
     else:
        print()
        print("====================================================================================================")
        print("=====   Error: Fuente no válida. Debe ser un nombre de archivo o una lista de instrucciones.   =====")
        print("====================================================================================================")
        print()

     if not self.instrucciones:  # Si las instrucciones están vacías después de todo
        print()
        print("=======================================================================================================================================")
        print("=====   No se encontraron instrucciones. Asegúrate de que el archivo no esté vacío o proporciona instrucciones predeterminadas.   =====")
        print("=======================================================================================================================================")
        print()
   








    def mostrar_movimiento(self):
        """Mostrar los movimientos uno a uno cuando el usuario presione las flechas 'arriba' o 'abajo'."""
        print("=====================================================================================================================================")
        print("=====   Presiona la flecha 'arriba' para el siguiente movimiento, 'abajo' para ver movimientos realizados o 'esc' para salir.   =====")
        print("=====================================================================================================================================")


        while True:
            # Wait for the user to press any key (either 'up', 'down' or 'esc')
            event = keyboard.read_event()

            # Check if a key was pressed (not released)
            if event.event_type == keyboard.KEY_DOWN:

                if event.name == 'flecha arriba':  # If the 'up' arrow is pressed
                    if self.pila_movimientos_no_realizados:
                        movimiento = self.pila_movimientos_no_realizados.pop(0)  # Pop the first movement from pila_movimientos
                        print("========================================")
                        print(f"Movimiento ejecutado: {movimiento}")
                        print("========================================")
                        self.pila_movimientos_realizados.append(movimiento)
                    else:
                        print("====================================================")
                        print("=====   No hay más movimientos por ejecutar.   =====")
                        print("====================================================")

                elif event.name == 'flecha abajo':  # If the 'down' arrow is pressed
                    if self.pila_movimientos_realizados:
                        movimiento = self.pila_movimientos_realizados.pop()  # Pop the last movement from pila_movimientorealizados
                        print("===================================================")
                        print(f"Movimientos realizados (retroceso): {movimiento}")
                        print("===================================================")
                        self.pila_movimientos_no_realizados.append(movimiento)  # Re-add it to pila_movimientos for replay
                    else:
                        print("==============================================")
                        print("=====   No hay movimientos realizados.   =====")
                        print("==============================================")

                elif event.name == 'esc':  # If the 'Esc' key is pressed, exit
                    print("========================================================")
                    print("=====   Saliendo de la ejecución de movimientos.   =====")
                    print("========================================================")
                    break

    def mostrar_movimientos(self):
        print()
        print("============================================================================================================================================================")
        print("Mostrando todos los movimientos: ", self.pila_todos_movimientos)  
        print("============================================================================================================================================================")
        print()

    def mostrar_cubo(self):
        self.cubo.mostrar_cubo_kociemba() 

    def mezclar_cubo(self):
     """Generates a scrambled cube and updates its state."""
     self.cubo.mezclar()  # Call the Cubo's mezclar method
     self.cube_state_valid = True  # Set the state to valid

    # Show the cube in Kociemba format
     self.cubo.mostrar_cubo_kociemba()  # Pass the Kociemba state to display it

    def resolver_cubo(self):
        """Resolver el cubo y almacenar la solución en la pila de movimientos en el formato correcto."""
        if self.cube_state_valid:  # Asegúrate de que el cubo esté mezclado antes de resolver
            solucion = self.cubo.resolver()  # Llama al método resolver
            print()
            print("==============================================================================================")
            print("Solución encontrada:", solucion)  # Imprime la solución
            print("==============================================================================================")
            print()
            
            # Apilar la solución en la pila de movimientos
            self.pila_todos_movimientos = solucion.split()  # Dividir la solución en movimientos separados
            self.pila_movimientos_no_realizados = solucion.split()  # Dividir la solución en movimientos separados
        else:
            print("==============================================================================================")
            print("=====   Error: No se puede resolver. Mezcle el cubo primero o cargue un estado válido.   =====")
            print("==============================================================================================")



    def ejecutar_instrucciones(self):
        """Ejecuta las instrucciones cargadas."""
        for instruccion in self.instrucciones:
            print()
            print("================================================")
            print(f"Ejecutando instrucción: {instruccion}")
            print("================================================")
            print()
            self.ejecutar_instruccion(instruccion)

    def ejecutar_instruccion(self, instruccion):
     """Ejecuta una única instrucción."""
     comando = instruccion[0].upper()  # Obtiene el comando (en mayúsculas)

     if comando == "MEZCLAR_CUBO":
        self.mezclar_cubo()
     elif comando in ["MOSTRAR_CUBO", "RESOLVER_CUBO", "MOSTRAR_MOVIMIENTO", "MOSTRAR_MOVIMIENTOS"]:
        if self.cube_state_valid:  # Solo ejecutar si el estado del cubo es válido
            if comando == "MOSTRAR_CUBO":
                self.mostrar_cubo()
            elif comando == "RESOLVER_CUBO":
                self.resolver_cubo()
            elif comando == "MOSTRAR_MOVIMIENTO":
                self.mostrar_movimiento()
            elif comando == "MOSTRAR_MOVIMIENTOS":
                self.mostrar_movimientos()
        else:
            print("===============================================================================")
            print("=====   El estado del cubo no es válido. Solo se puede mezclar el cubo.   =====")
            print("===============================================================================")
     else:
        print()
        print("=============================================")
        print(f"Instrucción no reconocida: {comando}")
        print("=============================================")
        print()

