# Máquina Virtual para Cubo de Rubik

Este proyecto implementa una **máquina virtual diseñada específicamente para manipular y resolver un cubo de Rubik** mediante una serie de operaciones predefinidas y un motor de resolución eficiente basado en el **algoritmo de Kociemba**. La máquina virtual permite simular las acciones y visualizar en la terminal el estado del cubo, emulando el funcionamiento de un cubo de Rubik real. Ofrece una interfaz de línea de comandos para ejecutar instrucciones secuenciales, permitiendo tanto la **mezcla** como la **resolución automatizada** del cubo.

Este proyecto busca ofrecer una experiencia interactiva de simulación, brindando una manera sencilla de trabajar con los movimientos y la solución del cubo de Rubik, ideal tanto para desarrolladores interesados en algoritmos de resolución como para entusiastas del cubo de Rubik que desean entender más sobre su funcionamiento interno y los métodos de resolución óptimos.


## Autores

- [@micezer](https://github.com/micezer/AwareLang.git)](https://github.com/micezer/Rubik-Cube-Virtual-Machine.git)

### Objetivo del Proyecto

El cubo de Rubik, famoso rompecabezas tridimensional, presenta múltiples combinaciones y requiere una serie de movimientos específicos para regresar al estado "resuelto". El objetivo de este proyecto es proporcionar una forma automatizada de interactuar con un cubo de Rubik desde la línea de comandos, posibilitando no solo la resolución, sino también la visualización y manipulación del cubo en tiempo real. Esto se logra a través de una **máquina virtual** que procesa instrucciones y actúa sobre un cubo de Rubik virtual, representado por la biblioteca **PyCuber** y resuelto mediante **Kociemba**.

### Requisitos

Para ejecutar este proyecto, asegúrate de contar con las siguientes herramientas y bibliotecas instaladas:

- **Python 3.x**: La versión 3 de Python es necesaria para asegurar la compatibilidad con las bibliotecas utilizadas y con la sintaxis del código.

#### Bibliotecas de Python

Instala las siguientes bibliotecas mediante `pip`:

- **`pycuber`**: Biblioteca que permite la creación, visualización y manipulación de un cubo de Rubik virtual.
  
```bash
pip install pycuber
```

- **`kociemba`**: Implementación del algoritmo de Kociemba para resolver el cubo de Rubik en el menor número de movimientos posible.

```bash
pip install kociemba
```

### Instrucciones Disponibles

- **MEZCLAR_CUBO**: Genera una mezcla aleatoria del cubo, aplicando movimientos aleatorios en cada cara para obtener un estado desordenado.
  
- **MOSTRAR_CUBO**: Visualiza el estado actual del cubo en la terminal, representando cada cara del cubo con colores correspondientes. Esta vista permite al usuario identificar la disposición y colores de las caras como en un cubo de Rubik físico.

- **RESOLVER_CUBO**: Calcula la secuencia óptima de movimientos para resolver el cubo desde su estado actual, utilizando el algoritmo de Kociemba. Al ejecutar esta instrucción, el cubo se restablece a su estado resuelto.

- **MOSTRAR_MOVIMIENTO**: Muestra el último movimiento realizado en el cubo, proporcionando una actualización paso a paso del proceso de resolución o mezcla en curso.

- **MOSTRAR_MOVIMIENTOS**: Muestra todos los movimientos ejecutados en el cubo hasta el momento, proporcionando un historial completo que permite un seguimiento detallado de las operaciones realizadas.


### Características Principales

1. **Mezcla Automática**: La máquina virtual permite mezclar el cubo de Rubik de manera aleatoria y controlada, generando patrones únicos en cada ejecución.

2. **Resolución Óptima**: Utilizando el eficiente algoritmo de Kociemba, el cubo puede resolverse en el menor número de movimientos posible, alcanzando su estado solucionado sin pasos innecesarios.

3. **Visualización en Tiempo Real**: La representación del cubo en la terminal utiliza colores para simular la disposición física y los colores reales de un cubo de Rubik, facilitando la visualización y el seguimiento de cada movimiento en tiempo real.

4. **Seguimiento de Movimientos**: La máquina virtual guarda un historial de movimientos, permitiendo ver la secuencia de operaciones aplicadas al cubo, lo cual es útil para estudiar las combinaciones y pasos necesarios para resolver o manipular el cubo.

5. **Ejecuta Instrucciones desde Archivo o Línea de Comandos**: Puedes cargar instrucciones desde un archivo o utilizar un conjunto de operaciones predeterminadas, proporcionando flexibilidad en su ejecución.



### Aplicaciones

Este proyecto puede servir como una herramienta educativa y práctica para:

- Estudiar algoritmos de resolución de cubo de Rubik.
- Experimentar con diferentes configuraciones de mezcla y resolución.
- Entender el funcionamiento de una máquina virtual aplicada a un problema de resolución secuencial.




## Estructura del Proyecto

Este proyecto se organiza en varios módulos para facilitar la comprensión y mantenimiento del código:

- **`maquina_virtual.py`**: Este archivo contiene la implementación de la clase `MaquinaVirtual`, que se encarga de interpretar y ejecutar las instrucciones para manipular el cubo. Gestiona las operaciones disponibles, como mezclar, resolver, y mostrar el cubo, además de almacenar un registro de movimientos.

- **`cubo.py`**: Define la clase `Cubo`, que representa el cubo de Rubik en sí mismo. Esta clase permite realizar operaciones como convertir el cubo al formato Kociemba, aplicar mezclas, resolver el cubo y mostrar su estado en la terminal mediante colores.

- **`main.py`**: Es el punto de entrada del programa para la ejecución desde la línea de comandos. Utiliza `argparse` para gestionar los argumentos de entrada y permite cargar instrucciones de un archivo o ejecutar un conjunto de instrucciones predeterminadas en la máquina virtual.

Cada módulo está diseñado para una funcionalidad específica, permitiendo así una separación clara de responsabilidades dentro del código.

## Uso

### Ejecutar el Programa

Para ejecutar el programa, usa el siguiente comando en la terminal:

```bash
python main.py -run <ruta_del_archivo>
```

Donde <ruta_del_archivo> es la ruta del archivo que contiene las instrucciones para la máquina virtual.

### Ejecución sin Archivo de Instrucciones

Si no proporcionas un archivo o si el archivo especificado no se encuentra, el programa cargará automáticamente un conjunto de instrucciones predeterminadas para que puedas probar las funcionalidades básicas de la máquina virtual. Estas instrucciones incluyen operaciones como mezclar el cubo, mostrar su estado actual, resolverlo y visualizar los movimientos realizados.

#### Ejemplo de Ejecución

```bash
python main.py -run instrucciones.rbkmv
```

En este ejemplo, la máquina virtual cargará y ejecutará las instrucciones en `instrucciones.rbkmv`. Si el archivo no existe, el programa notificará que se están utilizando las instrucciones predeterminadas.

## Formato del Archivo de Instrucciones

El archivo de instrucciones debe contener una lista de operaciones que la máquina virtual ejecutará secuencialmente. Cada operación debe estar en una línea separada y escrita en mayúsculas. Las instrucciones disponibles permiten mezclar, mostrar y resolver el cubo, además de realizar un seguimiento de los movimientos.

### Ejemplo de Archivo de Instrucciones

```plaintext
MEZCLAR_CUBO
MOSTRAR_CUBO
RESOLVER_CUBO
MOSTRAR_MOVIMIENTO
```

Contribuciones
Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## Explicación del Código

## Clase `MaquinaVirtual`

La clase `MaquinaVirtual` gestiona la ejecución de instrucciones para manipular y resolver un cubo de Rubik utilizando una pila de operaciones. A continuación se detallan las funciones de esta clase y su propósito:

### Funciones de la Clase `MaquinaVirtual`

- **`__init__(self)`**:  
  Constructor de la clase. Inicializa el cubo de Rubik y la pila de movimientos, y establece un diccionario de operaciones que enlaza cada instrucción con su función correspondiente en la máquina virtual.

- **`cargar_programa(self, archivo, instrucciones_predeterminadas)`**:  
  Carga las instrucciones desde un archivo o, si no se encuentra el archivo, carga las instrucciones predeterminadas. Esta función abre el archivo especificado, si existe, y lee cada línea para añadir las instrucciones a la lista de operaciones de la máquina virtual.

- **`ejecutar_instrucciones(self)`**:  
  Ejecuta las instrucciones cargadas en la lista de operaciones de la máquina virtual. Para cada instrucción, llama a la función correspondiente. Este método es el núcleo de la ejecución de la máquina virtual.

- **`mezclar_cubo(self)`**:  
  Genera una secuencia de movimientos aleatorios para mezclar el cubo y los agrega a la pila de movimientos. Esto permite crear una configuración inicial no resuelta del cubo de Rubik.

- **`mostrar_cubo(self)`**:  
  Muestra en la terminal el estado actual del cubo en un formato visual que utiliza colores para representar cada cara, ofreciendo una visión clara de la disposición actual de las piezas del cubo.

- **`resolver_cubo(self)`**:  
  Calcula la secuencia de movimientos necesarios para resolver el cubo en su estado original utilizando el algoritmo de Kociemba, y agrega esta secuencia a la pila de movimientos. Ejecutar esta función deja el cubo en su estado resuelto.

- **`mostrar_movimiento(self)`**:  
  Muestra el último movimiento realizado en el cubo. Esto es útil para hacer seguimiento de cada operación individual aplicada al cubo.

- **`mostrar_movimientos(self)`**:  
  Muestra todos los movimientos realizados en el cubo hasta el momento. Esta función permite visualizar el historial completo de operaciones, facilitando el seguimiento de todas las acciones que se han ejecutado en la máquina virtual.

## Clase `Cubo`

La clase `Cubo` es responsable de representar y manipular un cubo de Rubik, así como de implementar operaciones necesarias para mezclar y resolver el cubo utilizando el algoritmo de Kociemba. A continuación se detallan las funciones de esta clase y su propósito:

### Funciones de la Clase `Cubo`

- **`__init__(self)`**:  
  Constructor de la clase. Inicializa un nuevo cubo de Rubik utilizando la biblioteca `pycuber`. Esto establece el estado inicial del cubo con todos los stickers en sus posiciones correctas.

- **`convertir_a_kociemba(self)`**:  
  Convierte el estado actual del cubo de PyCuber a un formato que puede ser utilizado por el algoritmo de Kociemba. Esta función organiza los stickers de cada cara del cubo en un solo string de acuerdo con el orden requerido por Kociemba, reemplazando los colores por sus identificadores correspondientes.

- **`resolver(self)`**:  
  Utiliza el algoritmo de Kociemba para calcular la secuencia óptima de movimientos necesarios para resolver el cubo a partir de su estado actual. Devuelve la solución en forma de string que describe los movimientos necesarios.

- **`mezclar(self)`**:  
  Genera un cubo mezclado aplicando una serie de movimientos aleatorios. Actualiza el estado del cubo en función de la mezcla generada y devuelve la representación actual del cubo tras la mezcla.

- **`mostrar_cubo_kociemba(self)`**:  
  Muestra el estado actual del cubo en un formato visual en la terminal, utilizando códigos de colores para representar cada cara del cubo. Esta función utiliza el formato Kociemba para presentar la disposición del cubo, facilitando la visualización de su estado actual.

## Clase `main`

La clase `main` actúa como punto de entrada para la ejecución de la máquina virtual que manipula y resuelve el cubo de Rubik. Esta clase gestiona la interacción con el usuario a través de la línea de comandos y coordina la ejecución de las instrucciones. A continuación, se describen las funciones y su propósito:

### Funciones de la Clase `main`

- **`main()`**:  
  Esta es la función principal que se ejecuta al iniciar el programa. Se encarga de las siguientes tareas:

  1. **Análisis de Argumentos**: Utiliza la biblioteca `argparse` para analizar los argumentos proporcionados en la línea de comandos. Permite especificar la ruta de un archivo de instrucciones a ejecutar mediante el parámetro `-run`.

  2. **Inicialización de la Máquina Virtual**: Crea una instancia de la clase `MaquinaVirtual`, que gestiona la ejecución de las operaciones sobre el cubo.

  3. **Instrucciones Predeterminadas**: Define una lista de instrucciones predeterminadas que se ejecutarán si no se proporciona un archivo de instrucciones o si el archivo no se encuentra.

  4. **Carga de Instrucciones**: Verifica si se ha proporcionado un archivo válido. Si es así, carga las instrucciones desde ese archivo. Si no, carga las instrucciones predeterminadas y notifica al usuario sobre la carga de estas.

  5. **Ejecución de Instrucciones**: Llama a la función `ejecutar_instrucciones()` de la clase `MaquinaVirtual` para llevar a cabo las operaciones especificadas en las instrucciones.

  6. **Ejecución Condicional**: Se asegura de que la función `main()` solo se ejecute si el script se ejecuta como programa principal, utilizando el bloque `if __name__ == "__main__":`.

## Bibliografía

- **Documentación de Python**: La documentación oficial de Python proporciona información sobre el lenguaje y sus bibliotecas estándar. Puedes encontrarla en [python.org](https://www.python.org/doc/).

- **pycuber**: Biblioteca utilizada para representar y manipular cubos de Rubik en Python. Su documentación está disponible en [pycuber en GitHub](https://github.com/pycuber/pycuber).

- **Kociemba's Algorithm**: Este algoritmo es fundamental para resolver el cubo de Rubik de manera eficiente. Puedes leer más sobre él en [Kociemba's website](http://kociemba.org/cube.htm) y consultar la implementación en Python en [kociemba en GitHub](https://github.com/hkociemba/RubiksCube-Twisty-Resolver).

- **Algoritmos de resolución de cubos de Rubik**: Para una comprensión más profunda de los algoritmos utilizados en la resolución de cubos, puedes consultar [El Cubo de Rubik](https://www.rubiks.com) y recursos adicionales sobre teoría de grupos y combinatoria.

- **Tutoriales y Artículos**: Existen numerosos tutoriales y artículos en línea que explican cómo implementar cubos de Rubik en diferentes lenguajes de programación. Recursos como [GeeksforGeeks](https://www.geeksforgeeks.org/) y [Medium](https://medium.com/) ofrecen artículos sobre el tema.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar en este proyecto, puedes hacerlo de las siguientes maneras:

1. **Reportar problemas**: Si encuentras errores o problemas en el código, por favor, abre un **issue** en el repositorio para que podamos solucionarlo.

2. **Sugerir mejoras**: Si tienes ideas para mejorar el proyecto o agregar nuevas características, no dudes en compartir tus sugerencias.

3. **Enviar solicitudes de extracción (pull requests)**: Si deseas implementar una mejora o corregir un error, puedes enviar un pull request con tus cambios. Asegúrate de que tu código siga el estilo del proyecto y esté bien documentado.

4. **Documentación**: Ayúdanos a mantener la documentación actualizada y clara. Cualquier mejora en los archivos de documentación será muy apreciada.

5. **Pruebas**: Si puedes agregar pruebas para nuevas características o para mejorar la cobertura de pruebas existente, será de gran ayuda.

Por favor, consulta el archivo `CONTRIBUTING.md` (si está disponible) para obtener más detalles sobre el proceso de contribución.
