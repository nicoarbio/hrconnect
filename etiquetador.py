import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import glob

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("img-processor")
        self.images = []
        self.current_image_idx = 0
        self.image_quadrants = {}  # Diccionario para almacenar los cuadrantes de cada imagen
        self.dragging = False
        self.start_x = None
        self.start_y = None
        self.info_file = "info.txt"  # Nombre del archivo de texto
        self.quadrant_counter = 0  # Contador para los cuadrantes
        self.standard_size = (400, 400)  # Tamaño estándar de las imágenes
        
        self.canvas = tk.Canvas(self, width=self.standard_size[0], height=self.standard_size[1], cursor="crosshair")
        self.canvas.pack()
        
        self.load_button = tk.Button(self, text="Cargar Carpeta", command=self.load_folder, cursor="crosshair")
        self.load_button.pack(side=tk.LEFT)
        
        self.prev_button = tk.Button(self, text="Anterior", command=self.prev_image, cursor="arrow")
        self.prev_button.pack(side=tk.LEFT)
        
        self.next_button = tk.Button(self, text="Siguiente", command=self.next_image, cursor="arrow")
        self.next_button.pack(side=tk.LEFT)
        
        self.save_button = tk.Button(self, text="Guardar Información", command=self.save_info, cursor="arrow")
        self.save_button.pack(side=tk.RIGHT)
        
        self.reset_button = tk.Button(self, text="Restablecer", command=self.reset_quadrants, cursor="arrow")
        self.reset_button.pack(side=tk.RIGHT)
        
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        self.mainloop()
        
    def load_folder(self): # Cargar carpeta con imágenes
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Limpiar datos anteriores al cargar una nueva carpeta
            self.images = []
            self.image_quadrants = {}
            self.current_image_idx = 0
            
            # Cargar imágenes
            for file_path in sorted(glob.glob(folder_path + "/*.jpg")):  # Puedes ajustar la extensión según tus necesidades
                try:
                    print("Cargando imagen:", file_path)
                    image = Image.open(file_path)
                    image = self.resize_image(image, self.standard_size)  # Redimensionar la imagen
                    photo = ImageTk.PhotoImage(image)  # Mantener una referencia a la imagen
                    self.images.append((photo, file_path))
                    self.image_quadrants[file_path] = {"quad_1": [], "quad_2": []}  # Inicializar los cuadrantes para esta imagen
                except Exception as e:
                    print("Error al cargar la imagen:", e)
            self.show_current_image()
        
    def resize_image(self, image, size):
        return image.resize(size)
        
    def show_current_image(self):
        self.canvas.delete("all")
        image, file_path = self.images[self.current_image_idx]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
        
        # Dibujar cuadrantes
        for idx, quad in enumerate(self.image_quadrants[file_path]["quad_1"]):
            self.draw_quadrant(quad, idx)
        for idx, quad in enumerate(self.image_quadrants[file_path]["quad_2"]):
            self.draw_quadrant(quad, idx)
        
    def draw_quadrant(self, quad, idx):
        color = 'red' if idx == 0 else 'blue'
        self.canvas.create_rectangle(quad, outline=color)
        x, y, _, _ = quad
        self.canvas.create_text(x + 10, y + 10, text=str(idx), fill=color)  # Mostrar el número en el cuadrante
        
    def on_press(self, event):
        quadrants_1 = self.image_quadrants[self.images[self.current_image_idx][1]]["quad_1"]
        quadrants_2 = self.image_quadrants[self.images[self.current_image_idx][1]]["quad_2"]
        if len(quadrants_1) < 2 and len(quadrants_2) < 2:
            # Comenzar el arrastre
            self.dragging = True
            self.start_x = event.x
            self.start_y = event.y
        
    def on_drag(self, event):
        # Dibujar el cuadrante mientras se arrastra
        if self.dragging:
            quadrants_1 = self.image_quadrants[self.images[self.current_image_idx][1]]["quad_1"]
            quadrants_2 = self.image_quadrants[self.images[self.current_image_idx][1]]["quad_2"]
            if len(quadrants_1) < 2 or len(quadrants_2) < 2:
                self.show_current_image()
                if len(quadrants_1) < 2:
                    self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='red')
                elif len(quadrants_2) < 2:
                    self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='blue')
        
    def on_release(self, event):
        # Finalizar el arrastre y dibujar el cuadrante
        if self.dragging:
            end_x = event.x
            end_y = event.y
            quadrants_1 = self.image_quadrants[self.images[self.current_image_idx][1]]["quad_1"]
            quadrants_2 = self.image_quadrants[self.images[self.current_image_idx][1]]["quad_2"]
            if len(quadrants_1) < 2:
                quad = (self.start_x, self.start_y, end_x, end_y)
                quadrants_1.append(quad)
            elif len(quadrants_2) < 2:
                quad = (self.start_x, self.start_y, end_x, end_y)
                quadrants_2.append(quad)
            self.dragging = False
            self.start_x = None
            self.start_y = None
            self.show_current_image()
        
    def prev_image(self):
        if self.current_image_idx > 0:
            self.current_image_idx -= 1
            self.show_current_image()
        
    def next_image(self):
        if self.current_image_idx < len(self.images) - 1:
            self.current_image_idx += 1
            self.show_current_image()
            
    def save_info(self):
        # Guardar información en un archivo de texto
        with open(self.info_file, "a") as f:
            for file_path, quadrants_dict in self.image_quadrants.items():
                file_name = file_path.split("/")[-1]
                for quad_key, quadrants in quadrants_dict.items():
                    # Obtén los valores antes de entrar al bucle de cuadrantes
                    value_1 = "0"
                    value_2 = "1"
                    for i, quad in enumerate(quadrants, start=1):
                        if i == 1:
                            value = value_1
                        elif i == 2:
                            value = value_2
                        info = f"{file_name}: {value} - {quad}\n"
                        f.write(info)
        print("Información guardada en", self.info_file)
        
    def reset_quadrants(self):
        self.image_quadrants[self.images[self.current_image_idx][1]] = {"quad_1": [], "quad_2": []}
        self.show_current_image()

if __name__ == "__main__":
    app = App()
