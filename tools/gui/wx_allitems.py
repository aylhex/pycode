#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/9/18

import sys
import wx
########################################################################
class myMenu(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self,None,-1,'My Frame',size=(500,300))
        menubar=wx.MenuBar()
        menu_file=wx.Menu()
        menu_edit=wx.Menu()
        menu_help=wx.Menu()
        submenu_edit=wx.Menu()
        #menu_file
        menu_file.Append(101,'&Open','Open a new document')
        menu_file.Append(102,'&Save','Save the document')
        menu_file.AppendSeparator()
        #menu_edit
        menu_edit.Append(201,'check item1','',wx.ITEM_CHECK)
        menu_edit.Append(202,'check item2','',kind=wx.ITEM_CHECK)
        menu_edit.AppendMenu(203,'submenu',submenu_edit)
        #submenu
        submenu_edit.Append(301,'radio item 1',kind=wx.ITEM_RADIO)
        submenu_edit.Append(302,'radio item 2',kind=wx.ITEM_RADIO)
        submenu_edit.Append(303,'radio item 3',kind=wx.ITEM_RADIO)
        #menu_help
        menu_help.Append(401,'&exit','sss')
        #menubar
        menubar.Append(menu_file,'&file')
        menubar.Append(menu_edit,'&edit')
        menubar.Append(menu_help,'&help')
        self.SetMenuBar(menubar)
        #panel
        panel=wx.Panel(self,-1)
        panel.Bind(wx.EVT_MOTION,self.onMove)
        wx.StaticText(panel,-1,"Pos:",pos=(10,12))
        self.posCtrl=wx.TextCtrl(panel,-1,"",pos=(40,10))
        #frame
        self.Center()
        
        wx.EVT_MENU(self,401,self.OnQuit)
    def onMove(self,event):
        pos=event.GetPosition()
        self.posCtrl.SetValue("%s,%s"%(pos.x,pos.y))
    def OnQuit(self,event):
        self.Close()
########################################################################
class myToolBar(wx.Frame):
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 350, 250 ) )  
        wx.Frame.__init__(self,None,-1,'MyFrame.py',size=(500,300))
        vbox = wx.BoxSizer( wx.VERTICAL )  
        toolbar = wx.ToolBar( self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER )  
        toolbar.AddSimpleTool( 1, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'New', '' )  
        toolbar.AddSimpleTool( 2, wx.Image( 'stock_open.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Open', '' )  
        toolbar.AddSimpleTool( 3, wx.Image( 'stock_save.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Save', '' )  
        toolbar.AddSeparator()  
        toolbar.AddSimpleTool( 4, wx.Image( 'stock_exit.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Exit', '' )  
        toolbar.Realize()  
          
        vbox.Add( toolbar, 0, border=5 )  
        self.SetSizer( vbox )  
        self.statusbar = self.CreateStatusBar()  
          
        self.Centre()  
          
        wx.EVT_TOOL( self, 1, self.OnNew )  
        wx.EVT_TOOL( self, 2, self.OnOpen )  
        wx.EVT_TOOL( self, 3, self.OnSave )  
        wx.EVT_TOOL( self, 4, self.OnExit )
        
    def OnNew( self, event ):  
        self.statusbar.SetStatusText( 'New Command' )  
      
    def OnOpen( self, event ):  
        self.statusbar.SetStatusText( 'Open Command' )  
      
    def OnSave( self, event ):  
        self.statusbar.SetStatusText( 'Save Command' )  
      
    def OnExit( self, event ):  
        self.Close()  

########################################################################
class myBoxsizer(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self,None,-1,'myboxsizer',(-1,-1),wx.Size(300,150))  
        panel=wx.Panel(self,-1)  
        #box=wx.BoxSizer(wx.HORIZONTAL)
        box=wx.BoxSizer(wx.HORIZONTAL)
        box.Add( wx.Button( panel, -1, 'Button1' ), 1 )  
        box.Add( wx.Button( panel, -1, 'Button2' ), 1 )  
        box.Add( wx.Button( panel, -1, 'Button3' ), 1 )  
          
        panel.SetSizer(box)  
        self.Centre()  
        
    
    
class myApp(wx.App):
    def  OnInit(self):
        #frame=myframe()
        frame=myBoxsizer()
        frame.Show(True)
        return True
if __name__=='__main__':
    app=myApp()
    app.MainLoop()