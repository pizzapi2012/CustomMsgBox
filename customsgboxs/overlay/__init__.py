import customtkinter as ctk
import sys

def rgb_color(r: int, g: int, b: int, text: str) -> str:
    return str(f"\033[38;2;{r};{g};{b}m{text}\033[0m")

class Overlay:
    def __init__(self, corner: int):
        self.root = ctk.CTk()
        
        self.running = False
        
        self.root.attributes('-topmost', 1)
        
        self.root.grid_columnconfigure(0, weight=1)
        
        self.root.grid_rowconfigure(0, weight=1)
        
        self.root.overrideredirect(True)
        
        self.corner = corner
        
        if sys.platform.startswith("win"):
            transparent_color = '#000001'
            self.root.attributes("-transparentcolor", transparent_color)
        elif sys.platform.startswith("darwin"):
            transparent_color = 'systemTransparent'
            self.root.attributes("-transparent", True)
        else:
            self.corner = 0
        
        
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=self.corner, bg_color=transparent_color)
        self.main_frame.grid(sticky="nswe")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        self.exitbutton = ctk.CTkButton(self.main_frame, text="X", text_color="white", command=self.exit_win)
        self.exitbutton.pack(anchor="ne")
        self.main_frame.pack()
    
    def exit_win(self):
        self.root.destroy()
    
    def set_size(self, size: tuple):
        self.root.geometry(str(size[0]) + "X" + str(size[1]))
    
    def run(self):
        if not self.running:
            self.running = True
            self.root.eval('tk::PlaceWindow . center')
            self.root.mainloop()
        elif self.running:
            print(rgb_color(255, 0, 0, "Error: ") + rgb_color(255, 255, 255, "overlay is still running!"))

main = Overlay(corner=30)

main.run()
main.root.geometry("100x100")