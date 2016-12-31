import wx

class Panel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.maak_input()
        self.velden_maken()
        
    def maak_input(self):
        self.text = wx.TextCtrl(self, value = ""
                                , style = wx.TE_MULTILINE)
        self.knop1 = wx.Button(self, -1, "Geef bijbehorende primers")
        self.max_product = wx.TextCtrl(self, value = "")
        self.start = wx.TextCtrl(self, value = "")
        self.stop = wx.TextCtrl(self, value = "")
        
    def velden_maken(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(wx.StaticText(self, -1,"Voer hier je sequentie in: "), 1, wx.EXPAND | wx.ALL)
        vbox.Add(self.text, 4, wx.EXPAND | wx.ALL)
        vbox.Add(self.knop1, 4, wx.EXPAND | wx.ALL)
        hbox.Add(wx.StaticText(self, -1,"Startpositie : "), 0, wx.EXPAND | wx.ALL)
        hbox.Add(self.start, 1, wx.TOP)
        hbox.Add(wx.StaticText(self, -1,"Stoppositie : "), 0, wx.EXPAND | wx.ALL)
        hbox.Add(self.stop, 1, wx.TOP)
        self.velden_maken2(hbox,vbox)
        
    def velden_maken2(self,hbox,vbox):
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox2.Add(wx.StaticText(self, -1,"Deel sequentie waar annealing " \
                                "plaats mag vinden"), 1, wx.EXPAND | wx.ALL)
        vbox2.Add(hbox, 1, wx.CENTRE | wx.ALL)
        hbox2.Add(vbox2, 1, wx.EXPAND | wx.ALL)
        vbox3.Add(wx.StaticText(self, -1,"Max lengte PCR product: ")
                  , 1, wx.CENTRE | wx.BOTTOM)
        vbox3.Add(self.max_product, 0, wx.CENTRE)
        vbox3.Add(wx.StaticText(self, -1,""), 1, wx.EXPAND | wx.ALL)
        hbox2.Add(vbox3, 1, wx.EXPAND | wx.ALL)
        vbox.Add(hbox2, 4, wx.EXPAND | wx.ALL)
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
        
