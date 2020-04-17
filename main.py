# coding=utf-8
from Tkinter import *
from dummy import *
import Pmw


def frame(root, side=None, expand=YES, fill=BOTH, padx=None, pady=None, anchor=None, font=None):
    w = Frame(root)
    if font:
        w.option_add('*Font', font)

    w.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, anchor=anchor)
    return w


InputTexts = DummyClass()
InputTexts.RL = [['Vs', 'supply voltage'], ['f', 'supply frequency'], ['XL', 'inductive reactance'],
                 ['R', 'circuit resistance'], ['Z', 'circuit impedance'],
                 ['I', ' magnitude of the current'], ['θ', 'phase angle of the circuit'],
                 ['Vr', 'magnitude of the voltage across the resistance'],
                 ['VL', 'magnitude of the voltage across the inductance']]

InputTexts.RC = ''
InputTexts.RLC = ''


class Application(Frame):
    def __init__(self, master=None):
        # declare main Frame
        Frame.__init__(self, master)
        self.master.title('AC Theory application')
        # TODO set font style
        self.master.option_add('*Font', 'Verdana 11 bold')

        self.pack(expand=YES, fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        def create_menu_window(master):
            self.master_frame = frame(master, padx=20, pady=20)
            title_label = Label(self.master_frame, text='Select circuit:').pack(side=TOP, anchor=N, expand=YES,
                                                                                fill=BOTH)
            selection_frame = frame(self.master_frame, pady=10)

            for circuit in ('RL', 'RC', 'RLC'):
                btn = Button(selection_frame, text=circuit, width=5, height=2)
                btn.pack(side=LEFT, expand=YES, fill=BOTH)

                def handler(event, master_=master, circuit_=circuit):
                    return create_calculations_window(event, master_, circuit_)

                btn.bind('<Button-1>', handler)
                btn.bind('<KeyPress-space>', handler)

        def create_calculations_window(event, master, circuit):
            pack_settings = self.master_frame.pack_info()
            self.master_frame.pack_forget()

            def go_back():
                master_frame.pack_forget()
                self.master_frame.pack(pack_settings)

            master_frame = frame(master, padx=20, pady=20, font='Verdana 11 bold')

            go_back = Button(master_frame, text='GO BACK', command=go_back)
            go_back.pack(anchor=W, pady=1)

            label = Label(master_frame, text='Circuit attributes {} circuit'.format(circuit)).pack(pady=10)

            labels_frame = frame(master_frame, font='Verdana 11')

            if circuit == 'RL':
                for entry in InputTexts.RL:
                    Pmw.EntryField(labels_frame, entry_width=8, value='',
                                   label_text='Enter {} ({}):  '.format(entry[1], entry[0]), labelpos=W,
                                   labelmargin=1).pack(anchor=W, pady=1, expand=YES)
            elif circuit == 'RC':
                pass
            else:
                pass

        create_menu_window(self)


app = Application()
app.mainloop()
