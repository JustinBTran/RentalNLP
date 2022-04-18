import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from infer import inference
import threading

class App(tk.Tk):
    def __init__(self):
            row = 0
            tk.Tk.__init__(self)
            self.title("Real EsSafe")
            self.geometry("800x700")
            self.intro = tk.Label(text="Real EsSafe")
            self.intro.grid(column=0,row=row)
            row+=1
            # self.descrip = tk.Label(text = "In the text box below, write the symbol of the stock you want to track. Then when you're ready, hit the button to begin.")
            # self.descrip.grid(column=0,row=1)
            self.text = ScrolledText(self, wrap=tk.WORD)
            self.text.grid(column = 0, row =row)
            row += 1
            self.button = tk.Button(text="  Run  ", command = self.start)
            self.button.grid(column = 0, row =row)
            row += 1

    def start(self):
        # predict = inference(self.text.get("1.0",'end-1c'))
        # self.predict = tk.Label(text=predict,
        #                         # bg="red",
        #                         fg="red",
        #                         font="20"
        #                         )
        # self.predict.grid(column=0,row=5)
        x = threading.Thread(target=self.run_infer, args=(self.text.get("1.0", 'end-1c'),))
        x.start()

    def run_infer(self, input):
        predict = inference(input)
        self.predict = tk.Label(text=predict,
                                # bg="red",
                                fg="red",
                                font="20"
                                )
        self.predict.grid(column=0, row=5)


app = App()
app.mainloop()