import tkinter as tk

class GUI(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack
        self.create_wigets()
    
    def create_wigets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["width"] = 15
        self.hi_there["height"] = 10
        self.hi_there["text"] = "Hello World\n(Click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self,text="QUIT",fg="red",command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there,everyone")

root = tk.Tk()
app = GUI(master=root)
root.title("This is a test")
app.mainloop()
