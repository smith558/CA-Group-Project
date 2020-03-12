# coding=utf-8
import Tkinter as tk
import AC_math as ac


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        def create_input_ui(master):
            # initiate text for labels
            label_text = ['Vs', 'Vr', 'VL', 'Vc', 'XC', 'XL', 'R', 'Z', 'f', 'C', 'L', 'θ', 'Ω', 'Ω', 'Ω', 'Ω', 'Hz',
                          '°', 'H', 'F', 'V', 'V', 'V', 'V']
            # dictionary of tk.Label & tk.Entry objects
            labels = {}
            entries = {}
            # top-window
            top = master.winfo_toplevel()

            # set-up grid
            for i in range(4):
                master.columnconfigure(i, minsize=50, weight=1)
                master.rowconfigure(i, weight=1)
                top.columnconfigure(i, weight=1)
                top.rowconfigure(i, weight=1)

            # set-up labels & entries
            for i in range(len(label_text)):
                _column = 2 if (i >= 12) else 0
                _row = i - 12 if (i >= 12) else i
                print len(label_text)

                label = labels['label_{0}'.format(i)] = tk.Label(master, text=label_text[i])
                label.grid(row=_row, column=_column, ipadx=5, ipady=5, sticky=tk.N + tk.E + tk.S + tk.W)

                entry = entries['entry_{0}'.format(i)] = tk.Entry(master)
                entry.grid(row=_row, column=_column + 1, ipadx=5, ipady=5, sticky=tk.N + tk.E + tk.S + tk.W)

        def create_start_btn(master, _row=0, _column=0, width=1):
            self.startButton = tk.Button(master, text='Calculator', command=master.quit)
            self.startButton.grid(row=_row, column=_column, ipadx=5, ipady=5, sticky=tk.N + tk.E + tk.S + tk.W,
                                  columnspan=width)

        create_input_ui(self)
        self.rowconfigure(12, minsize=35, weight=1)
        create_start_btn(self, _row=13, _column=0, width=4)


app = Application()
app.master.title('Sample application')
app.mainloop()
