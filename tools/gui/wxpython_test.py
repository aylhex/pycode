#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/9/8

import sys
import wx

########################################################################
class MyFrame(wx.Frame):
    """we simply derive a new class of frame"""

    #----------------------------------------------------------------------
    def __init__(self,parent,title):
        """Constructor"""
        wx.Frame.__init__(self,parent,title=title,size=(500,300))
        self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.Show(True)
        
        
    
    
#----------------------------------------------------------------------
def main():
    """"""
    app=wx.App(False)
    frame=MyFrame(None,"hello world")
    app.MainLoop()

if __name__=='__main__':
    main()
    
    