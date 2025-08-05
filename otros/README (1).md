# Plantilla para desarrollo de prácticas con test mediante Doctest

Este plantilla proporciona una metodología para desarrollar, probar e integrar nuevas funciones de manera modular usando `doctest`.

## 📂 Estructura de la plantilla

```
/practica
│── main.py       # Archivo principal que ejecuta las funciones
│── mylib.py      # Biblioteca de funciones matemáticas o utilitarias
│── README.md     # Documentación de la plantilla que finalmente uses
```

## 🚀 Funcionamiento

### 1️⃣ Agregar Nuevas Funciones

- Define la función en `mylib.py`.
- Incluye ejemplos de prueba en su docstring con `doctest`.

#### Ejemplo:

```python
def suma(a, b):
    """
    Devuelve la suma de dos números.
    
    >>> suma(2, 3)
    5
    >>> suma(-1, 1)
    0
    """
    return a + b
```

### 2️⃣ Ejecutar Funciones

Ejecuta el programa llamando funciones dinámicamente:

```sh
python main.py <nombre_funcion> <parametros>
```

#### Ejemplo:

```sh
python main.py T 5
python main.py suma 10 20
```

### 3️⃣ Ejecutar Pruebas

Para probar todas las funciones definidas en `mylib.py`, usa:

```sh
python main.py --test
```

Esto ejecutará los `doctest` incluidos en cada función.

## ✅ Beneficios de la Metodología

- **Modularidad**: `mylib.py` contiene solo funciones, `main.py` gestiona la ejecución.
- **Pruebas integradas**: `doctest` permite validar las funciones sin herramientas externas.
- **Ejecución flexible**: Se pueden probar funciones sin modificar código.
- **Escalabilidad**: Agregar nuevas funciones es sencillo y ordenado.



