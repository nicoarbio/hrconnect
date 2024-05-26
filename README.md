# hrconnect
Trabajo práctico realizado en Python para la materia Análisis de Sistemas de la Licenciatura en Tecnologías de la Información de la Universidad de Palermo

## Integrantes
- Arbio, Nicolás Garbiel ([nicoarbio](https://github.com/nicoarbio))
- Cobice, Leonardo ([leocobice](https://github.com/leocobice))
- Guerchicoff Adamo, Tomás ([Tguerchicoff](https://github.com/Tguerchicoff))
- Zaragoza, Yago ([Yago-Zaragoza](https://github.com/Yago-Zaragoza))

### Instalación: preparación del ambiente local con las dependencias requeridas
**¡Modo administrador requerido!**

1. Tener python instalado
1. Ejecutar `python -m venv venv`
1. En Windows: `.\venv\Scripts\activate`. En Linux/Mac `source venv/bin/activate`
1. Ejecutar `py -m pip install flit wheel`
1. Ejecutar `flit install --deps=all --symlink`
1. Ejecutar `pip install -e .`

### Ejecutar aplicación
1. Validar que el ambiente local esté activo: `.\venv\Scripts\activate`
1. Ejecutar el programa (desde la raíz del repositorio, admin no requerido)
   ```bash
   py -m src
   ````
1. Al finalizar, se recomienda desconectar el ambiente local ejecutando: `deactivate`
