# coding=utf-8
from Tkinter import *

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from idlelib.ToolTip import *
from ac_math import *
from dummy import *


def frame(root, side=None, expand=YES, fill=BOTH, padx=None, pady=None, anchor=None, font=None, width=None):
    w = Frame(root, width=width)
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
InputTexts.RL = [['Vs', 'Enter supply voltage (experimental)', 'V', '[V] - Volt - derived unit for electric potential'],
                 ['f', 'Enter supply frequency', 'Hz', '[Hz] - Hertz - derived unit of frequency'],
                 ['XL', 'Inductive reactance', 'Ω', '[Ω] - Ohm - derived unit of electrical resistance'],
                 ['R', 'Enter circuit resistance', 'Ω', '[Ω] - Ohm - derived unit of electrical resistance'],
                 ['Z', 'Circuit impedance', 'Ω', '[Ω] - Ohm - derived unit of electrical resistance'],
                 ['I', 'Magnitude of the current', 'A', '[A] - Ampere -  base unit of electric current'],
                 ['θ', 'Phase angle of the circuit', 'rad', '[rad] - Radian - standard unit of angular measure'],
                 ['VR', 'Magnitude of the voltage across the resistance', 'V',
                  '[V] - Volt - derived unit for electric potential'],
                 ['VL', 'Magnitude of the voltage across the inductance', 'V',
                  '[V] - Volt - derived unit for electric potential'],
                 ['L', 'Enter conductor\'s conductance', 'H', '[H] - Henry - derived unit of electrical inductance']]

InputTexts.RC = [['Vs', 'Enter supply voltage (experimental)', 'V'], ['f', 'Enter supply frequency', 'Hz'],
                 ['XC', 'Capacitive reactance', 'Ω'], ['R', 'Enter circuit resistance', 'Ω'],
                 ['Z', 'Circuit impedance', 'Ω'], ['I', 'Magnitude of the current', 'A'],
                 ['θ', 'Phase angle of the circuit', 'rad'],
                 ['VR', 'Magnitude of the voltage across the resistance', 'V'],
                 ['VC', 'Magnitude of the voltage across the capacitor', 'V'],
                 ['C', 'Enter conductor\'s capacitance', 'F']]

