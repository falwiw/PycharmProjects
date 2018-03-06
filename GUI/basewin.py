# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class BaseMainWind
###########################################################################

class BaseMainWind(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"吉吉代理浏览器", pos=wx.DefaultPosition, size=wx.Size(310, 480),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(310, 480), wx.Size(310, 480))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"主窗口测试", wx.Point(-1, -1), wx.Size(100, 18),
                                           wx.ALIGN_CENTRE)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_staticText2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer1.Add(self.m_staticText2, 0, wx.ALIGN_CENTER, 5)

        self.text_main = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer1.Add(self.text_main, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.button_main = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_main.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.button_main.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer1.Add(self.button_main, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_main.Bind(wx.EVT_BUTTON, self.main_button_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def main_button_click(self, event):
        event.Skip()


