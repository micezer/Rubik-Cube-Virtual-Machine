from maquina_virtual import MaquinaVirtual
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='Ejecutar programa en la máquina virtual.')
    parser.add_argument('-run', dest='archivo', required=False,
                        help='Ruta del archivo de programa a ejecutar')
    args = parser.parse_args()

    maquina = MaquinaVirtual()  # Inicializa la máquina virtual

    # Definir las instrucciones predeterminadas
    instrucciones_predeterminadas = [
        ("MEZCLAR_CUBO",),
        ("MOSTRAR_CUBO",),
        ("RESOLVER_CUBO",),
        ("MOSTRAR_MOVIMIENTO",),
        ("MOSTRAR_MOVIMIENTOS",),
    ]

    if args.archivo and os.path.isfile(args.archivo):
        # Cargar instrucciones desde el archivo
        maquina.cargar_programa(args.archivo, instrucciones_predeterminadas)
    else:
        print()
        print("==============================================================================")
        print("=====   Archivo no encontrado, cargando instrucciones predeterminadas.   =====")
        print("==============================================================================")
        print()
        maquina.cargar_programa(instrucciones_predeterminadas)

    maquina.ejecutar_instrucciones()  # Ejecuta las instrucciones

if __name__ == "__main__":
    main()