from __future__ import division ## essential for decimals
import wx

import Primerprogram_input
import Primerprogram_output


class Schermpje(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 500)) 
        self.scherm1 = Primerprogram_input.Panel(self, -1)
        self.scherm2 = Primerprogram_output.Panel(self, -1)
        self.huidig_s = self.scherm1
        self.set_buttons()
        self.scherm_show()
        self.Centre()
        self.Show(True)
      
    def scherm_show(self):
        self.scherm2.Show(False)
        boxje = wx.BoxSizer()
        boxje.Add(self.scherm1, 1, wx.EXPAND)
        boxje.Add(self.scherm2, 1, wx.EXPAND)
        self.SetSizer(boxje)
        
    def set_buttons(self):
        self.scherm1.knop1.Bind(wx.EVT_BUTTON, self.event_knop)
        self.scherm2.knop1.Bind(wx.EVT_BUTTON, self.event_terug)
        
    def event_terug(self, event):
        self.huidig_s.Show(False)
        self.scherm1.Show(True)
        self.huidig_s = self.scherm1
        self.Layout()
        
    def event_knop(self, event):
        a = event.GetEventObject().GetLabel()
        if a == "Geef bijbehorende primers":
            self.find_primers()
            self.huidig_s.Show(False)
            self.scherm2.Show(True)
            self.huidig_s = self.scherm2
        self.Layout()
    # self.scherm1.start.GetValue() self.scherm2.posities.SetLabel(posities)

    def find_primers(self):
        input_sequence = self.scherm1.text.GetValue()
        start = int(self.scherm1.start.GetValue())
        stop = int(self.scherm1.stop.GetValue())
        primers = {}
        sequence = ""
        for x in range(0,start):
            sequence += input_sequence[x]
            if (start-x > 16):
                #print(str(start-x))
                primers = self.search_primer(x, (start-x), input_sequence, primers)
        for x in range(stop,len(input_sequence)):
            sequence += input_sequence[x]
            if ((len(input_sequence)- x) > 16): 
                primers = self.search_primer(x, (len(input_sequence)- x), input_sequence, primers)
        # dictionary -> start and stop gebruiken als keys.
            
        print(primers)
        #print(sequence)
        #return sequence
    
    def search_primer(self, x, difference, input_sequence, primer_list):
        temp = 0
        gc_val = 0
        primer = ""
        max_val = self.max_value(x, difference)
        for y in range(x,max_val): # minimal 17 max 25
            qualified, temp, primer, gc_val = self.build_primers(temp, gc_val, primer, input_sequence[y])
            if (temp > 54 and temp < 61) \
            and (len(primer)> 16 and len(primer) < 26) \
            and ((gc_val/len(primer) >= 0.5) and (gc_val/len(primer) <= 0.6 )) \
            and qualified == 1 :
                if not x in primer_list:
                    primer_list[x] = [(str(primer) + " " + str(temp) + " " + str("%.0f" % (gc_val/len(primer)*100)))]
                else:
                #print(str(primer) + str(temp) + str("%.0f" % (gc_val/len(primer)*100)))
                    primer_list[x].append(str(primer) + " " + str(temp) + " " + str("%.0f" % (gc_val/len(primer)*100)))
        return primer_list

    def build_primers(self, temp, gc_val, primer, y):
        qualified = 0
        if temp < 57 :
            if (y == 'G' or y == 'C'):
                temp += 4
                gc_val += 1
                primer += y
                qualified = 1
        if temp < 59 :
            if (y == 'A' or y == 'T'):
                temp += 2
                primer += y
                qualified = 1
        return qualified, temp, primer, gc_val
    
    def max_value(self, x, difference):
        max_val = 0
        if difference > 25:
            max_val = x + 25
        else :
            max_val = x + difference
        return max_val

if __name__ == "__main__":
    app = wx.App()
    Schermpje(None, -1, "Primerprogram" )
    app.MainLoop()