InputTexts.RLC = [['Vs', 'Enter supply voltage (experimental)', 'V'], ['f', 'Enter supply frequency', 'Hz'],
                  ['XC', 'Capacitive reactance', 'Ω'], ['R', 'Enter circuit resistance', 'Ω'],
                  ['Z', 'Circuit impedance', 'Ω'], ['I', 'Magnitude of the current', 'A'],
                  ['θ', 'Phase angle of the circuit', 'rad'],
                  ['VR', 'Magnitude of the voltage across the resistance', 'V'],
                  ['VC', 'Magnitude of the voltage across the capacitor', 'V'], ['XL', 'Inductive reactance', 'Ω'],
                  ['VL', 'Magnitude of the voltage across the inductance', 'V'],
                  ['C', 'Enter conductor\'s capacitance', 'F'], ['L', 'Enter conductor\'s conductance', 'H']]


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
        self.processing_method()

        resistance = self.params_given.get('r')
        inductance = self.params_given.get('l')
        frequency = self.params_given.get('f')
        current = self.params_given.get('i')
        master = self.chart_frame

        try:
            self.w.destroy()
            print 'RE-DRAWING CHART'
        except AttributeError:
            pass
        finally:
            print 'GRAPHING'
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            # b = f.add_subplot(2, 1, 2)

            # Data for plotting
            midpoint = 0

            try:
                t = np.arange(0, 2 * (1 / frequency), 0.0001)
                w = 2 * pi * frequency
                r = resistance
                l = inductance
                ang = w * l / r
                V = (r ** 2 + (w * l) ** 2) ** 0.5 * current * np.sin(w * t + atan(ang))
            except TypeError:
                pass
            else:
                a.plot(t, V)
                a.axhline(y=midpoint, color='grey')

                a.set_ylabel(ylabel='Supply voltage [V]')
                a.grid(True)
                a.set_title(label='Voltage across a sinusoidal AC source')

                canvas = FigureCanvasTkAgg(f, master)
                canvas.draw()
                self.w = canvas.get_tk_widget()
                self.w.pack(side=BOTTOM, fill=BOTH, expand=True, pady=10)

    def info_pop_up(self, circuit, master=None):
        top = Toplevel()
        explainer_txt = Message(top)

        if circuit == 'RL':
            explainer_txt.config(text='RL - Lorem ipsum is placeholder text commonly used in the graphic, '
                                      'print, and publishing industries for previewing layouts and'
                                      'visual mockups.')
        elif circuit == 'RC':
            explainer_txt.config(text='RC - Lorem ipsum is placeholder text commonly used in the graphic, '
                                      'print, and publishing industries for previewing layouts and'
                                      'visual mockups.')
        else:
            explainer_txt.config(text='RLC - Lorem ipsum is placeholder text commonly used in the graphic, '
                                      'print, and publishing industries for previewing layouts and'
                                      'visual mockups.')
        explainer_txt.pack(side=TOP, anchor=N, expand=YES, fill=BOTH, pady=3)

    def calculate_method(self, circuit, last_updated):
        print last_updated

        if circuit == 'RL':
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
        elif circuit == 'RC':
            def up_capacitive_reactance():
                self.processing_method()
                if last_updated != 'xc' and all(k in self.params_given.keys() for k in ('f', 'c')):
                    self.variables['XC'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_capacitive_reactance, self.params_given, ('f', 'c'))))
                    return True

            def up_capacitance_voltage():
                self.processing_method()
                if last_updated != 'vc' and all(k in self.params_given.keys() for k in ('i', 'xc')):
                    self.variables['VC'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_capacitive_voltage, self.params_given, ('i', 'xc'))))
                    return True

            def up_phase_agnle():
                self.processing_method()
                if last_updated != 'θ' and all(k in self.params_given.keys() for k in ('r', 'xc')):
                    self.variables['θ'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_phase_angle, self.params_given, ('r', 'xc'))))
                    return True

            def up_supply_frequency():
                self.processing_method()
                if last_updated != 'f' and all(k in self.params_given.keys() for k in ('c', 'xc')):
                    self.variables['f'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_supply_frequency, self.params_given, ('c', 'xc'))))
                    return True

            def up_circuit_resistance():
                self.processing_method()
                if last_updated != 'r' and all(k in self.params_given.keys() for k in ('z', 'xc')):
                    self.variables['R'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_circuit_resistance, self.params_given, ('z', 'xc'))))
                    return True

            def up_circuit_impedance():
                self.processing_method()
                if last_updated != 'z' and all(k in self.params_given.keys() for k in ('r', 'xc')):
                    self.variables['Z'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_circuit_impedence, self.params_given, ('r', 'xc'))))
                    return True

            def up_resistor_voltage():
                self.processing_method()
                if last_updated != 'vr' and all(k in self.params_given.keys() for k in ('i', 'r')):
                    self.variables['VR'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_resistor_voltage, self.params_given, ('i', 'r'))))
                    return True

            def up_supply_voltage():
                self.processing_method()
                if last_updated != 'vs' and all(k in self.params_given.keys() for k in ('i', 'z')):
                    self.variables['Vs'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_supply_voltage_2, self.params_given, ('i', 'z'))))
                    return True

            def up_circuit_current():
                self.processing_method()
                if last_updated != 'i' and all(k in self.params_given.keys() for k in ('z', 'vs')):
                    self.variables['I'].set(
                        str(calculate_parameter(RC_CIRCUIT.get_circuit_current, self.params_given, ('z', 'vs'))))
                    return True

            # TODO algorithm
            # i,r -> vr
            if up_resistor_voltage():
                up_supply_voltage()
            # i,xc -> vc
            if up_capacitance_voltage():
                up_supply_voltage()
                up_supply_frequency()
            # f,c -> xc
            if up_capacitive_reactance():
                up_capacitance_voltage()
                up_supply_frequency()
                up_circuit_resistance()
            # vs,z -> i
            if up_circuit_current():
                up_capacitance_voltage()
                up_resistor_voltage()
            # xc,r -> z
            if up_circuit_impedance():
                up_circuit_current()
                up_circuit_resistance()
            # r,xc -> θ
            if up_phase_agnle():
                pass
            # c,xc -> f
            if up_supply_frequency():
                pass
        else:
            def up_capacitive_reactance():
                self.processing_method()
                if last_updated != 'xc' and all(k in self.params_given.keys() for k in ('f', 'c')):
                    self.variables['XC'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_capacitive_reactance, self.params_given, ('f', 'c'))))
                    return True

            def up_inductive_reactance():
                self.processing_method()
                if last_updated != 'xl' and all(k in self.params_given.keys() for k in ('f', 'l')):
                    self.variables['XL'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_inductive_reactance, self.params_given, ('f', 'l'))))
                    return True

            def up_capacitance_voltage():
                self.processing_method()
                if last_updated != 'vc' and all(k in self.params_given.keys() for k in ('i', 'xc')):
                    self.variables['VC'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_capacitive_voltage, self.params_given, ('i', 'xc'))))
                    return True

            def up_inductor_voltage():
                self.processing_method()
                if last_updated != 'vl' and all(k in self.params_given.keys() for k in ('i', 'xl')):
                    self.variables['VL'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_inductor_voltage, self.params_given, ('i', 'xl'))))
                    return True

            def up_phase_agnle():
                self.processing_method()
                if last_updated != 'θ' and all(k in self.params_given.keys() for k in ('r', 'xc', 'xl')):
                    self.variables['θ'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_phase_angle, self.params_given, ('r', 'xc', 'xl'))))
                    return True

            def up_supply_frequency():
                self.processing_method()
                if last_updated != 'f' and all(k in self.params_given.keys() for k in ('c', 'xc')):
                    self.variables['f'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_supply_frequency, self.params_given, ('c', 'xc'))))
                    return True

            def up_supply_frequency_2():
                self.processing_method()
                if last_updated != 'f' and all(k in self.params_given.keys() for k in ('l', 'xl')):
                    self.variables['f'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_supply_frequency_2, self.params_given, ('l', 'xl'))))
                    return True

            def up_circuit_resistance():
                self.processing_method()
                if last_updated != 'r' and all(k in self.params_given.keys() for k in ('z', 'xc', 'xl')):
                    self.variables['R'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_circuit_resistance, self.params_given,
                                                ('z', 'xc', 'xl'))))
                    return True

            def up_circuit_impedance():
                self.processing_method()
                if last_updated != 'z' and all(k in self.params_given.keys() for k in ('r', 'xc', 'xl')):
                    self.variables['Z'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_circuit_impedence, self.params_given,
                                                ('r', 'xc', 'xl'))))
                    return True

            def up_resistor_voltage():
                self.processing_method()
                if last_updated != 'vr' and all(k in self.params_given.keys() for k in ('i', 'r')):
                    self.variables['VR'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_resistor_voltage, self.params_given, ('i', 'r'))))
                    return True

            def up_supply_voltage():
                self.processing_method()
                if last_updated != 'vs' and all(k in self.params_given.keys() for k in ('i', 'z')):
                    self.variables['Vs'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_supply_voltage_2, self.params_given, ('i', 'z'))))
                    return True

            def up_circuit_current():
                self.processing_method()
                if last_updated != 'i' and all(k in self.params_given.keys() for k in ('z', 'vs')):
                    self.variables['I'].set(
                        str(calculate_parameter(RLC_CIRCUIT.get_circuit_current, self.params_given, ('z', 'vs'))))
                    return True

            # TODO algorithm
            # i,r -> vr
            if up_resistor_voltage():
                up_supply_voltage()
            # i,xc -> vc
            if up_capacitance_voltage():
                up_supply_voltage()
                up_supply_frequency()
            # f,c -> xc
            if up_capacitive_reactance():
                up_capacitance_voltage()
                up_supply_frequency()
                up_circuit_resistance()
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
                up_capacitance_voltage()
                up_resistor_voltage()
                up_inductor_voltage()
            # xc,r,xl -> z
            if up_circuit_impedance():
                up_circuit_current()
                up_circuit_resistance()
            # r,xc -> θ
            if up_phase_agnle():
                pass
            # c,xc -> f
            if up_supply_frequency():
                pass

    def processing_method(self, circuit=None):
        self.params_given = {}

        for i in self.variables:
            try:
                if self.variables[i].get() == '':
                    continue
                if float(self.variables[i].get()) < 0:
                    self.variables[i].set(u'posi №s only')
                    raise ValueError
                self.params_given[i.lower()] = float(self.variables[i].get())
            except ValueError:
                if self.variables[i].get() != u'posi №s only':
                    self.variables[i].set(u'№s only')

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

            explainer_txt = Message(self.master_frame,
                                    text='Lorem ipsum is placeholder text commonly used in the graphic, '
                                         'print, and publishing industries for previewing layouts and'
                                         'visual mockups.')
            explainer_txt.pack(side=TOP, anchor=N, expand=YES, fill=BOTH, pady=3)

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

            def handler(circuit=circuit, master=navbar_frame):
                return self.info_pop_up(circuit, master)

            help_btn = Button(navbar_frame, bitmap='question', height=26, command=handler)
            help_btn.pack(pady=1, side=RIGHT, padx=1)

            refresh = Button(navbar_frame, text='GRAPH', command=self.plot)
            refresh.pack(anchor=E, pady=1, side=RIGHT)

            Label(self.circuit_frame, text='Circuit attributes {} circuit'.format(circuit)).pack(pady=10)

            labels_frame = frame(self.circuit_frame, font='Verdana 11')

            self.variables = {}
            if circuit == 'RL':
                for text in InputTexts.RL:
                    var = self.variables[text[0]] = StringVar()
                    entry_frame = frame(labels_frame, side=TOP, anchor=W, padx=5)

                    Label(entry_frame, text='{} ({}):  '.format(text[1], text[0])).pack(anchor=W, side=LEFT, pady=1,
                                                                                        expand=YES)

                    field_frame = frame(entry_frame)
                    entry = Entry(field_frame, textvariable=var, width=10)
                    if text[0].lower() in ['i', 'z', 'θ', 'vr', 'vl', 'xl']:
                        entry.configure(state='disabled')
                    # TODO better validation?
                    entry.pack(pady=1, side=LEFT, anchor=W)
                    unit = Label(field_frame, text='{}'.format(text[2]), width=3)
                    unit.pack(side=LEFT, anchor=E)
                    ToolTip(unit, text[3])

                    def handler(event, circuit=circuit, last_updated=text[0].lower()):
                        return self.calculate_method(circuit, last_updated)

                    entry.bind('<FocusOut>', handler)
                    entry.bind('<KeyRelease-Return>', handler)
                # temp placeholder for chart
                self.chart_frame = frame(self.circuit_frame)
            elif circuit == 'RC':
                for text in InputTexts.RC:
                    var = self.variables[text[0]] = StringVar()
                    entry_frame = frame(labels_frame, side=TOP, anchor=W, padx=5)

                    Label(entry_frame, text='{} ({}):  '.format(text[1], text[0])).pack(anchor=W, side=LEFT, pady=1,
                                                                                        expand=YES)

                    field_frame = frame(entry_frame)
                    entry = Entry(field_frame, textvariable=var, width=10)
                    if text[0].lower() in ['i', 'z', 'θ', 'vr', 'vc', 'xc']:
                        entry.configure(state='disabled')
                    # TODO better validation?
                    entry.pack(pady=1, side=LEFT, anchor=W)
                    Label(field_frame, text='{}'.format(text[2]), width=3).pack(side=LEFT, anchor=E)

                    def handler(event, circuit=circuit, last_updated=text[0].lower()):
                        return self.calculate_method(circuit, last_updated)

                    entry.bind('<FocusOut>', handler)
                    entry.bind('<KeyRelease-Return>', handler)
            else:
                for text in InputTexts.RLC:
                    var = self.variables[text[0]] = StringVar()
                    entry_frame = frame(labels_frame, side=TOP, anchor=W, padx=5)

                    Label(entry_frame, text='{} ({}):  '.format(text[1], text[0])).pack(anchor=W, side=LEFT, pady=1,
                                                                                        expand=YES)

                    field_frame = frame(entry_frame)
                    entry = Entry(field_frame, textvariable=var, width=10)
                    if text[0].lower() in ['i', 'z', 'θ', 'vr', 'vc', 'xc', 'vl', 'xl']:
                        entry.configure(state='disabled')
                    # TODO better validation?
                    entry.pack(pady=1, side=LEFT, anchor=W)
                    Label(field_frame, text='{}'.format(text[2]), width=3).pack(side=LEFT, anchor=E)

                    def handler(event, circuit=circuit, last_updated=text[0].lower()):
                        return self.calculate_method(circuit, last_updated)

                    entry.bind('<FocusOut>', handler)
                    entry.bind('<KeyRelease-Return>', handler)

        create_menu_window(self)


app = Application()
app.mainloop()
