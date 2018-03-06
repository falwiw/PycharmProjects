import htmlPy
from back_end import BackEnd

app = htmlPy.AppGUI(title=u"Sample application")

app.width = 310
app.height = 410
app.maximized = False
app.template_path = "."
app.bind(BackEnd(app))

app.template = ("index.html", {})

if __name__ == "__main__":
    app.start()