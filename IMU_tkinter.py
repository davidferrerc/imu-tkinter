#!/usr/bin/env python
#-*- coding: utf-8 -*-

import Tkinter
import tkFileDialog
import time
import os

def open_file():
    options = {}
    options['filetypes'] = []
    options['filetypes'].append(('TSV files', '.tsv'))
    options['filetypes'].append(('CSV files', '.csv'))
    options['initialdir'] = '/home/pi'
    options['parent'] = root
    options['title'] = 'Open an existing file'
    
    openfile = tkFileDialog.askopenfilename(**options)

    if openfile:
        os.system('gnumeric ' + openfile)
        #Para version raspberry
        #os.system('soffice ' + openfile)

info_widget = """ ATENTION
Please, be patient,wait few seconds while the
magnetometer is stablized"""

#FUNCIONALIDAD CUANDO DESEAMOS GUARDAR LA LECTURA EN UN ARCHIVO
def output_file():
    options = {}
    options['defaultextension'] = '.csv'
    options['filetypes'] = []
    options['filetypes'].append(('CSV files', '.csv')) 
    options['filetypes'].append(('TSV files', '.tsv'))
    options['title'] = 'Choose save directory'

#Seleccionamos la ruta donde guardaremos el archivo
    global outputfile
    outputfile = tkFileDialog.asksaveasfilename(**options)

#Deshabilitamos todos los botones
    btn_abrir.configure (state = 'disabled')
    btn_archivo.configure (state = 'disabled')
    btn_hecho.configure (state = 'disabled')
    btn_calibrar.configure (state = 'disabled')
    btn_visual.configure (state = 'disabled')
    btn_salir.configure (state = 'disabled')
    btn_ayuda.configure (state = 'disabled')

#Mostramos ventana de aviso
    global toplevel
    toplevel = Tkinter.Toplevel()
    toplevel.title('Calibrating Magnetometer')
    toplevel.minsize(350,150)
    toplevel.maxsize(350,150)
    toplevel.config(cursor= 'watch')
    label1 = Tkinter.Label(toplevel, justify = 'center',pady = 10\
    
                       , text=info_widget,width =40) 
    label1.pack()
    
    label2 = Tkinter.Label(toplevel,fg = 'red', justify = 'center',pady = 10\
    , text="Dont move the sensor while the button is enabled (45 sec)", width =40)
    label2.pack()
    global buttonOK
    buttonOK = Tkinter.Button(toplevel, text= "OK, Run it" \
                             , width=20,state = 'disabled', command = enable_gui)
    buttonOK.pack()

    toplevel.after(45000,inicioimu_enablebutton)

#FUNCIONALIDAD CUANDO DESEAMOS VER LA LECTURA EN LA VENTANA DE COMANDOS                  
def inicioimu_disable():
#Deshabilitamos todos los botones
    btn_abrir.configure (state = 'disabled')
    btn_archivo.configure (state = 'disabled')
    btn_hecho.configure (state = 'disabled') 
    btn_calibrar.configure (state = 'disabled')
    btn_visual.configure (state = 'disabled')
    btn_salir.configure (state = 'disabled')
    btn_ayuda.configure (state = 'disabled')
   
#Mostramos ventana de aviso
    global toplevel
    toplevel = Tkinter.Toplevel()
    toplevel.title('Calibrating Magnetometer')
    toplevel.minsize(350,150)
    toplevel.maxsize(350,150)
    toplevel.config(cursor= 'watch')
    label1 = Tkinter.Label(toplevel, justify = 'center',pady = 10\
                           , text=info_widget,width =40)
    label1.pack()
    
    label2 = Tkinter.Label(toplevel,fg = 'red', justify = 'center',pady = 10\
    , text= "Dont move the sensor while the button is enabled (45 sec)" , width =40)
    label2.pack()
    global buttonOK
    buttonOK = Tkinter.Button(toplevel, text= "OK, Run it" \
                             , width=20,state = 'disabled', command = enable_gui)
    buttonOK.pack()

    toplevel.after(45000,inicioimu_enablebutton)

def inicioimu_enablebutton():

    buttonOK.configure(state = 'normal')
