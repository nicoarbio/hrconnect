# hrconnect
Trabajo práctico realizado en Python para la materia Análisis de Sistemas de la Licenciatura en Tecnologías de la Información de la Universidad de Palermo

## Integrantes
- Arbio, Nicolás Garbiel ([nicoarbio](https://github.com/nicoarbio))
- Cobice, Leonardo ([leocobice](https://github.com/leocobice))
- Guerchicoff Adamo, Tomás ([Tguerchicoff](https://github.com/Tguerchicoff))
- Zaragoza, Yago ([Yago-Zaragoza](https://github.com/Yago-Zaragoza))

### Requerimientos
- Python 3.10 o superior
- `pip install bcrypt`

### Instalación
1. Clonar el repositorio (SSH o HTTPS)
    ```bash
    git clone git@github.com:nicoarbio/hrconnect.git
    ```
    ```bash
    git clone https://github.com/nicoarbio/hrconnect.git
    ```

1. Entrar al repositorio 
   ```bash
   cd hrconnect
   ```

### Requisitos - Crear ambiente local para el proyecto
1. Tener python instalado
1. Ejecutar `python -m venv venv`
1. En Windows: `.\venv\Scripts\activate`. En Linux/Mac `source venv/bin/activate`
1. Ejecutar `py -m pip install flit wheel`
1. Ejecutar `flit install --deps=all --symlink`
1. Ejecutar `pip install -e .`

### Ejecutar aplicación

1. Ejecutar el programa (desde la raíz del repositorio)
   ```bash
   py -m src
   ```

##### Links útiles
- [A practical guide to python project structure and packaging](https://medium.com/@joshuale/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95.)
