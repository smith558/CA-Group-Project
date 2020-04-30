# coding=utf-8
from Tkinter import *

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from dummy import *
from ac_math import *


def frame(root, side=None, expand=YES, fill=BOTH, padx=None, pady=None, anchor=None, font=None):
    w = Frame(root)
    if font:
        w.option_add('*Font', font)

    w.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady, anchor=anchor)
    return w


def calculate_parameter(method, params_given={}, required=()):
    condition = True
    params_needed = {}

    for parameter in required:
        if parameter not in params_given:
            condition = False
            break
        params_needed[parameter] = params_given[parameter]
    if condition:
        return round(method(**params_needed), 4)
    return ''


InputTexts = DummyClass()
InputTexts.RL = [['Vs', 'Enter supply voltage (experimental) [V]'], ['f', 'Enter supply frequency [Hz]'],
                 ['XL', 'Inductive reactance [Ω]'], ['R', 'Enter circuit resistance [Ω]'],
                 ['Z', 'Circuit impedance [Ω]'], ['I', 'Magnitude of the current [A]'],
                 ['θ', 'Phase angle of the circuit [°]'], ['VR', 'Magnitude of the voltage across the resistance [V]'],
                 ['VL', 'Magnitude of the voltage across the inductance [V]'],
                 ['L', 'Enter conductor\'s conductance [H]']]

InputTexts.RC = ''
InputTexts.RLC = ''


