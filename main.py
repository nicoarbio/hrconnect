import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageAnnotationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Annotation App")
        
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        self.rect_start_x = None
        self.rect_start_y = None
        self.rect_end_x = None
        self.rect_end_y = None

        self.rectangles = []

        self.load_button = tk.Button(self.master, text="Cargar Imagen", command=self.load_image)
        self.load_button.pack()

        self.save_button = tk.Button(self.master, text="Guardar Rectángulos", command=self.save_rectangles)
        self.save_button.pack()

        self.canvas.bind("<Button-1>", self.start_rect)
        self.canvas.bind("<B1-Motion>", self.draw_rect)
        self.canvas.bind("<ButtonRelease-1>", self.end_rect)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((800, 600), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def start_rect(self, event):
        self.rect_start_x = self.canvas.canvasx(event.x)
        self.rect_start_y = self.canvas.canvasy(event.y)

    def draw_rect(self, event):
        self.rect_end_x = self.canvas.canvasx(event.x)
        self.rect_end_y = self.canvas.canvasy(event.y)
        self.canvas.delete("temp_rect")
        self.canvas.create_rectangle(self.rect_start_x, self.rect_start_y, self.rect_end_x, self.rect_end_y, outline="red", tags="temp_rect")

    def end_rect(self, event):
        self.rect_end_x = self.canvas.canvasx(event.x)
        self.rect_end_y = self.canvas.canvasy(event.y)
        self.rectangles.append((self.rect_start_x, self.rect_start_y, self.rect_end_x, self.rect_end_y))
        self.canvas.create_rectangle(self.rect_start_x, self.rect_start_y, self.rect_end_x, self.rect_end_y, outline="red")
    
    def save_rectangles(self):
        if self.rectangles:
            with open("rectangles.txt", "w") as f:
                for rect in self.rectangles:
                    f.write(f"{rect[0]},{rect[1]},{rect[2]},{rect[3]}\n")
            print("Rectángulos guardados en rectangles.txt")

def main():
    root = tk.Tk()
    app = ImageAnnotationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()