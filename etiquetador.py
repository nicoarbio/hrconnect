import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import glob

class Quadrant:
    def __init__(self, start_x, start_y, end_x, end_y, color, counter_text=""):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color
        self.counter_text = counter_text

    def draw(self, canvas):
        canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, outline=self.color)
        if self.counter_text:
            x = self.start_x + 10
            y = self.start_y - 10
            canvas.create_text(x, y, text=self.counter_text, fill=self.color)

    def __str__(self):
        return f"({self.start_x}, {self.start_y}, {self.end_x}, {self.end_y})"


class CustImage:
    def __init__(self, photo, file_path):
        self.photo = photo
        self.file_path = file_path
        self.quadrants = []
        self.quadrant_counter = 0

    def add_quadrant(self, quadrant):
        if self.quadrant_counter < 2:
            self.quadrants.append(quadrant)
            self.quadrant_counter += 1

    def clear_quadrants(self):
        self.quadrants = []
        self.quadrant_counter = 0

class Folder:
    def __init__(self):
        self.images = []

    def add_image(self, image):
        self.images.append(image)

    def clear_images(self):
        self.images = []

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("img-processor")
        self.folder = Folder()
        self.current_image_idx = 0
        self.standard_size = (500, 500)
        
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
        
    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder.clear_images()
            for file_path in sorted(glob.glob(folder_path + "/*.jpg")):
                try:
                    print("Cargando imagen:", file_path)
                    image = Image.open(file_path)
                    image = self.resize_image(image, self.standard_size)
                    photo = ImageTk.PhotoImage(image)
                    cust_image = CustImage(photo, file_path)
                    self.folder.add_image(cust_image)
                except Exception as e:
                    print("Error al cargar la imagen:", e)
            self.show_current_image()
        
    def resize_image(self, image, size):
        return image.resize(size)
        
    def show_current_image(self):
        self.canvas.delete("all")
        image = self.folder.images[self.current_image_idx]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image.photo)
        for quadrant in image.quadrants:
            quadrant.draw(self.canvas)
        
    def on_press(self, event):
        image = self.folder.images[self.current_image_idx]
        if len(image.quadrants) < 2:
            self.start_x = event.x
            self.start_y = event.y
        
    def on_drag(self, event):
        image = self.folder.images[self.current_image_idx]
        if len(image.quadrants) < 2:
            end_x = event.x
            end_y = event.y
            if len(image.quadrants) == 0:
                color = 'red'
            else:
                color = 'blue'
            self.canvas.delete("quadrant_temp")
            self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=color, tags="quadrant_temp")
        
    def on_release(self, event):
        image = self.folder.images[self.current_image_idx]
        if len(image.quadrants) < 2:
            end_x = event.x
            end_y = event.y
            if len(image.quadrants) == 0:
                color = 'red'
                counter_text = "1"
            else:
                color = 'blue'
                counter_text = "2"
            quadrant = Quadrant(self.start_x, self.start_y, end_x, end_y, color, counter_text)
            image.add_quadrant(quadrant)
            self.canvas.delete("quadrant_temp")
            self.show_current_image()

        
    def prev_image(self):
        if self.current_image_idx > 0:
            self.current_image_idx -= 1
            self.show_current_image()
        
    def next_image(self):
        if self.current_image_idx < len(self.folder.images) - 1:
            self.current_image_idx += 1
            self.show_current_image()
            
    def save_info(self):
        with open("info.txt", "a") as f:
            for cust_image in self.folder.images:
                file_name = cust_image.file_path.split("/")[-1]
                for i, quadrant in enumerate(cust_image.quadrants, start=1):
                    value = "0" if i == 1 else "1"
                    info = f"{file_name}: {value} - {quadrant}\n"
                    f.write(info)
        print("Información guardada en info.txt")
        
    def reset_quadrants(self):
        image = self.folder.images[self.current_image_idx]
        image.clear_quadrants()
        self.show_current_image()

if __name__ == "__main__":
    app = App()