#Lanzamos comando de arranque
    if str(mode.get()) == 'raw':
        os.system( 'minimu9-ahrs -b /dev/'\
                     + str(i2c.get()) \
                     + ' -- mode ' + str(mode.get()) \
                     + ' > ' + outputfile)
    else:
        os.system( 'minimu9-ahrs -b /dev/'\
                     + str(i2c.get()) \
                     + ' -- mode ' + str(mode.get()) \
                     + ' -- output ' + str(form.get()) \
                     + ' > ' + outputfile)

def enable_gui():
    btn_abrir.configure (state = 'normal')
    btn_archivo.configure (state = 'normal')
    btn_hecho.configure (state = 'normal')
    btn_calibrar.configure (state = 'normal')
    btn_visual.configure (state = 'normal')
    btn_salir.configure (state = 'normal')
    btn_ayuda.configure (state = 'normal')
    toplevel.destroy()

def calibrate():

#GUI para seguir instrucciones calibracion de la IMU
    lbl_message = """Please, read the instructions
on command window"""
    topcalib = Tkinter.Toplevel()
    topcalib.title('Calibrating IMU')
    topcalib.minsize(250,100)
    topcalib.maxsize(250,100)
    topcalib.config(cursor= 'watch')
    labelcal = Tkinter.Label(topcalib,fg = 'red', justify = 'center',pady = 10\
                           , text=lbl_message, width =40)
    labelcal.pack()
    buttoncal = Tkinter.Button(topcalib, text= "OK" \
                             , width=20, command = topcalib.destroy)
    buttoncal.pack()

#Lanzamos comando de calibracion
    os.system( 'minimu9-ahrs-calibrate -b /dev/' + str(i2c.get()))
    
def visualizer():
#Lanzamos comando para el visualizador
    os.system( 'minimu9-ahrs -b /dev/' + str(i2c.get()) + ' | ahrs-visualizer')

#Ventana para cierre del visualizador
    global toplvlvis
    toplvlvis = Tkinter.Toplevel()
    toplvlvis.title('Close visualizer')
    toplvlvis.minsize(250,100)
    toplvlvis.maxsize(250,100)    
    labelvis = Tkinter.Label(toplvlvis,fg = 'red', justify = 'center',pady = 10\
                           , text= "Click here to close the visualizer" , width =40)
    labelvis.pack()
    buttonclose = Tkinter.Button(toplvlvis, text= "Close visualizer" \
                             , width=20, command = closevisualizer)
    buttonclose.pack()


#Lanzamos comando para matar el proceso del visualizador
def closevisualizer():      
    os.system('killall ahrs-visualizer')
    toplvlvis.destroy()

#Lanzamos comando para abrir la ayuda
def ayuda():
    os.system('man minimu9-ahrs')

#Funcion para deshabilitar la eleccion de los formatos cuando elegimos el modo raw
def disablerbutmode():
    formato_Rbuton_matrix.configure(state = 'disabled')

    formato_Rbuton_quaternion.configure(state = 'disabled')

    formato_Rbuton_euler.configure(state = 'disabled')

#Funcion para habilitar la eleccion de los formatos cuando deseleccionamos el modo raw                  
def enablerbutmode():
    formato_Rbuton_matrix.configure(state = 'normal')

    formato_Rbuton_quaternion.configure(state = 'normal')

    formato_Rbuton_euler.configure(state = 'normal')
   

#********************** Creacion de la interfaz gráfica principal **********************#
#Creamos el GUI...
root = Tkinter.Tk()
root.minsize(371,325)
root.maxsize(371,325) 

i2c = Tkinter.StringVar()
mode = Tkinter.StringVar()
form = Tkinter.StringVar()

#Titulo
root.title( "MinIMU9-V2 sensor management" )


#Seleccion del bus I2C
i2c_frm = Tkinter.LabelFrame(root, text = "I2C bus selection" , width = '30' )

i2c_Rbuton0 = Tkinter.Radiobutton(i2c_frm, text= "Port 0" , width = 19,\
                        value= "i2c-0" , justify=Tkinter.CENTER, variable = i2c)

i2c_Rbuton1 = Tkinter.Radiobutton(i2c_frm, text= "Port 1" , width = 18,\
                        value= "i2c-1" , justify=Tkinter.CENTER, variable = i2c)
