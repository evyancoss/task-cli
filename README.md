# Task Manager CLI

Este es un proyecto de línea de comandos para gestionar tareas. Permite agregar, listar, actualizar, eliminar y cambiar el estado de las tareas.

## Estructura del Proyecto

```
.gitignore
main.py
models/
    task.py
    __pycache__/
        task.cpython-312.pyc
src/
    tasks.json
```

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd task-cli
    ```

2. Asegúrate de tener Python instalado (versión 3.6 o superior).

3. Instala las dependencias necesarias (si las hubiera).

## Uso

### Agregar una tarea

```sh
python main.py add --description "Descripción de la tarea"
```

### Listar tareas

```sh
python main.py list [--status <estado>]
```

### Actualizar una tarea

```sh
python main.py update <uid> --description "Nueva descripción"
```

### Eliminar una tarea

```sh
python main.py delete <uid>
```

### Cambiar el estado de una tarea a "en progreso"

```sh
python main.py mark-in-progress <uid>
```

### Cambiar el estado de una tarea a "hecho"

```sh
python main.py mark-done <uid>
```

## Archivos y Directorios

- `main.py`: Archivo principal que contiene la lógica de la CLI.
- `models/task.py`: Contiene las funciones para gestionar las tareas.
- `src/tasks.json`: Archivo JSON donde se almacenan las tareas.
- `models/__pycache__/`: Directorio que contiene archivos compilados de Python.
- `.gitignore`: Archivo para ignorar directorios y archivos específicos en el control de versiones.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.