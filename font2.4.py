import PySimpleGUI as sg
sg.theme("DarkTeal1")
sg.theme_text_color("#ffffff")
window = sg.Window(title="Profile", layout=[
        [sg.Text("FTI UNISKA", font=("Helvetica", 24), text_color="#FF885B",)],
        [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "italic", "bold", "underline"), text_color="#243642")],
        [sg.Text("UNISKA MAB BANJARMASIN", text_color="#E2F1E7")],
    ],
    size=(430, 150),
    font=("Times", 18)
)
window.read()
window.close()
