# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:26:59 2016

@author: Yingqing Zhou
"""

import wx
import urllib2
import re
import sys


class mystockgui(wx.Frame):
    def __init__(self, parent, title, stocklist):        
        wx.Frame.__init__(self, parent, title=title, size=(400,600))        
        panel = wx.Panel(self, -1)
        
        self.stocklist = stocklist
        
        self.index = 0
        
        self.listCtrl = wx.ListCtrl(panel, size=(400,500), style=wx.LC_REPORT)
        self.listCtrl.InsertColumn(0, 'Code', width=80)
        self.listCtrl.InsertColumn(1, 'Company', width=200)
        self.listCtrl.InsertColumn(2, 'Last Trade', width=120)
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.fillList()
        
        self.CreateStatusBar()            
        filemenu = self.showmenu()
        
        
        self.Show(True)
    
    def showmenu(self):
        # menu
        filemenu = wx.Menu()
        fileItem = filemenu.Append(wx.ID_ABOUT, "&About", "Information about his program")
        filemenu.AppendSeparator()
        exitItem = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")
        
        # create the menuba
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)     
        
        # set events
        self.Bind(wx.EVT_MENU, self.OnAbout, fileItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        
        return filemenu

    def OnAbout(self, event):
        dlg = wx.MessageDialog( self, "A small Don Jones Industrial stock tool in Python", "About myStockGui", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() 
        
    def OnExit(self, event):
        self.Close(True)
    
    def fillList(self):
        
        for item in self.stocklist:
            self.listCtrl.InsertStringItem(self.index, item[0])
            self.listCtrl.SetStringItem(self.index, 1, item[1])
            self.listCtrl.SetStringItem(self.index, 2, item[2])            
            
            
            if self.index % 2:
                self.listCtrl.SetItemBackgroundColour(self.index, "white")
            else:
                self.listCtrl.SetItemBackgroundColour(self.index, "blue")
            self.index += 1
    
    def onItemSelected(self, event):
        currentItem = event.m_itemIndex
        #stock = self.listCtrl.GetItemData(currentItem)
        print currentItem
        
if __name__=='__main__':
    dBytes = urllib2.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
    #print dBytes
    m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b><span id="[a-z0-9_]*">(.*?)</span></b>.*?</tr>',  dBytes)#dStr)
    if m:
        print(m)
    else: 
        print ('Cannot fetch data')
        sys.exit(1)
        
    app = wx.App(False)    
    frame = mystockgui(None, "Don Jones Industrial Stock Tool", m)        
    app.MainLoop()