#Empaquetamos...
i2c_Rbuton0.grid(row = 0, column = 0)

i2c_Rbuton1.grid(row = 0, column = 1)


#Modo de ejecucion
modo_frm = Tkinter.LabelFrame(root, text= "Execution mode" )

modo_Rbuton_normal = Tkinter.Radiobutton(modo_frm, text= "Standard Mode       " ,\
                            width = 19, justify=Tkinter.LEFT, value= "normal" , \
                                    variable = mode, command = enablerbutmode)

modo_Rbuton_gyro = Tkinter.Radiobutton(modo_frm, text= "Gyro-only Mode" , \
                            width = 18, justify=Tkinter.LEFT, value= "gyro" ,\
                                    variable = mode, command = enablerbutmode)

modo_Rbuton_compass = Tkinter.Radiobutton(modo_frm, text= "Compass-only Mode" ,\
                            width = 19, justify=Tkinter.LEFT, value= "compass" ,\
                                    variable = mode, command = enablerbutmode)

modo_Rbuton_raw = Tkinter.Radiobutton(modo_frm, text= "Raw Mode        " ,\
                            width = 18, justify=Tkinter.LEFT, value= "raw" ,\
                                    variable = mode, command = disablerbutmode)

#Empaquetamos...
modo_Rbuton_normal.grid(row = 0, column = 0)

modo_Rbuton_gyro.grid(row = 0, column = 1)

modo_Rbuton_compass.grid(row = 1, column = 0)

modo_Rbuton_raw.grid(row = 1, column = 1)

#Formatos de salida...
formato_frm = Tkinter.LabelFrame(root, text= "Output format" )

formato_Rbuton_matrix = Tkinter.Radiobutton(formato_frm, text= "Cosine Matrix format" ,\
                    width = 41, justify=Tkinter.LEFT, value= "matrix" , variable = form)

formato_Rbuton_quaternion = Tkinter.Radiobutton(formato_frm, text= "Quaternion format   " ,\
                    width = 41, justify=Tkinter.LEFT, value= "quaternion" , variable = form)

formato_Rbuton_euler = Tkinter.Radiobutton(formato_frm, text= "Euler Angles format " ,\
                    width = 41, justify=Tkinter.LEFT, value= "euler" , variable = form)

#Empaquetamos...
formato_Rbuton_matrix.grid(row = 0, column = 0)

formato_Rbuton_quaternion.grid(row = 1, column = 0)

formato_Rbuton_euler.grid(row = 2, column = 0)


i2c_frm.pack(fill='both', expand='no', padx = 5)
modo_frm.pack(fill='both', expand='no', padx = 5)
formato_frm.pack(fill='both', expand='no', padx = 5,pady=5)

#Botones...
boton_frm = Tkinter.Frame(root)

btn_abrir = Tkinter.Button(boton_frm, text='Open File', width= 13, \
                        padx = 5, pady = 5, relief = 'groove', command = open_file)

btn_archivo = Tkinter.Button(boton_frm, text='Output File', width= 13, \
                        padx = 5, pady = 5, relief = 'groove', command = output_file)

btn_hecho = Tkinter.Button(boton_frm, text='Done', width = 13, \
                        padx = 5, pady = 5, relief = 'groove', command=inicioimu_disable)

btn_calibrar = Tkinter.Button(boton_frm, text='Calibrate', width = 13, \
                        padx = 5, pady = 5, relief = 'solid', command=calibrate)

btn_visual = Tkinter.Button(boton_frm, text='Visualizer', width = 13, \
                        padx = 5, pady = 5, relief = 'solid', command=visualizer)

btn_salir = Tkinter.Button(boton_frm, text='Exit', width = 13, \
                        command = root.destroy, padx = 5, pady = 5, relief = 'sunken')

btn_ayuda = Tkinter.Button(boton_frm, text='Help', width = 8, \
                           relief = 'flat', command=ayuda)

btn_abrir.grid(row=0, column=0)
btn_archivo.grid(row=1, column=0)
btn_hecho.grid(row = 2, column=0)
btn_calibrar.grid(row=0, column=2)
btn_visual.grid(row=1, column=2)
btn_salir.grid(row=0, column=3)
btn_ayuda.grid(row=1, column=3)

boton_frm.pack()

root.mainloop()
