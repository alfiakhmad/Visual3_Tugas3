import PySimpleGUI as sg
sg.theme("DarkTeal1")
sg.theme_text_color("#ffffff")
window = sg.Window(title="Profile", layout=[
        [sg.Text("FTI UNISKA", font=("Helvetica", 24))],
        [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "italic", "bold", "underline"))],
        [sg.Text("UNISKA MAB BANJARMASIN")],
    ],
    size=(430, 200),
    font=("Times", 18)
)
window.read()
window.close()
