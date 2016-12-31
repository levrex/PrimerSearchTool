import wx

class Panel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        
        self.maak_input()
        self.velden_maken()
        
    def maak_input(self):
        self.knop1 = wx.Button(self, -1, "Ga terug naar invoerscherm")
        self.sequentie = wx.StaticText(self, -1,"ATGT")
        self.posities = wx.StaticText(self, -1,"")
        
    def velden_maken(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.posities, 1, wx.EXPAND | wx.ALL)
        vbox.Add(wx.StaticText(self, -1,"De primers zijn als volgt: ")
                 , 1, wx.EXPAND | wx.ALL)
        vbox.Add(self.sequentie, 4, wx.EXPAND | wx.ALL)
        vbox.Add(self.knop1, 4, wx.EXPAND | wx.ALL)
        self.SetSizer(vbox)
        
        
class Schermpje(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (600,600))
        self.paneeltje = Panel(self, -1)
        self.Show(True)
        
if __name__ == "__main__":
        app = wx.App()
        Schermpje(None, -1, "Primer program")
        app.MainLoop()
        
