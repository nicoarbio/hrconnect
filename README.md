# img-processor
Trabajo práctico realizado en Python para la materia Análisis de Sistemas de la Licenciatura en Tecnologías de la Información de la Universidad de Palermo

## Requisitos - Crear ambiente local para el proyecto
1. Tener python instalado
1. Ejecutar `python -m venv venv`
1. En Windows: `venv\Scripts\activate`
    En Linux/Mac `source venv/bin/activate`
1. Ejecutar `pip install -r requirements.txt`

> Puede ser que falte la dependencia `tkinter` y sea necesario instalarla en el OS: `sudo apt-get install python3-tk`

## Ejecutar aplicación
1. Ejecutar `python3 etiquetador.py` (puede que en vez de `python3` sea `python`)

## Uso
- Al iniciar la aplicación, puedes cargar una carpeta que contenga imágenes haciendo clic en el botón "Cargar Carpeta".
- Puedes navegar entre las imágenes cargadas utilizando los botones "Anterior" y "Siguiente".
- Para dibujar cuadrantes en la imagen actual, haz clic y arrastra en el área de la imagen.
- Cada cuadrante dibujado se numerará automáticamente, comenzando desde 0.
- Una vez que hayas dibujado los cuadrantes deseados, puedes guardar la información haciendo clic en el botón "Guardar Información". 
