import wx

app = wx.App()
window = wx.Frame(None, title="吉吉代理浏览器 - wxPython", size=(310, 480))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(50, 100))
window.Show(True)
app.MainLoop()
