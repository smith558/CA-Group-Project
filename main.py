# coding=utf-8
import Tkinter as tk
# AC theory maths calculations module
import AC_math as ac
import tkFont


class Application(tk.Frame):
    def __init__(self, master=None):
        # declare main Frame
        tk.Frame.__init__(self, master)
        # declare fonts
        global helv10; global helv12
        helv10 = tkFont.Font(family='Helvetica', size=10)
        helv12 = tkFont.Font(family='Helvetica', size=12)

        self.grid()
        self.create_widgets()

    # main GUI creation method
    def create_widgets(self):
        def create_input_ui(master):
            # initiate text for labels
            label_texts = ['Vs', 'Vr', 'VL', 'Vc', 'XC', 'XL', 'R', 'Z', 'f', 'C', 'L', 'θ', 'Ω', 'Ω', 'Ω', 'Ω', 'Hz',
                           '°', 'H', 'F', 'V', 'V', 'V', 'V']
            # dictionaries of tk.Label & tk.Entry objects
            labels = {}
            entries = {}

            # # top-window
            # top = master.winfo_toplevel()
            # # make re-sizeable
            # top.columnconfigure(0, weight=1)
            # top.rowconfigure(0, weight=1)

            # set-up grid
            for i in range(4):
                master.columnconfigure(i, minsize=50)
                master.rowconfigure(i)

            # set-up labels & Entries
            for i in range(len(label_texts)):
                _column = 2 if (i >= 12) else 0
                _row = i - 12 if (i >= 12) else i

                # initiate tk.Label objects in labels[] in format 'label_x' where x is a unique integer from 0 - 23
                label = labels['label_{0}'.format(i)] = tk.Label(master, text=label_texts[i],
                                                                 font=helv10)
                label.grid(row=_row, column=_column, ipadx=5, ipady=5, sticky=tk.N + tk.E + tk.S + tk.W)

                # initiate tk.Entry objects in entries[] in format 'entry_x' where x is a unique integer from 0 - 23
                entry = entries['entry_{0}'.format(i)] = tk.Entry(master)
                entry.grid(row=_row, column=_column + 1, ipadx=5, ipady=5, sticky=tk.N + tk.E + tk.S + tk.W)

        def create_start_btn(master, _row=0, _column=0, width=1):
            self.startButton = tk.Button(master, text='Calculator', font=helv12, command=master.quit)
            self.startButton.grid(row=_row, column=_column, ipadx=5, ipady=5, sticky=tk.N + tk.E + tk.S + tk.W,
                                  columnspan=width)

        create_input_ui(self)
        # make an empty row
        self.rowconfigure(12, minsize=35)
        create_start_btn(self, _row=13, _column=0, width=4)

    # back-end processing method
    @staticmethod
    def process_method():
        pass


app = Application()
app.master.title('Sample application')
app.mainloop()
