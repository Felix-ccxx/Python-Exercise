import wx
import urllib
import re

from custom_dialogs import ConfigureData

class StockFrame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,None,title=title,size=(500,600))
        self.CreateStatusBar()
        menuBar=wx.MenuBar()

        filemenu=wx.Menu()
        menuBar.Append(filemenu,"&File")

        menuAbout=filemenu.Append(wx.ID_ABOUT,"&About"," Information about this program")
        filemenu.AppendSeparator()
        
        menuQuit = filemenu.Append(wx.ID_EXIT,"Q&uit"," Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onQuit, menuQuit)
        self.SetMenuBar(menuBar)
        
    
