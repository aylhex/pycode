#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/7/30
#!/usr/bin/env python  
# FileName: calculator.py  
import wx  
class MyFrame( wx.Frame ):  
    def __init__( self, parent, id, title ):  
        wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition,wx.Size(300, 250))  
  
        self.formula = False  
          
        menubar = wx.MenuBar()  
        file = wx.Menu()  
        file.Append( 22, '&Quit', 'Exit Calculator' )  
        menubar.Append( file, '&File' )  
        self.SetMenuBar( menubar )  
          
        wx.EVT_MENU( self, 22, self.OnClose )  
        sizer = wx.BoxSizer( wx.VERTICAL )  
          
        self.display = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT)  
        sizer.Add(self.display, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 4)  
        gs = wx.GridSizer(4, 4, 3, 3)  
        gs.AddMany([(wx.Button(self, 20, 'Cls'), 0, wx.EXPAND),  
        (wx.Button(self, 21, 'Bck'), 0, wx.EXPAND),  
        (wx.StaticText(self, -1, ''), 0, wx.EXPAND),  
        (wx.Button(self, 22, 'Close'), 0, wx.EXPAND),  
        (wx.Button(self, 1, '7'), 0, wx.EXPAND),  
        (wx.Button(self, 2, '8'), 0, wx.EXPAND),  
        (wx.Button(self, 3, '9'), 0, wx.EXPAND),  
        (wx.Button(self, 4, '/'), 0, wx.EXPAND),  
        (wx.Button(self, 5, '4'), 0, wx.EXPAND),  
        (wx.Button(self, 6, '5'), 0, wx.EXPAND),  
        (wx.Button(self, 7, '6'), 0, wx.EXPAND),  
        (wx.Button(self, 8, '*'), 0, wx.EXPAND),  
        (wx.Button(self, 9, '1'), 0, wx.EXPAND),  
        (wx.Button(self, 10, '2'), 0, wx.EXPAND),  
        (wx.Button(self, 11, '3'), 0, wx.EXPAND),  
        (wx.Button(self, 12, '-'), 0, wx.EXPAND),  
        (wx.Button(self, 13, '0'), 0, wx.EXPAND),  
        (wx.Button(self, 14, '.'), 0, wx.EXPAND),  
        (wx.Button(self, 15, '='), 0, wx.EXPAND),  
        (wx.Button(self, 16, '+'), 0, wx.EXPAND)])  
        sizer.Add(gs, 1, wx.EXPAND)  
        self.SetSizer(sizer)  
        self.Centre()  
        wx.EVT_BUTTON(self, 20, self.OnClear)  
        wx.EVT_BUTTON(self, 21, self.OnBackspace)  
        wx.EVT_BUTTON(self, 22, self.OnClose)  
        wx.EVT_BUTTON(self, 1, self.OnSeven)  
        wx.EVT_BUTTON(self, 2, self.OnEight)  
        wx.EVT_BUTTON(self, 3, self.OnNine)  
        wx.EVT_BUTTON(self, 4, self.OnDivide)  
        wx.EVT_BUTTON(self, 5, self.OnFour)  
        wx.EVT_BUTTON(self, 6, self.OnFive)  
        wx.EVT_BUTTON(self, 7, self.OnSix)  
        wx.EVT_BUTTON(self, 8, self.OnMultiply)  
        wx.EVT_BUTTON(self, 9, self.OnOne)  
        wx.EVT_BUTTON(self, 10, self.OnTwo)  
        wx.EVT_BUTTON(self, 11, self.OnThree)  
        wx.EVT_BUTTON(self, 12, self.OnMinus)  
        wx.EVT_BUTTON(self, 13, self.OnZero)  
        wx.EVT_BUTTON(self, 14, self.OnDot)  
        wx.EVT_BUTTON(self, 15, self.OnEqual)  
        wx.EVT_BUTTON(self, 16, self.OnPlus)  
  
    def OnClear(self, event):  
        self.display.Clear()  
    def OnBackspace(self, event):  
        formula = self.display.GetValue()  
        self.display.Clear()  
        self.display.SetValue(formula[:-1])  
    def OnClose(self, event):  
        self.Close()  
    def OnDivide(self, event):  
        if self.formula:  
            return  
        self.display.AppendText('/')  
    def OnMultiply(self, event):  
        if self.formula:  
            return  
        self.display.AppendText('*')  
    def OnMinus(self, event):  
        if self.formula:  
            return  
        self.display.AppendText('-')  
    def OnPlus(self, event):  
        if self.formula:  
            return  
        self.display.AppendText('+')  
    def OnDot(self, event):  
        if self.formula:  
            return  
        self.display.AppendText('.')  
    def OnEqual(self, event):  
        if self.formula:  
            return  
        formula = self.display.GetValue()  
        self.formula = True  
        try:  
            self.display.Clear()  
            output = eval(formula)  
            self.display.AppendText(str(output))  
        except StandardError:  
            self.display.AppendText("Error")  
    def OnZero(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('0')  
    def OnOne(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('1')  
    def OnTwo(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('2')  
    def OnThree(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('3')  
    def OnFour(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('4')  
    def OnFive(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('5')  
    def OnSix(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('6')  
    def OnSeven(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('7')  
    def OnEight(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('8')  
    def OnNine(self, event):  
        if self.formula:  
            self.display.Clear()  
            self.formula = False  
            self.display.AppendText('9')  
      
class MyApp(wx.App):  
        def OnInit(self):  
            frame = MyFrame(None, -1, "calculator.py")  
            frame.Show(True)  
            self.SetTopWindow(frame)  
            return True  
if __name__=='__main__':
    app = MyApp(0)  
    app.MainLoop()
    
    