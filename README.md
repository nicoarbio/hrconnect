# hrconnect
Trabajo práctico realizado en Python para la materia Análisis de Sistemas de la Licenciatura en Tecnologías de la Información de la Universidad de Palermo

## Integrantes
- Arbio, Nicolás Garbiel ([nicoarbio](https://github.com/nicoarbio))
- Cobice, Leonardo ([leocobice](https://github.com/leocobice))
- Guerchicoff Adamo, Tomás ([Tguerchicoff](https://github.com/Tguerchicoff))
- Zaragoza, Yago ([Yago-Zaragoza](https://github.com/Yago-Zaragoza))

## Instalación: preparación del ambiente local con las dependencias requeridas

> 💡 En caso que no lo hayas hecho!
> En Poweshell se requiere habilitar los scripts: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

1. Tener python instalado (se utilizó la versión 3.12.2)
1. Ejecutar `python -m venv venv`
1. En Windows: `.\venv\Scripts\activate`. En Linux/Mac `source venv/bin/activate`
1. Ejecutar `pip install -e .`

## Ejecutar aplicación
> La forma fácil es utilizar VSCode y desde `Run and Debug`, ejecutar `HRConnect`. Sino, desde la consola seguir los siguientes pasos
1. Validar que el ambiente local esté activo: `.\venv\Scripts\activate`
1. Ejecutar el programa (desde la raíz del repositorio, admin no requerido)
   ```bash
   py -m src
   ````
1. Al finalizar, se recomienda desconectar el ambiente local ejecutando: `deactivate`

# Pendientes
1. [X] Armar un BeanManager para poder instanciar las clases de los DAOs y services
1. [X] Armar un dao de Posiciones ("positions") para poder borrar posiciones
1. [ ] Armar un service que devuelta el estado del suministro electrico. (Random y con un 5% de posibilidades. De ser así dinámicante debe aparecer una nueva opcion para el hr_partner que le permita cargar la fichada manual)
1. [ ] Sumarle al dao de users (en vez de armar un dao de Notificaciones ("notifications") para poder almacenar las nuevas notifcaciones para los usuarios)
1. [ ] Armar un service para envio de notificaciones cada cierto tiempo
1. [ ] Sumarle al dao de users la posibilidad de crear nuevos usuarios. Para el caso de uso del hr_partner