class Application(Frame):
    def __init__(self, master=None):
        # declare main Frame
        Frame.__init__(self, master)
        self.master.title('AC Theory application')
        self.winfo_toplevel().resizable(False, False)

        # TODO set font style
        self.master.option_add('*Font', 'Verdana 11 bold')
        self.params_given = {}

        self.pack(expand=YES, fill=BOTH)
        self.create_widgets()

    def plot(self):
        print 'GRAPHING'

        resistance = self.params_given.get('r', 19)
        inductance = self.params_given.get('l', 60e-3)
        frequency = self.params_given.get('f', 47.75)
        current = self.params_given.get('i', 5)
        master = self.chart_frame

        try:
            self.w.destroy()
            print 'RE-DRAWING CHART'
        except:
            pass
        finally:
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            # b = f.add_subplot(2, 1, 2)

            # Data for plotting
            midpoint = 0

            t = np.arange(0, 2 * (1 / frequency), 0.0001)
            w = 2 * pi * frequency
            r = resistance
            l = inductance
            ang = w * l / r
            V = (r ** 2 + (w * l) ** 2) ** 0.5 * current * np.sin(w * t + atan(ang))

            a.plot(t, V)
            a.axhline(y=midpoint, color='grey')

            a.set_ylabel(ylabel='Supply voltage [V]')
            a.set_title(label='Voltage across a sinusoidal AC source')

            canvas = FigureCanvasTkAgg(f, master)
            canvas.draw()
            self.w = canvas.get_tk_widget()
            self.w.pack(side=BOTTOM, fill=BOTH, expand=True, pady=10)

    def calculate_method(self, event, circuit, last_updated):
        print last_updated

        def up_resistor_voltage():
            self.processing_method()
            if last_updated != 'vr' and all(k in self.params_given.keys() for k in ('i', 'r')):
                self.variables['VR'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_resistor_voltage, self.params_given, ('i', 'r'))))
                return True

        def up_supply_voltage():
            self.processing_method()
            if last_updated != 'vs' and all(k in self.params_given.keys() for k in ('i', 'z')):
                self.variables['Vs'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_supply_voltage_2, self.params_given, ('i', 'z'))))
                return True

        def up_inductor_voltage():
            self.processing_method()
            if last_updated != 'vl' and all(k in self.params_given.keys() for k in ('i', 'xl')):
                self.variables['VL'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_inductor_voltage, self.params_given, ('i', 'xl'))))
                return True

        def up_phase_agnle():
            self.processing_method()
            if last_updated != 'θ' and all(k in self.params_given.keys() for k in ('r', 'xl')):
                self.variables['θ'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_phase_angle, self.params_given, ('r', 'xl'))))
                return True

        def up_inductive_reactance():
            self.processing_method()
            if last_updated != 'xl' and all(k in self.params_given.keys() for k in ('f', 'l')):
                self.variables['XL'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_inductive_reactance, self.params_given, ('f', 'l'))))
                return True

        def up_circuit_current():
            self.processing_method()
            if last_updated != 'i' and all(k in self.params_given.keys() for k in ('z', 'vs')):
                self.variables['I'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_circuit_current, self.params_given, ('z', 'vs'))))
                return True

        def up_circuit_impedance():
            self.processing_method()
            if last_updated != 'z' and all(k in self.params_given.keys() for k in ('r', 'xl')):
                self.variables['Z'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_circuit_impedence, self.params_given, ('r', 'xl'))))
                return True

        def up_supply_frequency():
            self.processing_method()
            if last_updated != 'f' and all(k in self.params_given.keys() for k in ('l', 'xl')):
                self.variables['f'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_supply_frequency, self.params_given, ('l', 'xl'))))
                return True

        def up_circuit_resistance():
            self.processing_method()
            if last_updated != 'r' and all(k in self.params_given.keys() for k in ('z', 'xl')):
                self.variables['R'].set(
                    str(calculate_parameter(RL_CIRCUIT.get_circuit_resistance, self.params_given, ('z', 'xl'))))
                return True

        # TODO algorithm
        # i,r -> vr
        if up_resistor_voltage():
            up_supply_voltage()
        # i,xl -> vl
        if up_inductor_voltage():
            up_supply_voltage()
            up_supply_frequency()
        # f,l -> xl
        if up_inductive_reactance():
            up_inductor_voltage()
            up_supply_frequency()
            up_circuit_resistance()
        # vs,z -> i
        if up_circuit_current():
            up_inductor_voltage()
            up_resistor_voltage()
        # xl,r -> z
        if up_circuit_impedance():
            up_circuit_current()
            up_circuit_resistance()
        # r,xl -> θ
        if up_phase_agnle():
            pass
        # l,xl -> f
        if up_supply_frequency():
            pass

    def processing_method(self, circuit=None):
        self.params_given = {}

        for i in self.variables:
            try:
                if self.variables[i].get() == '':
                    continue
                self.params_given[i.lower()] = float(self.variables[i].get())
            except ValueError:
                self.variables[i].set('numbers only')
        print 'params given: ' + str(self.params_given)

    def create_widgets(self):
        def create_menu_window(master):
            self.master_frame = frame(master, padx=20, pady=20)
            title_label = Label(self.master_frame, text='Select circuit:').pack(side=TOP, anchor=N, expand=YES,
                                                                                fill=BOTH)
            selection_frame = frame(self.master_frame, pady=10)

            for circuit in ('RL', 'RC', 'RLC'):
                btn = Button(selection_frame, text=circuit, width=6, height=2)
                btn.pack(side=LEFT, expand=YES, fill=BOTH)

                def handler(event, master_=master, circuit_=circuit):
                    return create_calculations_window(event, master_, circuit_)

                btn.bind('<Button-1>', handler)
                btn.bind('<KeyPress-space>', handler)

        def create_calculations_window(event, master, circuit):
            pack_settings = self.master_frame.pack_info()
            self.master_frame.pack_forget()

            def go_back():
                self.circuit_frame.pack_forget()
                self.master_frame.pack(pack_settings)

            self.circuit_frame = frame(master, padx=20, pady=20, font='Verdana 11 bold')

            navbar_frame = frame(self.circuit_frame)
            go_back = Button(navbar_frame, text='GO BACK', command=go_back)
            go_back.pack(anchor=W, side=LEFT, pady=1)

            refresh = Button(navbar_frame, text='GRAPH', command=self.plot)
            refresh.pack(anchor=NE, pady=1)

            Label(self.circuit_frame, text='Circuit attributes {} circuit'.format(circuit)).pack(pady=10)

            labels_frame = frame(self.circuit_frame, font='Verdana 11')

            self.variables = {}
            if circuit == 'RL':
                for text in InputTexts.RL:
                    var = self.variables[text[0]] = StringVar()
                    entry_frame = frame(labels_frame, side=TOP, anchor=W)

                    Label(entry_frame, text='{} ({}):  '.format(text[1], text[0])).pack(anchor=W, side=LEFT,
                                                                                        pady=1, expand=YES)
                    entry = Entry(entry_frame, textvariable=var)
                    if text[0].lower() in ['i', 'z', 'θ', 'vr', 'vl', 'xl']:
                        entry.configure(state='disabled')
                    # TODO better validation?
                    entry.pack(pady=1, expand=YES)

                    def handler(event, last_updated=text[0].lower()):
                        return self.calculate_method(event, circuit, last_updated)

                    entry.bind('<FocusIn>', handler)
                    entry.bind('<FocusOut>', handler)
                    entry.bind('<KeyRelease-Return>', handler)
                # temp placeholder for chart
                self.chart_frame = frame(self.circuit_frame)
            elif circuit == 'RC':
                pass
            else:
                pass

        create_menu_window(self)


app = Application()
app.mainloop()
