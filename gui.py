import stock_price as sp
import wx
import wx.xrc


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.mainpanel = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.codetext2 = wx.StaticText(self.mainpanel, wx.ID_ANY, u"Hello !", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext2.Wrap(-1)

        self.codetext2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                       "Cascadia Mono SemiBold"))

        bSizer11.Add(self.codetext2, 0, wx.ALL, 5)

        bSizer10.Add(bSizer11, 1, wx.EXPAND, 5)

        wSizer14 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext22 = wx.StaticText(self.mainpanel, wx.ID_ANY, u"Today is : ", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.codetext22.Wrap(-1)

        self.codetext22.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                        "Cascadia Mono SemiBold"))

        wSizer14.Add(self.codetext22, 0, wx.ALL, 5)

        self.maintime = wx.StaticText(self.mainpanel, wx.ID_ANY, u"WED 09/11/2022", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.maintime.Wrap(-1)

        self.maintime.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        wSizer14.Add(self.maintime, 0, wx.ALL, 5)

        bSizer10.Add(wSizer14, 1, wx.EXPAND, 5)

        bSizer31.Add(bSizer10, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)

        wSizer18 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext42 = wx.StaticText(self.mainpanel, wx.ID_ANY, u"Account Value", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.codetext42.Wrap(-1)

        self.codetext42.SetFont(
            wx.Font(18, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cascadia Mono"))
        self.codetext42.SetForegroundColour(wx.Colour(98, 103, 117))

        wSizer18.Add(self.codetext42, 0, wx.ALL, 5)

        gSizer1.Add(wSizer18, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.codetext421 = wx.StaticText(self.mainpanel, wx.ID_ANY, u"Today's Change", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.codetext421.Wrap(-1)

        self.codetext421.SetFont(
            wx.Font(18, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cascadia Mono"))
        self.codetext421.SetForegroundColour(wx.Colour(98, 103, 117))

        bSizer9.Add(self.codetext421, 0, wx.ALL, 5)

        gSizer1.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer31.Add(gSizer1, 1, wx.EXPAND, 5)

        gSizer11 = wx.GridSizer(0, 2, 0, 0)

        fgSizer11 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.accountvalue = wx.StaticText(self.mainpanel, wx.ID_ANY, u"3067.80", wx.DefaultPosition, wx.DefaultSize, 0)
        self.accountvalue.Wrap(-1)

        self.accountvalue.SetFont(wx.Font(36, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                          "Cascadia Mono SemiBold"))

        fgSizer11.Add(self.accountvalue, 0, wx.ALL, 5)

        gSizer11.Add(fgSizer11, 1, wx.EXPAND, 5)

        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.todayshange = wx.StaticText(self.mainpanel, wx.ID_ANY, u"  +30.21 (1.00%)", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.todayshange.Wrap(-1)

        self.todayshange.SetFont(
            wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))
        self.todayshange.SetForegroundColour(wx.Colour(0, 255, 0))

        fgSizer21.Add(self.todayshange, 0, wx.ALL, 5)

        gSizer11.Add(fgSizer21, 1, wx.EXPAND, 5)

        bSizer31.Add(gSizer11, 1, wx.EXPAND, 5)

        self.mainpanel.SetSizer(bSizer31)
        self.mainpanel.Layout()
        bSizer31.Fit(self.mainpanel)
        self.m_notebook2.AddPage(self.mainpanel, u"Overview", False)
        self.m_panel2 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Stock Code : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext.Wrap(-1)

        self.codetext.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        wSizer1.Add(self.codetext, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(85, -1), 0)
        wSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self.m_panel2, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        bSizer3.Add(wSizer1, 1, wx.EXPAND, 5)

        wSizer2 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext1 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Reference : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext1.Wrap(-1)

        self.codetext1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                       "Cascadia Mono SemiBold"))

        wSizer2.Add(self.codetext1, 0, wx.ALL, 5)

        self.orderref = wx.StaticText(self.m_panel2, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.orderref.Wrap(-1)

        self.orderref.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        wSizer2.Add(self.orderref, 0, wx.ALL, 5)

        bSizer3.Add(wSizer2, 1, wx.EXPAND, 5)

        wSizer3 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_textCtrl21 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                        0)
        wSizer3.Add(self.m_textCtrl21, 0, wx.ALL, 5)

        self.codetext12 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Shares at ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext12.Wrap(-1)

        self.codetext12.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                        "Cascadia Mono SemiBold"))

        wSizer3.Add(self.codetext12, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1), 0)
        wSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self.m_panel2, wx.ID_ANY, u"Evaluate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer3.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer3.Add(wSizer3, 1, wx.EXPAND, 5)

        wSizer6 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext13 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Total : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext13.Wrap(-1)

        self.codetext13.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                        "Cascadia Mono SemiBold"))

        wSizer6.Add(self.codetext13, 0, wx.ALL, 5)

        self.codetext131 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext131.Wrap(-1)

        self.codetext131.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        wSizer6.Add(self.codetext131, 0, wx.ALL, 5)

        self.codetext1311 = wx.StaticText(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.codetext1311.Wrap(-1)

        self.codetext1311.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                          "Cascadia Mono SemiBold"))

        wSizer6.Add(self.codetext1311, 0, wx.ALL, 5)

        self.m_button21 = wx.Button(self.m_panel2, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button21.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer6.Add(self.m_button21, 0, wx.ALL, 5)

        bSizer3.Add(wSizer6, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        self.m_notebook2.AddPage(self.m_panel2, u"Order", False)
        self.m_panel21 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer32 = wx.BoxSizer(wx.VERTICAL)

        wSizer12 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext3 = wx.StaticText(self.m_panel21, wx.ID_ANY, u"Stock Code : ", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        self.codetext3.Wrap(-1)

        self.codetext3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                       "Cascadia Mono SemiBold"))

        wSizer12.Add(self.codetext3, 0, wx.ALL, 5)

        self.m_textCtrl22 = wx.TextCtrl(self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(90, -1),
                                        0)
        wSizer12.Add(self.m_textCtrl22, 0, wx.ALL, 5)

        self.sellsearchbut = wx.Button(self.m_panel21, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sellsearchbut.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer12.Add(self.sellsearchbut, 0, wx.ALL, 5)

        bSizer32.Add(wSizer12, 1, wx.EXPAND, 5)

        wSizer21 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext14 = wx.StaticText(self.m_panel21, wx.ID_ANY, u"Reference : ", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.codetext14.Wrap(-1)

        self.codetext14.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                        "Cascadia Mono SemiBold"))

        wSizer21.Add(self.codetext14, 0, wx.ALL, 5)

        self.sellreftext = wx.StaticText(self.m_panel21, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sellreftext.Wrap(-1)

        self.sellreftext.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        wSizer21.Add(self.sellreftext, 0, wx.ALL, 5)

        bSizer32.Add(wSizer21, 1, wx.EXPAND, 5)

        wSizer31 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_textCtrl211 = wx.TextCtrl(self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                         0)
        wSizer31.Add(self.m_textCtrl211, 0, wx.ALL, 5)

        self.codetext121 = wx.StaticText(self.m_panel21, wx.ID_ANY, u"Shares   Stock:", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.codetext121.Wrap(-1)

        self.codetext121.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        wSizer31.Add(self.codetext121, 0, wx.ALL, 5)

        self.stockamount = wx.StaticText(self.m_panel21, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stockamount.Wrap(-1)

        self.stockamount.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        wSizer31.Add(self.stockamount, 0, wx.ALL, 5)

        self.totalsell1 = wx.StaticText(self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.totalsell1.Wrap(-1)

        self.totalsell1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                        "Cascadia Mono SemiBold"))

        wSizer31.Add(self.totalsell1, 0, wx.ALL, 5)

        self.m_button22 = wx.Button(self.m_panel21, wx.ID_ANY, u"Estimate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button22.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer31.Add(self.m_button22, 0, wx.ALL, 5)

        bSizer32.Add(wSizer31, 1, wx.EXPAND, 5)

        wSizer61 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.codetext135 = wx.StaticText(self.m_panel21, wx.ID_ANY, u"Total : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext135.Wrap(-1)

        self.codetext135.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        wSizer61.Add(self.codetext135, 0, wx.ALL, 5)

        self.totalsell = wx.StaticText(self.m_panel21, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.totalsell.Wrap(-1)

        self.totalsell.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                       "Cascadia Mono SemiBold"))

        wSizer61.Add(self.totalsell, 0, wx.ALL, 5)

        self.yy = wx.StaticText(self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.yy.Wrap(-1)

        self.yy.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                "Cascadia Mono SemiBold"))

        wSizer61.Add(self.yy, 0, wx.ALL, 5)

        self.m_button212 = wx.Button(self.m_panel21, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button212.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer61.Add(self.m_button212, 0, wx.ALL, 5)

        bSizer32.Add(wSizer61, 1, wx.EXPAND, 5)

        self.m_panel21.SetSizer(bSizer32)
        self.m_panel21.Layout()
        bSizer32.Fit(self.m_panel21)
        self.m_notebook2.AddPage(self.m_panel21, u"Sell", True)
        self.m_scrolledWindow4 = wx.ScrolledWindow(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow4.SetScrollRate(5, 5)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.watchlisttime = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"2022/11/19     22:25:30",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.watchlisttime.Wrap(-1)

        self.watchlisttime.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                           "Cascadia Mono SemiBold"))

        gbSizer1.Add(self.watchlisttime, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText49 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText49.Wrap(-1)

        gbSizer1.Add(self.m_staticText49, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.watchlistrefresh = wx.Button(self.m_scrolledWindow4, wx.ID_ANY, u"Refresh", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.watchlistrefresh.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        gbSizer1.Add(self.watchlistrefresh, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer4.Add(gbSizer1, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.codetext133 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"Ticker", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.codetext133.Wrap(-1)

        self.codetext133.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        gSizer4.Add(self.codetext133, 0, wx.ALL, 5)

        self.codetext134 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"Price", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.codetext134.Wrap(-1)

        self.codetext134.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        gSizer4.Add(self.codetext134, 0, wx.ALL, 5)

        gSizer3.Add(gSizer4, 1, wx.EXPAND, 5)

        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        self.codetext136 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"Change", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.codetext136.Wrap(-1)

        self.codetext136.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        gSizer5.Add(self.codetext136, 0, wx.ALL, 5)

        self.codetext137 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codetext137.Wrap(-1)

        self.codetext137.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                         "Cascadia Mono SemiBold"))

        gSizer5.Add(self.codetext137, 0, wx.ALL, 5)

        gSizer3.Add(gSizer5, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer3, 1, wx.EXPAND, 5)

        gSizer31 = wx.GridSizer(0, 2, 0, 0)

        gSizer41 = wx.GridSizer(0, 2, 0, 0)

        self.wltik1 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"AAPL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wltik1.Wrap(-1)

        self.wltik1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                    "Cascadia Mono SemiBold"))

        gSizer41.Add(self.wltik1, 0, wx.ALL, 5)

        self.wl1 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"139.80", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl1.Wrap(-1)

        self.wl1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer41.Add(self.wl1, 0, wx.ALL, 5)

        gSizer31.Add(gSizer41, 1, wx.EXPAND, 5)

        gSizer51 = wx.GridSizer(0, 2, 0, 0)

        self.wl2 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"+2.36", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl2.Wrap(-1)

        self.wl2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer51.Add(self.wl2, 0, wx.ALL, 5)

        self.wl3 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl3.Wrap(-1)

        self.wl3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer51.Add(self.wl3, 0, wx.ALL, 5)

        gSizer31.Add(gSizer51, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer31, 1, wx.EXPAND, 5)

        gSizer32 = wx.GridSizer(0, 2, 0, 0)

        gSizer42 = wx.GridSizer(0, 2, 0, 0)

        self.wltik2 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"AMD", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wltik2.Wrap(-1)

        self.wltik2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                    "Cascadia Mono SemiBold"))

        gSizer42.Add(self.wltik2, 0, wx.ALL, 5)

        self.wl4 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"250.30", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl4.Wrap(-1)

        self.wl4.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer42.Add(self.wl4, 0, wx.ALL, 5)

        gSizer32.Add(gSizer42, 1, wx.EXPAND, 5)

        gSizer52 = wx.GridSizer(0, 2, 0, 0)

        self.wl5 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"-5.14", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl5.Wrap(-1)

        self.wl5.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer52.Add(self.wl5, 0, wx.ALL, 5)

        self.wl6 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl6.Wrap(-1)

        self.wl6.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer52.Add(self.wl6, 0, wx.ALL, 5)

        gSizer32.Add(gSizer52, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer32, 1, wx.EXPAND, 5)

        gSizer33 = wx.GridSizer(0, 2, 0, 0)

        gSizer43 = wx.GridSizer(0, 2, 0, 0)

        self.wltik3 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"GOOG", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wltik3.Wrap(-1)

        self.wltik3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                    "Cascadia Mono SemiBold"))

        gSizer43.Add(self.wltik3, 0, wx.ALL, 5)

        self.wl7 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"99.37", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl7.Wrap(-1)

        self.wl7.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer43.Add(self.wl7, 0, wx.ALL, 5)

        gSizer33.Add(gSizer43, 1, wx.EXPAND, 5)

        gSizer53 = wx.GridSizer(0, 2, 0, 0)

        self.wl8 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"+0.74", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl8.Wrap(-1)

        self.wl8.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer53.Add(self.wl8, 0, wx.ALL, 5)

        self.wl9 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl9.Wrap(-1)

        self.wl9.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                 "Cascadia Mono SemiBold"))

        gSizer53.Add(self.wl9, 0, wx.ALL, 5)

        gSizer33.Add(gSizer53, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer33, 1, wx.EXPAND, 5)

        gSizer34 = wx.GridSizer(0, 2, 0, 0)

        gSizer44 = wx.GridSizer(0, 2, 0, 0)

        self.wltik4 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"MSFT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wltik4.Wrap(-1)

        self.wltik4.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                    "Cascadia Mono SemiBold"))

        gSizer44.Add(self.wltik4, 0, wx.ALL, 5)

        self.wl10 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"123.5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl10.Wrap(-1)

        self.wl10.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                  "Cascadia Mono SemiBold"))

        gSizer44.Add(self.wl10, 0, wx.ALL, 5)

        gSizer34.Add(gSizer44, 1, wx.EXPAND, 5)

        gSizer54 = wx.GridSizer(0, 2, 0, 0)

        self.wl11 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"+6.56", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl11.Wrap(-1)

        self.wl11.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                  "Cascadia Mono SemiBold"))

        gSizer54.Add(self.wl11, 0, wx.ALL, 5)

        self.wl12 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl12.Wrap(-1)

        self.wl12.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                  "Cascadia Mono SemiBold"))

        gSizer54.Add(self.wl12, 0, wx.ALL, 5)

        gSizer34.Add(gSizer54, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer34, 1, wx.EXPAND, 5)

        gSizer35 = wx.GridSizer(0, 2, 0, 0)

        gSizer45 = wx.GridSizer(0, 2, 0, 0)

        self.wltik5 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"SPY", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wltik5.Wrap(-1)

        self.wltik5.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                    "Cascadia Mono SemiBold"))

        gSizer45.Add(self.wltik5, 0, wx.ALL, 5)

        self.wl13 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"382.00", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl13.Wrap(-1)

        self.wl13.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                  "Cascadia Mono SemiBold"))

        gSizer45.Add(self.wl13, 0, wx.ALL, 5)

        gSizer35.Add(gSizer45, 1, wx.EXPAND, 5)

        gSizer55 = wx.GridSizer(0, 2, 0, 0)

        self.wl14 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"Change", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl14.Wrap(-1)

        self.wl14.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                  "Cascadia Mono SemiBold"))

        gSizer55.Add(self.wl14, 0, wx.ALL, 5)

        self.wl15 = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wl15.Wrap(-1)

        self.wl15.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                  "Cascadia Mono SemiBold"))

        gSizer55.Add(self.wl15, 0, wx.ALL, 5)

        gSizer35.Add(gSizer55, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer35, 1, wx.EXPAND, 5)

        wSizer7 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.chantext = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"Change", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.chantext.Wrap(-1)

        self.chantext.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        wSizer7.Add(self.chantext, 0, wx.ALL, 5)

        self.watchlisttik = wx.TextCtrl(self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(90, -1), 0)
        wSizer7.Add(self.watchlisttik, 0, wx.ALL, 3)

        self.intotext = wx.StaticText(self.m_scrolledWindow4, wx.ID_ANY, u"into", wx.DefaultPosition, wx.DefaultSize, 0)
        self.intotext.Wrap(-1)

        self.intotext.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        wSizer7.Add(self.intotext, 0, wx.ALL, 5)

        self.watchlistqty = wx.TextCtrl(self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(90, -1), 0)
        wSizer7.Add(self.watchlistqty, 0, wx.ALL, 5)

        self.posapplybut = wx.Button(self.m_scrolledWindow4, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posapplybut.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        wSizer7.Add(self.posapplybut, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(wSizer7, 1, wx.EXPAND, 5)

        self.m_scrolledWindow4.SetSizer(bSizer4)
        self.m_scrolledWindow4.Layout()
        bSizer4.Fit(self.m_scrolledWindow4)
        self.m_notebook2.AddPage(self.m_scrolledWindow4, u"Watchlist", False)
        self.m_scrolledWindow41 = wx.ScrolledWindow(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                    wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow41.SetScrollRate(5, 5)
        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        gbSizer11 = wx.GridBagSizer(0, 0)
        gbSizer11.SetFlexibleDirection(wx.BOTH)
        gbSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.postime = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"2022/11/19     22:25:30", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.postime.Wrap(-1)

        self.postime.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gbSizer11.Add(self.postime, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText491 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText491.Wrap(-1)

        gbSizer11.Add(self.m_staticText491, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.posrefreshbut = wx.Button(self.m_scrolledWindow41, wx.ID_ANY, u"Refresh", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.posrefreshbut.SetFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cascadia Mono"))

        gbSizer11.Add(self.posrefreshbut, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer41.Add(gbSizer11, 1, wx.EXPAND, 5)

        gSizer36 = wx.GridSizer(0, 2, 0, 0)

        gSizer46 = wx.GridSizer(0, 2, 0, 0)

        self.codetext1331 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"Ticker", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.codetext1331.Wrap(-1)

        self.codetext1331.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                          "Cascadia Mono SemiBold"))

        gSizer46.Add(self.codetext1331, 0, wx.ALL, 5)

        self.codetext1341 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"Cost", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.codetext1341.Wrap(-1)

        self.codetext1341.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                          "Cascadia Mono SemiBold"))

        gSizer46.Add(self.codetext1341, 0, wx.ALL, 5)

        gSizer36.Add(gSizer46, 1, wx.EXPAND, 5)

        gSizer56 = wx.GridSizer(0, 2, 0, 0)

        self.codetext1361 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"Qty", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.codetext1361.Wrap(-1)

        self.codetext1361.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                          "Cascadia Mono SemiBold"))

        gSizer56.Add(self.codetext1361, 0, wx.ALL, 5)

        self.codetext1376 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"Market", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.codetext1376.Wrap(-1)

        self.codetext1376.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                          "Cascadia Mono SemiBold"))

        gSizer56.Add(self.codetext1376, 0, wx.ALL, 5)

        gSizer36.Add(gSizer56, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer36, 1, wx.EXPAND, 5)

        gSizer311 = wx.GridSizer(0, 2, 0, 0)

        gSizer411 = wx.GridSizer(0, 2, 0, 0)

        self.postik1 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik1.Wrap(-1)

        self.postik1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer411.Add(self.postik1, 0, wx.ALL, 5)

        self.poscost1 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost1.Wrap(-1)

        self.poscost1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer411.Add(self.poscost1, 0, wx.ALL, 5)

        gSizer311.Add(gSizer411, 1, wx.EXPAND, 5)

        gSizer511 = wx.GridSizer(0, 2, 0, 0)

        self.posqty1 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty1.Wrap(-1)

        self.posqty1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer511.Add(self.posqty1, 0, wx.ALL, 5)

        self.posmark1 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark1.Wrap(-1)

        self.posmark1.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer511.Add(self.posmark1, 0, wx.ALL, 5)

        gSizer311.Add(gSizer511, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer311, 1, wx.EXPAND, 5)

        gSizer321 = wx.GridSizer(0, 2, 0, 0)

        gSizer421 = wx.GridSizer(0, 2, 0, 0)

        self.postik2 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik2.Wrap(-1)

        self.postik2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer421.Add(self.postik2, 0, wx.ALL, 5)

        self.poscost2 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost2.Wrap(-1)

        self.poscost2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer421.Add(self.poscost2, 0, wx.ALL, 5)

        gSizer321.Add(gSizer421, 1, wx.EXPAND, 5)

        gSizer521 = wx.GridSizer(0, 2, 0, 0)

        self.posqty2 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty2.Wrap(-1)

        self.posqty2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer521.Add(self.posqty2, 0, wx.ALL, 5)

        self.posmark2 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark2.Wrap(-1)

        self.posmark2.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer521.Add(self.posmark2, 0, wx.ALL, 5)

        gSizer321.Add(gSizer521, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer321, 1, wx.EXPAND, 5)

        gSizer331 = wx.GridSizer(0, 2, 0, 0)

        gSizer431 = wx.GridSizer(0, 2, 0, 0)

        self.postik3 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik3.Wrap(-1)

        self.postik3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer431.Add(self.postik3, 0, wx.ALL, 5)

        self.poscost3 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost3.Wrap(-1)

        self.poscost3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer431.Add(self.poscost3, 0, wx.ALL, 5)

        gSizer331.Add(gSizer431, 1, wx.EXPAND, 5)

        gSizer531 = wx.GridSizer(0, 2, 0, 0)

        self.posqty3 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty3.Wrap(-1)

        self.posqty3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer531.Add(self.posqty3, 0, wx.ALL, 5)

        self.posmark3 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark3.Wrap(-1)

        self.posmark3.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer531.Add(self.posmark3, 0, wx.ALL, 5)

        gSizer331.Add(gSizer531, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer331, 1, wx.EXPAND, 5)

        gSizer341 = wx.GridSizer(0, 2, 0, 0)

        gSizer441 = wx.GridSizer(0, 2, 0, 0)

        self.postik4 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik4.Wrap(-1)

        self.postik4.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer441.Add(self.postik4, 0, wx.ALL, 5)

        self.poscost4 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost4.Wrap(-1)

        self.poscost4.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer441.Add(self.poscost4, 0, wx.ALL, 5)

        gSizer341.Add(gSizer441, 1, wx.EXPAND, 5)

        gSizer541 = wx.GridSizer(0, 2, 0, 0)

        self.posqty4 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty4.Wrap(-1)

        self.posqty4.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer541.Add(self.posqty4, 0, wx.ALL, 5)

        self.posmark4 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark4.Wrap(-1)

        self.posmark4.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer541.Add(self.posmark4, 0, wx.ALL, 5)

        gSizer341.Add(gSizer541, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer341, 1, wx.EXPAND, 5)

        gSizer351 = wx.GridSizer(0, 2, 0, 0)

        gSizer451 = wx.GridSizer(0, 2, 0, 0)

        self.postik5 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik5.Wrap(-1)

        self.postik5.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer451.Add(self.postik5, 0, wx.ALL, 5)

        self.poscost5 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost5.Wrap(-1)

        self.poscost5.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer451.Add(self.poscost5, 0, wx.ALL, 5)

        gSizer351.Add(gSizer451, 1, wx.EXPAND, 5)

        gSizer551 = wx.GridSizer(0, 2, 0, 0)

        self.posqty5 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty5.Wrap(-1)

        self.posqty5.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer551.Add(self.posqty5, 0, wx.ALL, 5)

        self.posmark5 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark5.Wrap(-1)

        self.posmark5.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer551.Add(self.posmark5, 0, wx.ALL, 5)

        gSizer351.Add(gSizer551, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer351, 1, wx.EXPAND, 5)

        gSizer361 = wx.GridSizer(0, 2, 0, 0)

        gSizer461 = wx.GridSizer(0, 2, 0, 0)

        self.postik6 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik6.Wrap(-1)

        self.postik6.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer461.Add(self.postik6, 0, wx.ALL, 5)

        self.poscost6 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost6.Wrap(-1)

        self.poscost6.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer461.Add(self.poscost6, 0, wx.ALL, 5)

        gSizer361.Add(gSizer461, 1, wx.EXPAND, 5)

        gSizer561 = wx.GridSizer(0, 2, 0, 0)

        self.posqty6 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty6.Wrap(-1)

        self.posqty6.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer561.Add(self.posqty6, 0, wx.ALL, 5)

        self.posmark6 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark6.Wrap(-1)

        self.posmark6.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer561.Add(self.posmark6, 0, wx.ALL, 5)

        gSizer361.Add(gSizer561, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer361, 1, wx.EXPAND, 5)

        gSizer362 = wx.GridSizer(0, 2, 0, 0)

        gSizer462 = wx.GridSizer(0, 2, 0, 0)

        self.postik7 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik7.Wrap(-1)

        self.postik7.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer462.Add(self.postik7, 0, wx.ALL, 5)

        self.poscost7 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost7.Wrap(-1)

        self.poscost7.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer462.Add(self.poscost7, 0, wx.ALL, 5)

        gSizer362.Add(gSizer462, 1, wx.EXPAND, 5)

        gSizer562 = wx.GridSizer(0, 2, 0, 0)

        self.posqty7 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty7.Wrap(-1)

        self.posqty7.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer562.Add(self.posqty7, 0, wx.ALL, 5)

        self.posmark7 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark7.Wrap(-1)

        self.posmark7.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer562.Add(self.posmark7, 0, wx.ALL, 5)

        gSizer362.Add(gSizer562, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer362, 1, wx.EXPAND, 5)

        gSizer363 = wx.GridSizer(0, 2, 0, 0)

        gSizer463 = wx.GridSizer(0, 2, 0, 0)

        self.postik8 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik8.Wrap(-1)

        self.postik8.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer463.Add(self.postik8, 0, wx.ALL, 5)

        self.poscost8 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost8.Wrap(-1)

        self.poscost8.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer463.Add(self.poscost8, 0, wx.ALL, 5)

        gSizer363.Add(gSizer463, 1, wx.EXPAND, 5)

        gSizer563 = wx.GridSizer(0, 2, 0, 0)

        self.posqty8 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty8.Wrap(-1)

        self.posqty8.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer563.Add(self.posqty8, 0, wx.ALL, 5)

        self.posmark8 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark8.Wrap(-1)

        self.posmark8.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer563.Add(self.posmark8, 0, wx.ALL, 5)

        gSizer363.Add(gSizer563, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer363, 1, wx.EXPAND, 5)

        gSizer364 = wx.GridSizer(0, 2, 0, 0)

        gSizer464 = wx.GridSizer(0, 2, 0, 0)

        self.postik9 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0)
        self.postik9.Wrap(-1)

        self.postik9.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer464.Add(self.postik9, 0, wx.ALL, 5)

        self.poscost9 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.poscost9.Wrap(-1)

        self.poscost9.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer464.Add(self.poscost9, 0, wx.ALL, 5)

        gSizer364.Add(gSizer464, 1, wx.EXPAND, 5)

        gSizer564 = wx.GridSizer(0, 2, 0, 0)

        self.posqty9 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty9.Wrap(-1)

        self.posqty9.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                     "Cascadia Mono SemiBold"))

        gSizer564.Add(self.posqty9, 0, wx.ALL, 5)

        self.posmark9 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.posmark9.Wrap(-1)

        self.posmark9.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer564.Add(self.posmark9, 0, wx.ALL, 5)

        gSizer364.Add(gSizer564, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer364, 1, wx.EXPAND, 5)

        gSizer365 = wx.GridSizer(0, 2, 0, 0)

        gSizer465 = wx.GridSizer(0, 2, 0, 0)

        self.postik10 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.postik10.Wrap(-1)

        self.postik10.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer465.Add(self.postik10, 0, wx.ALL, 5)

        self.poscost10 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        self.poscost10.Wrap(-1)

        self.poscost10.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                       "Cascadia Mono SemiBold"))

        gSizer465.Add(self.poscost10, 0, wx.ALL, 5)

        gSizer365.Add(gSizer465, 1, wx.EXPAND, 5)

        gSizer565 = wx.GridSizer(0, 2, 0, 0)

        self.posqty10 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.posqty10.Wrap(-1)

        self.posqty10.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                      "Cascadia Mono SemiBold"))

        gSizer565.Add(self.posqty10, 0, wx.ALL, 5)

        self.posmark10 = wx.StaticText(self.m_scrolledWindow41, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        self.posmark10.Wrap(-1)

        self.posmark10.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False,
                                       "Cascadia Mono SemiBold"))

        gSizer565.Add(self.posmark10, 0, wx.ALL, 5)

        gSizer365.Add(gSizer565, 1, wx.EXPAND, 5)

        bSizer41.Add(gSizer365, 1, wx.EXPAND, 5)

        self.m_scrolledWindow41.SetSizer(bSizer41)
        self.m_scrolledWindow41.Layout()
        bSizer41.Fit(self.m_scrolledWindow41)
        self.m_notebook2.AddPage(self.m_scrolledWindow41, u"Position", False)

        bSizer2.Add(self.m_notebook2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)
        self.sellsearchbut.Bind(wx.EVT_BUTTON, self.sellsearch)
        self.m_button22.Bind(wx.EVT_BUTTON, self.sellest)
        self.m_button212.Bind(wx.EVT_BUTTON, self.sellconfirm)
        self.m_button1.Bind(wx.EVT_BUTTON, self.orderprev)
        self.m_button2.Bind(wx.EVT_BUTTON, self.ordereval)
        self.m_button21.Bind(wx.EVT_BUTTON, self.orderconfirm)
        self.watchlistrefresh.Bind(wx.EVT_BUTTON, self.wlrefresh)
        self.posrefreshbut.Bind(wx.EVT_BUTTON, self.posrefresh)
        self.posapplybut.Bind(wx.EVT_BUTTON, self.applybut)

    def __del__(self):
        pass

    def initpane(self, event):
        stik = sp.get_ticker()
        postik = sp.get_pos_ticker()
        posavg = sp.get_pos_price()
        posqty = sp.get_pos_qty()
        sres = sp.search_price(stik)
        frm.wltik1.Label = stik[0].replace('\'', '')
        frm.wltik2.Label = stik[1].replace('\'', '')
        frm.wltik3.Label = stik[2].replace('\'', '')
        frm.wltik4.Label = stik[3].replace('\'', '')
        frm.wltik5.Label = stik[4].replace('\'', '')
        frm.wl1.Label = sres[0]
        frm.wl2.Label = sres[1]
        frm.wl3.Label = sres[2]
        frm.wl4.Label = sres[3]
        frm.wl5.Label = sres[4]
        frm.wl6.Label = sres[5]
        frm.wl7.Label = sres[6]
        frm.wl8.Label = sres[7]
        frm.wl9.Label = sres[8]
        frm.wl10.Label = sres[9]
        frm.wl11.Label = sres[10]
        frm.wl12.Label = sres[11]
        frm.wl13.Label = sres[12]
        frm.wl14.Label = sres[13]
        frm.wl15.Label = sres[14]
        if len(postik) >= 1:
            frm.postik1.Label = postik[0].replace('\'', '')
            frm.poscost1.Label = str(posavg[0])
            frm.posqty1.Label = str(posqty[0])
            frm.posmark1.Label = str(sp.get_price(postik[0]))
        if len(postik) >= 2:
            frm.postik2.Label = postik[1].replace('\'', '')
            frm.poscost2.Label = str(posavg[1])
            frm.posqty2.Label = str(posqty[1])
            frm.posmark2.Label = str(sp.get_price(postik[1]))
        if len(postik) >= 3:
            frm.postik3.Label = postik[2].replace('\'', '')
            frm.poscost3.Label = str(posavg[2])
            frm.posqty3.Label = str(posqty[2])
            frm.posmark3.Label = str(sp.get_price(postik[2]))
        if len(postik) >= 4:
            frm.postik4.Label = postik[3].replace('\'', '')
            frm.poscost4.Label = str(posavg[3])
            frm.posqty4.Label = str(posqty[3])
            frm.posmark4.Label = str(sp.get_price(postik[3]))
        if len(postik) >= 5:
            frm.postik5.Label = postik[4].replace('\'', '')
            frm.poscost5.Label = str(posavg[4])
            frm.posqty5.Label = str(posqty[4])
            frm.posmark5.Label = str(sp.get_price(postik[4]))
        if len(postik) >= 6:
            frm.postik6.Label = postik[5].replace('\'', '')
            frm.poscost6.Label = str(posavg[5])
            frm.posqty6.Label = str(posqty[5])
            frm.posmark6.Label = str(sp.get_price(postik[5]))
        if len(postik) >= 7:
            frm.postik7.Label = postik[6].replace('\'', '')
            frm.poscost7.Label = str(posavg[6])
            frm.posqty7.Label = str(posqty[6])
            frm.posmark7.Label = str(sp.get_price(postik[6]))
        if len(postik) >= 8:
            frm.postik8.Label = postik[7].replace('\'', '')
            frm.poscost8.Label = str(posavg[7])
            frm.posqty8.Label = str(posqty[7])
            frm.posmark8.Label = str(sp.get_price(postik[7]))
        if len(postik) >= 9:
            frm.postik9.Label = postik[8].replace('\'', '')
            frm.poscost9.Label = str(posavg[8])
            frm.posqty9.Label = str(posqty[8])
            frm.posmark9.Label = str(sp.get_price(postik[8]))
        if len(postik) >= 10:
            frm.postik10.Label = postik[9].replace('\'', '')
            frm.poscost10.Label = str(posavg[9])
            frm.posqty10.Label = str(posqty[9])
            frm.posmark10.Label = str(sp.get_price(postik[9]))
        if float(sres[1]) > 0:
            frm.wl2.SetForegroundColour((0, 255, 0))
            frm.wl3.SetForegroundColour((0, 255, 0))
        else:
            frm.wl2.ForegroundColour = (255, 0, 0)
            frm.wl3.ForegroundColour = (255, 0, 0)
        if float(sres[4]) > 0:
            frm.wl5.SetForegroundColour((0, 255, 0))
            frm.wl6.SetForegroundColour((0, 255, 0))
        else:
            frm.wl5.SetForegroundColour((255, 0, 0))
            frm.wl6.SetForegroundColour((255, 0, 0))
        if float(sres[7]) > 0:
            frm.wl8.SetForegroundColour((0, 255, 0))
            frm.wl9.SetForegroundColour((0, 255, 0))
        else:
            frm.wl8.SetForegroundColour((255, 0, 0))
            frm.wl9.SetForegroundColour((255, 0, 0))
        if float(sres[10]) > 0:
            frm.wl11.SetForegroundColour((0, 255, 0))
            frm.wl12.SetForegroundColour((0, 255, 0))
        else:
            frm.wl11.SetForegroundColour((255, 0, 0))
            frm.wl12.SetForegroundColour((255, 0, 0))
        if float(sres[13]) > 0:
            frm.wl14.SetForegroundColour((0, 255, 0))
            frm.wl15.SetForegroundColour((0, 255, 0))
        else:
            frm.wl14.SetForegroundColour((255, 0, 0))
            frm.wl15.SetForegroundColour((255, 0, 0))
        frm.accountvalue.Label = str(round(sum(sp.total_val(postik, posqty)), 2))
        frm.todayshange.Label = str(round(sum(sp.search_gap(postik, posqty)), 2))
        if float(frm.todayshange.Label) > 0:
            frm.todayshange.SetForegroundColour((0, 255, 0))
        else:
            frm.todayshange.SetForegroundColour((255, 0, 0))
        frm.watchlisttime.Label = sp.get_time()
        frm.postime.Label = sp.get_time()
        frm.maintime.Label = sp.getdate()

    def sellsearch(self, event):
        frm.stockamount.Label = str(sp.ser(f"{frm.m_textCtrl22.Value}"))
        frm.sellreftext.Label = str(sp.get_price(f"'{frm.m_textCtrl22.Value}'"))

    def sellest(self, event):
        frm.totalsell.Label = str(float(frm.sellreftext.Label) * float(frm.m_textCtrl211.Value))

    def sellconfirm(self, event):
        sp.sell(str(f"{frm.m_textCtrl22.Value}"), float(frm.sellreftext.Label), float(frm.m_textCtrl211.Value))
        frm.sellreftext.Label = "0.0"
        frm.totalsell.Label = "0.0"
        frm.m_textCtrl22.Value = ""
        frm.m_textCtrl211.Value = ""

    def orderprev(self, event):
        frm.orderref.Label = str(sp.get_price(f"'{frm.m_textCtrl2.Value}'"))

    def ordereval(self, event):
        frm.codetext131.Label = str(float(frm.m_textCtrl21.Value) * float(frm.m_textCtrl3.Value))

    def orderconfirm(self, event):
        sp.ord(str(f"{frm.m_textCtrl2.Value}"), float(frm.m_textCtrl3.Value), float(frm.m_textCtrl21.Value))
        frm.codetext131.Label = "0.0"
        frm.orderref.Label = "0.0"
        frm.m_textCtrl3.Value = ""
        frm.m_textCtrl2.Value = ""
        frm.m_textCtrl21.Value = ""

    def applybut(self, event):
        sp.changetik(f"{frm.watchlisttik.Value}", f"{frm.watchlistqty.Value}")
        frm.watchlisttik.Value = ""
        frm.watchlistqty.Value = ""
        self.wlrefresh(None)

    def wlrefresh(self, event):
        stik = sp.get_ticker()
        sres = sp.search_price(stik)
        frm.wltik1.Label = stik[0].replace('\'', '')
        frm.wltik2.Label = stik[1].replace('\'', '')
        frm.wltik3.Label = stik[2].replace('\'', '')
        frm.wltik4.Label = stik[3].replace('\'', '')
        frm.wltik5.Label = stik[4].replace('\'', '')
        frm.wl1.Label = sres[0]
        frm.wl2.Label = sres[1]
        frm.wl3.Label = sres[2]
        frm.wl4.Label = sres[3]
        frm.wl5.Label = sres[4]
        frm.wl6.Label = sres[5]
        frm.wl7.Label = sres[6]
        frm.wl8.Label = sres[7]
        frm.wl9.Label = sres[8]
        frm.wl10.Label = sres[9]
        frm.wl11.Label = sres[10]
        frm.wl12.Label = sres[11]
        frm.wl13.Label = sres[12]
        frm.wl14.Label = sres[13]
        frm.wl15.Label = sres[14]
        frm.watchlisttime.Label = sp.get_time()
        if float(sres[1]) > 0:
            frm.wl2.SetForegroundColour((0, 255, 0))
            frm.wl3.SetForegroundColour((0, 255, 0))
        else:
            frm.wl2.ForegroundColour = (255, 0, 0)
            frm.wl3.ForegroundColour = (255, 0, 0)
        if float(sres[4]) > 0:
            frm.wl5.SetForegroundColour((0, 255, 0))
            frm.wl6.SetForegroundColour((0, 255, 0))
        else:
            frm.wl5.SetForegroundColour((255, 0, 0))
            frm.wl6.SetForegroundColour((255, 0, 0))
        if float(sres[7]) > 0:
            frm.wl8.SetForegroundColour((0, 255, 0))
            frm.wl9.SetForegroundColour((0, 255, 0))
        else:
            frm.wl8.SetForegroundColour((255, 0, 0))
            frm.wl9.SetForegroundColour((255, 0, 0))
        if float(sres[10]) > 0:
            frm.wl11.SetForegroundColour((0, 255, 0))
            frm.wl12.SetForegroundColour((0, 255, 0))
        else:
            frm.wl11.SetForegroundColour((255, 0, 0))
            frm.wl12.SetForegroundColour((255, 0, 0))
        if float(sres[13]) > 0:
            frm.wl14.SetForegroundColour((0, 255, 0))
            frm.wl15.SetForegroundColour((0, 255, 0))
        else:
            frm.wl14.SetForegroundColour((255, 0, 0))
            frm.wl15.SetForegroundColour((255, 0, 0))

    def posrefresh(self, event):
        postik = sp.get_pos_ticker()
        posavg = sp.get_pos_price()
        posqty = sp.get_pos_qty()
        if len(postik) >= 1:
            frm.postik1.Label = postik[0].replace('\'', '')
            frm.poscost1.Label = str(posavg[0])
            frm.posqty1.Label = str(posqty[0])
            frm.posmark1.Label = str(sp.get_price(postik[0]))
        if len(postik) >= 2:
            frm.postik2.Label = postik[1].replace('\'', '')
            frm.poscost2.Label = str(posavg[1])
            frm.posqty2.Label = str(posqty[1])
            frm.posmark2.Label = str(sp.get_price(postik[1]))
        if len(postik) >= 3:
            frm.postik3.Label = postik[2].replace('\'', '')
            frm.poscost3.Label = str(posavg[2])
            frm.posqty3.Label = str(posqty[2])
            frm.posmark3.Label = str(sp.get_price(postik[2]))
        if len(postik) >= 4:
            frm.postik4.Label = postik[3].replace('\'', '')
            frm.poscost4.Label = str(posavg[3])
            frm.posqty4.Label = str(posqty[3])
            frm.posmark4.Label = str(sp.get_price(postik[3]))
        if len(postik) >= 5:
            frm.postik5.Label = postik[4].replace('\'', '')
            frm.poscost5.Label = str(posavg[4])
            frm.posqty5.Label = str(posqty[4])
            frm.posmark5.Label = str(sp.get_price(postik[4]))
        if len(postik) >= 6:
            frm.postik6.Label = postik[5].replace('\'', '')
            frm.poscost6.Label = str(posavg[5])
            frm.posqty6.Label = str(posqty[5])
            frm.posmark6.Label = str(sp.get_price(postik[5]))
        if len(postik) >= 7:
            frm.postik7.Label = postik[6].replace('\'', '')
            frm.poscost7.Label = str(posavg[6])
            frm.posqty7.Label = str(posqty[6])
            frm.posmark7.Label = str(sp.get_price(postik[6]))
        if len(postik) >= 8:
            frm.postik8.Label = postik[7].replace('\'', '')
            frm.poscost8.Label = str(posavg[7])
            frm.posqty8.Label = str(posqty[7])
            frm.posmark8.Label = str(sp.get_price(postik[7]))
        if len(postik) >= 9:
            frm.postik9.Label = postik[8].replace('\'', '')
            frm.poscost9.Label = str(posavg[8])
            frm.posqty9.Label = str(posqty[8])
            frm.posmark9.Label = str(sp.get_price(postik[8]))
        if len(postik) >= 10:
            frm.postik10.Label = postik[9].replace('\'', '')
            frm.poscost10.Label = str(posavg[9])
            frm.posqty10.Label = str(posqty[9])
            frm.posmark10.Label = str(sp.get_price(postik[9]))
        frm.accountvalue.Label = str(round(sum(sp.total_val(postik, posqty)), 2))
        frm.todayshange.Label = str(round(sum(sp.search_gap(postik, posqty)), 2))
        frm.watchlisttime.Label = sp.get_time()
        frm.postime.Label = sp.get_time()
        frm.maintime.Label = sp.getdate()


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame1(None)
    frm.Show()
    frm.initpane(None)
    app.MainLoop()
