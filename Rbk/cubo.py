import pycuber as pc
import kociemba

class Cubo:
    def __init__(self):
        self.cube = pc.Cube()  # Initializes a new cube

    def convertir_a_kociemba(self):
        """Convierte el cubo de PyCuber a formato Kociemba."""
        # Definimos las caras en el orden específico que requiere el formato Kociemba
        caras = {
            'U': self.cube.get_face('U'),
            'R': self.cube.get_face('R'),
            'F': self.cube.get_face('F'),
            'D': self.cube.get_face('D'),
            'L': self.cube.get_face('L'),
            'B': self.cube.get_face('B')
        }

        # Convertimos los stickers de cada cara en un solo string de acuerdo al formato Kociemba
        orden = ['U', 'R', 'F', 'D', 'L', 'B']  # El orden de las caras en Kociemba
        estado_pycube = ''.join([str(caras[face][i][j]) for face in orden for i in range(3) for j in range(3)])

        # Reemplazamos los nombres de colores por los identificadores que usa Kociemba y quitamos los corchetes
        estado_kociemba = estado_pycube.replace('w', 'U').replace('y', 'D').replace('g', 'F').replace('b', 'B').replace('r', 'R').replace('o', 'L')
        estado_kociemba = estado_kociemba.replace('[', '').replace(']', '')
        return estado_kociemba    

    def resolver(self):
        """Resuelve el cubo utilizando el algoritmo de Kociemba."""
        kociemba_str = self.convertir_a_kociemba()  # Obtener el estado actual en formato Kociemba
        solucion = kociemba.solve(kociemba_str)  # Resolver el cubo
        return solucion  # Devuelve la solución    

    def mezclar(self):
        """Genera un cubo mezclado y actualiza el estado."""
        scramble = pc.Formula().random()  # Genera un scramble aleatorio
        self.cube(scramble)  # Aplica el scramble al cubo de PyCuber
        self.estado = str(self.cube)  # Actualiza el estado después de mezclar
        return self.estado  # Devuelve el estado actual del cubo    

    def mostrar_cubo_kociemba(self):
        """Muestra el cubo en formato Kociemba."""
        kociemba_str = self.convertir_a_kociemba()  # Obtiene el estado en formato Kociemba

        color_map = {
            'U': '\033[47m',  # Blanco
            'D': '\033[43m',  # Amarillo
            'L': '\033[42m',  # Verde
            'R': '\033[41m',  # Rojo
            'F': '\033[44m',  # Azul
            'B': '\033[48;5;208m'  # Naranja
        }
        reset_color = '\033[0m'  # Resetear color

        def mini_cuadro(color_code):
            return f"{color_code}  {reset_color}"

        print("==============================================================")
        print("=====   Esta es la representación de tu cubo generado:   =====")
        print("==============================================================")
        print()

        print("==========================")
        print("=   Cara Superior (U):   =")
        print("==========================")
        print()
        for i in range(3):
            print("   ".join([mini_cuadro(color_map[kociemba_str[i * 3 + j]]) for j in range(3)]))
            print()

        print("========================")
        print("=   Lados (F, R, L):   =")
        print("========================")
        print()
        for i in range(3):
            print("   ".join([mini_cuadro(color_map[kociemba_str[18 + i]]),
                              mini_cuadro(color_map[kociemba_str[18 + i + 3]]),
                              mini_cuadro(color_map[kociemba_str[18 + i + 6]])]), "|", 
                  "   ".join([mini_cuadro(color_map[kociemba_str[36 + i]]),
                              mini_cuadro(color_map[kociemba_str[36 + i + 3]]),
                              mini_cuadro(color_map[kociemba_str[36 + i + 6]])]), "|", 
                  "   ".join([mini_cuadro(color_map[kociemba_str[9 + i]]),
                              mini_cuadro(color_map[kociemba_str[9 + i + 3]]),
                              mini_cuadro(color_map[kociemba_str[9 + i + 6]])]))
            print()

        print()    

        print("==========================")
        print("=   Cara Inferior (D):   =")
        print("==========================")
        print()

        for i in range(3):
            print("   ".join([mini_cuadro(color_map[kociemba_str[27 + i * 3 + j]]) for j in range(3)]))
            print()

        print("=========================")
        print("=   Cara Trasera (B):   =")
        print("=========================")
        print()

        for i in range(3):
            print("   ".join([mini_cuadro(color_map[kociemba_str[45 + i * 3 + j]]) for j in range(3)]))
            print()
    
