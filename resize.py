import PySimpleGUI as sg
susunan=[[sg.VPush()],
          [sg.Text("UNISKA MAB", font=("helvetica", 24))],
          [sg.Text("BANJARMASIN", font=("courier", 18))],
          [sg.VPush()]]
window = sg.Window(title="New Icon",
                   layout=susunan,
                   element_justification= "center",
                   icon="favicon.ico",
                   resizable=True,
                   size=(430, 200))
window.read()
window.close()