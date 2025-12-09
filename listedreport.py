import base64

# Logo图标的Base64数据
logo_png = "R0lGODlhMAAwAIAAAP///wAAACH5BAEAAAEALAAAAAAwADAAAgjuAAMIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKHUu2rNmzaNOqXcu2rdu3cOPKnUu3rt27ePPq3cu3r9+/gAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk27tu3buHPr3s27t+/fwIMLH068uPHjyJMrX868ufPn0KMHBAA7"
import os
import time
import requests
import pandas as pd
from tkinter import *
import tkinter.ttk
import ttkbootstrap as tkb
from datetime import datetime
with open(r'logo.png', 'wb') as w:
    w.write(base64.b64decode(logo_png))
orgid_url = 'http://www.cninfo.com.cn/new/data/szse_stock.json'
orgid_resp = requests.get(orgid_url)
orgid_resp_stock = orgid_resp.json()['stockList']
df_orgid = pd.DataFrame(orgid_resp_stock)
class tk_cnifo:
    def __init__(self):
        self.root = tkb.Window(themename='sandstone')
        self.back_color = '#FAFAFA'
        self.root['bg'] = self.back_color
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.orgin_factor = 1.6683087027914612
        self.scaling_factor = self.orgin_factor/self.root.tk.call('tk', 'scaling')
        self.width = 1200
        self.height =750
        self.text_size16 = int(16*self.scaling_factor)
        self.text_size14 = int(14*self.scaling_factor)
        self.text_size13 = int(13*self.scaling_factor)
        self.text_size12 = int(12*self.scaling_factor)
        self.text_size10 = int(10*self.scaling_factor)


        begin_h = (self.screenheight-self.height)/2
        self.begin_height = begin_h*4/5
        self.begin_width = (self.screenwidth-self.width)/2
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.begin_width, self.begin_height))
        self.root.update()
        self.root.title("Report Crawler")
        self.scaling_factor = self.root.tk.call('tk', 'scaling')
        self.root_height = self.root.winfo_height()
        self.root_width = self.root.winfo_width()
        print(self.scaling_factor)
        self.photo = PhotoImage(data = logo_png)
        self.adjust_font_size()
        self.class_color = "white"
        self.wl_color = "#424242"
        self.which_menu = 0
        self.default_color = self.root.cget("bg")
        self.frame_bo_def()
        self.frame_menu_def()
        self.frame_title_def()
        self.frame_normal_def()
        self.frame_check_var = self.one_code_frame_check_get(self)
        self.frame_one_code_def()
        self.frame_report_def()
        self.frame_more_code_def()
        self.frame_message_def()
        self.root.mainloop()


    def adjust_font_size(self):
        self.root_height =self.root.winfo_height()
        self.root_width = self.root.winfo_width()
        print(self.root_height,self.root_width)
        # font_size = int(height * 0.1)  # 根据窗口高度的10%来设置字体大小
        # custom_font.configure(size=font_size)
        # label.config(font=custom_font)
    def back_color_fix(self,fix_list):
        for fix in fix_list:
            fix['bg'] = self.back_color
    def frame_bo_def(self):
        self.frame_bo = tkb.Frame(self.root,bootstyle = 'primary',height = 24)
        bo_wl = tkb.Label(self.frame_bo,text = "Report Crawler 1.0",font = ("Times",self.text_size10,"bold"),bootstyle = 'inverse-primary',anchor = W)
        bo_wl.pack(anchor = CENTER,padx =30)
        self.frame_bo.pack(side = BOTTOM,fill = 'x')
        self.frame_bo.pack_propagate(0)
    def menu_delete_color(self):
        self.menu_bt0["bg"] = "white"
        self.menu_bt1["bg"] = "white"
        self.menu_bt2["bg"] = "white"
        self.menu_bt3["bg"] = "white"
        self.menu_bt4["bg"] = "white"
        self.menu_bt0["activebackground"] = self.back_color
        self.menu_bt1["activebackground"] = self.back_color
        self.menu_bt2["activebackground"] = self.back_color
        self.menu_bt3["activebackground"] = self.back_color
        self.menu_bt4["activebackground"] = self.back_color
    def frame_forget(self):
        self.frame_report.pack_forget()
        self.frame_normal.pack_forget()
        self.frame_one_code.pack_forget()
        self.frame_more_code.pack_forget()
        self.frame_message.pack_forget()
    def menu_botton0(self):
        self.menu_delete_color()
        self.menu_bt0["bg"] = self.back_color
        self.frame_forget()
        self.frame_normal.pack()
        self.which_menu = 0
    def menu_botton1(self):
        self.menu_delete_color()
        self.menu_bt1["bg"] = self.back_color
        self.frame_forget()
        self.frame_one_code.pack()
        self.which_menu = 1
    def menu_botton2(self):
        self.menu_delete_color()
        self.frame_forget()
        self.menu_bt2["bg"] = self.back_color
        self.frame_report.pack()
        self.which_menu = 2
    def menu_botton3(self):
        self.menu_delete_color()
        self.frame_forget()
        self.menu_bt3["bg"] = self.back_color
        self.frame_more_code.pack()
        self.which_menu = 3
    def menu_botton4(self):
        self.menu_delete_color()
        self.frame_forget()
        self.menu_bt4["bg"] = self.back_color
        self.frame_message.pack()
        self.which_menu = 0
    def frame_menu_def(self):
        self.frame_menu= Frame(self.root, width = int(250),bg = 'white')
        self.menu_bt0 = Button(self.frame_menu,text = "首页",font = ("宋体",self.text_size14,"bold"),bd = 0,anchor = W,padx =15,command = self.menu_botton0)
        self.menu_bt0.pack(fill = 'x',ipady = 15)
        self.menu_bt1 = Button(self.frame_menu,text = "单股报告批量下载",font = ("宋体",self.text_size14,"bold"),bd = 0,anchor = W,padx =15,command = self.menu_botton1)
        self.menu_bt1.pack(ipady = 15,fill = 'x')
        self.menu_bt2 = Button(self.frame_menu,text = "定期报告批量下载",font = ("宋体",self.text_size14,"bold"),bd = 0,anchor = W,padx =15,command = self.menu_botton2)
        self.menu_bt2.pack(ipady = 15,fill = 'x')
        self.menu_bt3 = Button(self.frame_menu,text = "多股报告批量下载",font = ("宋体",self.text_size14,"bold"),bd = 0,anchor = W,padx =15,command = self.menu_botton3)
        self.menu_bt3.pack(ipady = 15,fill = 'x')
        self.menu_bt4 = Button(self.frame_menu,text = "说明&设置",font = ("宋体",self.text_size14,"bold"),bd = 0,anchor = W,padx =15,command = self.menu_botton4)
        self.menu_bt4.pack(ipady = 15,fill = 'x')
        self.menu_delete_color()
        self.menu_bt0["bg"] = '#FAFAFA'
        self.menu_bt0["fg"] = "black"
        self.menu_bt1["fg"] = "black"
        self.menu_bt2["fg"] = "black"
        self.menu_bt3["fg"] = "black"
        self.menu_bt4["fg"] = "black"
        sep_frame = Frame(self.frame_menu,height = 2)
        sep_frame.pack(fill = 'x')
        sep_frame['bg'] = "#A4A4A4"
        self.frame_menu.pack(side = LEFT,fill = "y")
        self.frame_menu.pack_propagate(0)
    def frame_title_def(self):
        self.frame_title = Frame(self.root)
        self.frame_title['bg'] = self.back_color
        wp = Label(self.frame_title,image = self.photo)
        wp.pack(side = LEFT,pady = 10,padx = (0,25))
        wp['bg'] = self.back_color
        frame_title_wl = Frame(self.frame_title)
        frame_title_wl['bg'] = self.back_color
        wl_title1 = Label(frame_title_wl,text = "Report Download | Windows  ",font = ("Times",22,"bold"))
        wl_title1.pack(side = LEFT,pady = 10,anchor = S)
        wl_title2 = Label(frame_title_wl,text = "v 1.0 ",font = ("Times",18,""))
        wl_title2.pack(side = LEFT,padx = 15,anchor = S)
        wl_title1['bg'] = self.back_color
        wl_title2['bg'] = self.back_color
        frame_title_wl.pack(side = LEFT,pady = 10,padx = (25,0))
        self.frame_title.pack(pady = 0)
    def frame_normal_def(self):
        self.frame_normal = Frame(self.root, width=850, height=600)
        n_wl1 = Label(self.frame_normal,text = "欢迎来到 Report Crawler 1.0 !!",font = ("times",self.text_size16,'bold'),fg = "#735943")
        n_wl1.pack()
        n_wl1['fg'] = "#735943"
        n_wl2 = Label(self.frame_normal,text = "本程序具有多种批量下载功能，可选择如下几种方法~",font = ("宋体",self.text_size16,'bold'),fg = "#735943")
        n_wl2.pack(pady = (10,15))
        n_wl2['fg'] = "#735943"
        class_frame = Frame(self.frame_normal)

        # 第1个功能的介绍
        class_wl2 = Label(class_frame,text = "单股报告批量下载",font = ("宋体",self.text_size14,"bold"))
        class_wl2.pack(anchor = W,pady = (5,6))
        class_2_frame = Frame(class_frame,width = 600,height = 80)
        class_2_wl_frame = Frame(class_2_frame)
        class_2_wl1 = Label(class_2_wl_frame,text = " 支持单一股票报告的批量下载",font = ("仿宋",self.text_size13,))
        class_2_wl1.pack(anchor = W,pady = (5,8))
        class_2_wl2 = Label(class_2_wl_frame,text = " 可筛选板块、时间、报告类型等条件后批量下载多个公司的报告",font = ("仿宋",self.text_size13,))
        class_2_wl2.pack(anchor = W)
        class_2_wl_frame.pack(side = LEFT,pady  = 5)
        class_2_frame.pack(fill = X,anchor = W,padx = 25,pady  = 5)
        class_2_frame.pack_propagate(0)

        # 第2个功能的介绍
        class_wl1 = Label(class_frame, text="定期报告批量下载", font=("宋体", self.text_size14, "bold"), )
        class_wl1.pack(anchor=W, pady=(15, 6))
        class_1_frame = Frame(class_frame, width=750, height=80)
        class_1_wl_frame = Frame(class_1_frame, )
        class_1_wl1 = Label(class_1_wl_frame, text=" 支持季报、半年报和年报的批量下载", font=("仿宋", self.text_size13,))
        class_1_wl1.pack(anchor=W, pady=(5, 8))
        class_1_wl2 = Label(class_1_wl_frame, text=" 可筛选板块、时间等条件后批量下载多个公司的定期报告", font=("仿宋", self.text_size13,))
        class_1_wl2.pack(anchor=W)
        class_1_wl_frame.pack(side=LEFT)
        class_1_frame.pack(fill=X, anchor=W, padx=25)
        class_1_frame.pack_propagate(0)

        # 第三个功能的介绍
        class_wl3 = Label(class_frame,text = "多股报告批量下载",font = ("宋体",self.text_size14,"bold"))
        class_wl3.pack(anchor = W,pady = (15,6))
        class_3_frame = Frame(class_frame,width = 600,height = 80)
        class_3_wl_frame = Frame(class_3_frame)
        class_3_wl1 = Label(class_3_wl_frame,text = " 支持多个股票报告的批量下载",font = ("仿宋",self.text_size13,))
        class_3_wl1.pack(anchor = W,pady = (5,8))
        class_3_wl2 = Label(class_3_wl_frame,text = " 上传/输入股票代码，筛选时间等条件后批量下载多个公司的报告",font = ("仿宋",self.text_size13,))
        class_3_wl2.pack(anchor = W)
        class_3_wl_frame.pack(side = LEFT)
        class_3_frame.pack(fill = X,anchor = W,padx = 25,pady = 5)
        class_3_frame.pack_propagate(0)
        # 第四个功能的介绍
        class_frame.pack(anchor = W,padx = (15,0))
        n_wl3 = Label(self.frame_normal, text="请选择左侧对应功能开始吧！！", font=("times", self.text_size16, 'bold'))
        n_wl3.pack(side = BOTTOM)
        n_wl3['fg'] ="#735943"
        self.back_color_fix([self.frame_normal,class_frame,n_wl1,n_wl2,n_wl3,class_wl1,class_wl2,class_wl3])
        self.frame_normal.pack()
        self.frame_normal.pack_propagate(0)
    def frame_one_code_def(self):
        self.frame_one_code = Frame(self.root, width=820, height=610)
        r_wl1 = Label(self.frame_one_code, text="您已打开单股公告批量下载 part !", font=("宋体", self.text_size16, 'bold'), fg="#735943")
        r_wl1.pack(pady=(5, 25))
        r_wl1['fg'] = '#735943'
        self.sktcd_frame = Frame(self.frame_one_code)
        sk_c_wl = Label(self.sktcd_frame, text="股票代码输入(必填 | 输入股票代码并点击确认)", font=("宋体", self.text_size14, "bold"),
                      fg=self.wl_color)
        sk_c_wl.pack(anchor=W, pady=(0, 6), padx=(10, 10))
        sk_sktcd_1_frame = Frame(self.sktcd_frame)
        sk_sktcd_1_frame['bg'] = self.back_color
        sk_sktcd_wl_1 = Label(sk_sktcd_1_frame, text="股票代码:", font=("仿宋", self.text_size13, "bold"), fg=self.wl_color)
        sk_sktcd_wl_1.pack(side=LEFT, anchor=W, pady=3, padx=(80, 10))
        self.sk_sktcd_one_entry = Entry(sk_sktcd_1_frame, width=45, font=("Times", self.text_size13, ""), bg="white")
        self.sk_sktcd_one_entry.pack(side=LEFT, pady=3)
        sk_sktcd_1_button = Button(sk_sktcd_1_frame, text='确定', font=("仿宋", self.text_size12, ""), command = self.frame_check_var.code_check_one_mode)
        sk_sktcd_1_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        sk_sktcd_1_frame.pack(anchor=W, fill=X, pady=(0, 5))
        self.sktcd_frame.pack(fill="x",pady = (0,10))

        self.search_key_frame = Frame(self.frame_one_code)
        sk_s_wl = Label(self.search_key_frame, text="您可输入搜索关键词（非必填 | 多个关键词用空格隔开）", font=("宋体", self.text_size14, "bold"),
                      fg=self.wl_color)
        sk_s_wl.pack(anchor=W, pady=(0, 6), padx=(10, 10))
        sk_search_key_frame = Frame(self.search_key_frame)
        sk_search_key_wl = Label(sk_search_key_frame, text="关键词:  ", font=("仿宋", self.text_size13, "bold"), fg=self.wl_color)
        sk_search_key_wl.pack(side=LEFT, anchor=W, pady=3, padx=(80, 10))
        self.sk_search_key_entry = Entry(sk_search_key_frame, width=45, font=("Times", self.text_size13, ""), bg="white")
        self.sk_search_key_entry.pack(side=LEFT, pady=3)
        sk_search_key_1_button = Button(sk_search_key_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.keyword_check)
        sk_search_key_1_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        sk_search_key_frame.pack(anchor=W, fill=X, pady=(0, 5))
        self.search_key_frame.pack(fill="x")

        self.report_type_frame = Frame(self.frame_one_code)
        self.report_type_frame['bg'] = self.back_color
        sk_r_wl = Label(self.report_type_frame, text="报告类型(非必填 | 若未选择，默认为全选)", font=("宋体", self.text_size14, "bold"))
        sk_r_wl.pack(anchor=W, pady=(15, 6), padx=(10, 10))
        choice_type_frame = Frame(self.report_type_frame)

        report_type_list = ["年报", "半年报", "一季度报", "三季度报",'其他']
        choice_wl = Label(choice_type_frame, text="请选择： ", font=("仿宋", self.text_size13, 'bold'),)
        choice_wl.pack(side=LEFT, padx=(80, 2))
        self.report_type_vlist_one = []
        for r_type in report_type_list:
            self.report_type_vlist_one.append(StringVar())
            check_buttion = Checkbutton(choice_type_frame, text=r_type, variable=self.report_type_vlist_one[-1], onvalue=r_type, offvalue='',
                                        font=("仿宋", self.text_size12),)
            check_buttion['bg'] = self.back_color
            check_buttion.pack(side=LEFT, padx=(0, 10))
        choice_button = Button(choice_type_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.report_type_check)
        choice_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        choice_type_frame.pack(fill=X)
        self.report_type_frame.pack(fill=X)

        self.year_frame = Frame(self.frame_one_code)
        time_wl = Label(self.year_frame, text="时间选择(必填 | 若未选择，默认为2024年)", font=("宋体", self.text_size14, "bold"),)
        time_wl.pack(anchor=W, pady=(15, 6), padx=(10, 10))
        year_choice_frame = Frame(self.year_frame)
        b_year_choice_frame = Frame(year_choice_frame)
        begindate_wl = Label(b_year_choice_frame, text="起始日期:", font=("仿宋", self.text_size13, 'bold'), )
        begindate_wl.pack(side=LEFT, padx=(80, 2))
        # self.begindate_entry = tkb.DateEntry()
        startdate = datetime.strptime('2024-01-01', '%Y-%m-%d')
        enddate = datetime.strptime('2024-12-31', '%Y-%m-%d')
        self.begindate_entry = tkb.DateEntry(b_year_choice_frame, bootstyle="primary",startdate=startdate,dateformat='%Y-%m-%d')
        self.begindate_entry.pack(side=LEFT, padx=(10, 2))
        tkb.DateEntry()
        e_year_choice_frame = Frame(year_choice_frame)
        enddate_wl = Label(e_year_choice_frame, text="起始日期:", font=("仿宋", self.text_size13, 'bold'), )
        enddate_wl.pack(side=LEFT, padx=(80, 2))
        self.enddate_entry = tkb.DateEntry(e_year_choice_frame, bootstyle="primary",startdate=enddate,dateformat='%Y-%m-%d')
        self.enddate_entry.pack(side=LEFT, padx=(10, 2))

        choice_button = Button(year_choice_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.begin_end_time_check)
        choice_button.pack(side=RIGHT, anchor = SE,pady=3, padx=(0, 20))
        b_year_choice_frame.pack(fill=X,pady = (10,0))
        e_year_choice_frame.pack(fill=X,pady = (10,0))
        year_choice_frame.pack(fill=X)
        self.year_frame.pack(fill=X)
        r_wl2 = Label(self.frame_one_code, text="PS: 以上所有筛选信息，若有选择/输入，必须点击最右的'确定'！！！", font=("仿宋", self.text_size13, 'bold'), fg="#735943")
        r_wl2.pack(pady=(50, 0))
        r_wl2['fg'] = 'red'
        self.back_color_fix(
            [self.frame_one_code, r_wl1, self.sktcd_frame, sk_c_wl, sk_sktcd_1_frame, sk_sktcd_wl_1,
             choice_type_frame, choice_wl, self.report_type_frame, self.year_frame, time_wl, year_choice_frame,
             begindate_wl, enddate_wl, b_year_choice_frame, e_year_choice_frame, year_choice_frame,
             sk_s_wl, sk_search_key_frame, sk_search_key_wl, self.search_key_frame, sk_r_wl,r_wl2])
        finish_frame = Frame(self.frame_one_code)
        frame_more_code_finish_wl = Label(finish_frame, text="完成填写并进行信息确定可进入下一步", font=("宋体", self.text_size14, 'bold'))
        frame_more_code_finish_wl.pack(side=LEFT)
        frame_more_code_finish_wl['bg'] = self.back_color
        frame_more_code_finish_wl['fg'] = '#735943'
        self.frame_more_code_finish_botton = Button(finish_frame, text="下一步", font=("宋体", self.text_size14),command = self.frame_check_var.crawl_window_open)
        self.frame_more_code_finish_botton.pack(side=LEFT, padx=(50, 0))
        finish_frame['bg'] = self.back_color
        finish_frame.pack(side=BOTTOM)
        self.frame_one_code.pack_propagate(0)
        self.frame_one_code.pack_forget()
    def frame_report_def(self):
        self.frame_report = Frame(self.root, width=820, height=610)
        r_wl1 = Label(self.frame_report,text = "您已打开定期报告批量下载 part !",font = ("宋体",self.text_size16,'bold'))
        r_wl1.pack(pady = (5,25))
        r_wl1['fg'] = "#735943"
        self.sktcd_frame = Frame(self.frame_report)
        sk_wl = Label(self.sktcd_frame,text = "股票代码输入/上传(输入一种并点击确认,均未选择默认选择全部股票)",font = ("宋体",self.text_size14,"bold"))
        sk_wl.pack(anchor = W,pady = (0,6),padx = (10,10))
        sk_wl_1 = Label(self.sktcd_frame,text = "(1)可直接输入股票代码(逗号隔开，示例：000001,000002)",font = ("宋体",self.text_size14,"bold"))
        sk_wl_1.pack(anchor = W,pady = (5,5),padx = (25,20))
        sk_sktcd_1_frame = Frame(self.sktcd_frame)
        sk_sktcd_wl_1 = Label(sk_sktcd_1_frame,text = "股票代码:",font = ("仿宋",self.text_size13,"bold"),fg = self.wl_color)
        sk_sktcd_wl_1.pack(side = LEFT,anchor = W,pady = 3,padx = (80,10))
        self.sk_sktcd_entry_report = Entry(sk_sktcd_1_frame,width=45,font = ("Times",self.text_size13,""))
        self.sk_sktcd_entry_report.pack(side = LEFT,pady = 3)
        sk_sktcd_1_button = Button(sk_sktcd_1_frame,text = '确定',font = ("仿宋",self.text_size12,""),command = self.frame_check_var.code_check1)
        sk_sktcd_1_button.pack(side = RIGHT,pady = 3,padx = (0,20))
        sk_sktcd_1_frame.pack(anchor = W,fill = X,pady= (0,5))
        sk_wl_2 = Label(self.sktcd_frame,text = "(2)数量较多可将股票代码放入excel(放在同一列且有列名)",font = ("宋体",self.text_size14,"bold"),fg = self.wl_color)
        sk_wl_2.pack(anchor = W,pady = (5,3),padx = (25,20))
        sk_sktcd_2_frame = Frame(self.sktcd_frame)
        sk_sktcd_wl_2 = Label(sk_sktcd_2_frame,text = "文件路径:",font = ("仿宋",self.text_size13,"bold"))
        sk_sktcd_wl_2.pack(side = LEFT,anchor = W,pady = 3,padx = (80,10))
        self.sk_sktcd_file_entry_report = Entry(sk_sktcd_2_frame,width=24,font = ("Times",self.text_size13,""))
        self.sk_sktcd_file_entry_report.pack(side = LEFT,pady = 3)
        sk_sktcd_wl_3 = Label(sk_sktcd_2_frame,text = "列名:",font = ("仿宋",self.text_size13,"bold"))
        sk_sktcd_wl_3.pack(side = LEFT,anchor = W,pady = 3,padx =(15,10) )
        self.sk_sktcd_columns_entry_report = Entry(sk_sktcd_2_frame,width=12,font = ("Times",self.text_size13,""))
        self.sk_sktcd_columns_entry_report.pack(side = LEFT,pady = 3)
        sk_sktcd_2_button = Button(sk_sktcd_2_frame,text = '确定',font = ("仿宋",self.text_size12,""),command = self.frame_check_var.code_check2)
        sk_sktcd_2_button.pack(side = RIGHT,pady = 3,padx = (0,20))
        sk_sktcd_2_frame.pack(anchor = W,fill = X)
        self.sktcd_frame.pack(fill = "x")
        # sk_wl = Label(report_type_frame,text = "请选择报告类型",font = ("宋体",14,"bold"),fg = self.wl_color)
        # sk_wl.pack(anchor = W,pady = 6,padx = (25,20))
        self.plate_frame = Frame(self.frame_report)
        sk_p_wl = Label(self.plate_frame,text = "股票板块((非必填 | 未选择，默认为全选)",font = ("宋体",self.text_size14,"bold"),fg = self.wl_color)
        sk_p_wl.pack(anchor = W,pady = (15,6),padx = (10,10))
        plate_choice_frame = Frame(self.plate_frame)
        plate_list_r = ["主板[沪]","主板[深]","创业板","科创板","北交所"]
        plate_wl = Label(plate_choice_frame,text = "请选择： ",font = ("仿宋",self.text_size13,'bold'),fg = self.wl_color)
        plate_wl.pack(side = LEFT,padx = (80,2))
        self.plate_vlist_report = []
        for r_type in plate_list_r:
            self.plate_vlist_report.append(StringVar())
            check_buttion = Checkbutton(plate_choice_frame,text = r_type,variable = self.plate_vlist_report[-1],onvalue = r_type,offvalue = "",font = ("仿宋",self.text_size12),fg = self.wl_color)
            check_buttion.pack(side = LEFT,padx = 0)
            check_buttion['bg'] = self.back_color
        plate_button = Button(plate_choice_frame,text = '确定',font = ("仿宋",self.text_size12,""),command = self.frame_check_var.plate_check_report)
        plate_button.pack(side = RIGHT,pady = 3,padx = (0,20))
        plate_choice_frame.pack(fill = X)
        self.plate_frame.pack(fill = "x")

        self.report_type_frame = Frame(self.frame_report)
        sk_t_wl = Label(self.report_type_frame,text = "报告类型(非必填 | 未选择，默认为全选)",font = ("宋体",self.text_size14,"bold"),fg = self.wl_color)
        sk_t_wl.pack(anchor = W,pady = (15,6),padx = (10,10))
        choice_type_frame = Frame(self.report_type_frame)
        report_type_list = ["年报","半年报","一季度报","三季度报"]
        choice_wl = Label(choice_type_frame,text = "请选择： ",font = ("仿宋",self.text_size13,'bold'),fg = self.wl_color)
        choice_wl.pack(side = LEFT,padx = (80,2))
        self.report_type_vlist_report = []
        # check_buttion_year = Checkbutton(choice_type_frame,text = '年报',variable = var_year,onvalue = '年报',offvalue = "")
        for r_type in report_type_list:
            self.report_type_vlist_report.append(StringVar())
            check_buttion = Checkbutton(choice_type_frame,text = r_type,variable = self.report_type_vlist_report[-1],onvalue = r_type,offvalue = "",font = ("仿宋",self.text_size12),fg = self.wl_color)
            check_buttion.pack(side = LEFT,padx = (0,10))
            check_buttion['bg'] =  self.back_color
        choice_button = Button(choice_type_frame,text = '确定',font = ("仿宋",self.text_size12,""),command = self.frame_check_var.report_type_check)
        choice_button.pack(side = RIGHT,pady = 3,padx = (0,20))
        choice_type_frame.pack(fill = X)
        self.report_type_frame.pack(fill = X)

        self.year_frame = Frame(self.frame_report)
        year_list = list(range(2000, 2026))
        time_wl = Label(self.year_frame,text = "时间选择(非必填 | 可输入同一年 | 若未选择，默认为2023年)",font = ("宋体",self.text_size14,"bold"),fg = self.wl_color)
        time_wl.pack(anchor = W,pady = (15,6),padx = (10,10))
        year_choice_frame = Frame(self.year_frame)
        beginyear_wl = Label(year_choice_frame,text = "起始年度:",font = ("仿宋",self.text_size13,'bold'),fg = self.wl_color)
        beginyear_wl.pack(side = LEFT,padx = (80,2))
        current_var_begin = StringVar()
        self.beginyear_combobox = tkinter.ttk.Combobox(year_choice_frame, textvariable=current_var_begin,width = 10)
        self.beginyear_combobox['values'] = year_list
        self.beginyear_combobox.pack(side = LEFT,padx = (10,2))
        to_wl = Label(year_choice_frame,text = "至",font = ("仿宋",self.text_size13,'bold'),fg = self.wl_color)
        to_wl.pack(side = LEFT,padx = (15,0))
        endyear_wl = Label(year_choice_frame,text = "终止年度:",font = ("仿宋",self.text_size13,'bold'),fg = self.wl_color)
        endyear_wl.pack(side = LEFT,padx = (25,2))
        current_var_end = StringVar()
        self.endyear_combobox = tkinter.ttk.Combobox(year_choice_frame, textvariable=current_var_end, width=10)
        self.endyear_combobox['values'] = year_list
        self.endyear_combobox.pack(side=LEFT, padx=(10, 2))
        year_button = Button(year_choice_frame,text = '确定',font = ("仿宋",self.text_size12,""),command = self.frame_check_var.begin_end_time_check)
        year_button.pack(side = RIGHT,pady = 3,padx = (0,20))
        year_choice_frame.pack(fill = X)
        self.year_frame.pack(fill = X)
        r_wl2 = Label(self.frame_report, text="PS: 以上所有筛选信息，若有选择/输入，必须点击最右的'确定'！！", font=("仿宋", self.text_size13, 'bold'), fg="#735943")
        r_wl2.pack(pady=(25, 0))
        r_wl2['fg'] = 'red'
        self.back_color_fix(
            [self.frame_report, r_wl1, self.sktcd_frame, sk_wl, sk_wl_1, sk_sktcd_1_frame, sk_sktcd_wl_1,sk_wl_2,
            sk_sktcd_2_frame, sk_sktcd_wl_2, sk_sktcd_wl_3,self.plate_frame,sk_p_wl,plate_choice_frame,
            plate_wl,sk_t_wl,choice_type_frame,choice_wl,self.report_type_frame,self.year_frame,time_wl,year_choice_frame,
            beginyear_wl,to_wl,r_wl2,endyear_wl,])
        finish_frame = Frame(self.frame_report)
        frame_more_code_finish_wl = Label(finish_frame, text="完成填写并进行信息确定可进入下一步", font=("宋体", self.text_size14, 'bold'))
        frame_more_code_finish_wl.pack(side=LEFT)
        frame_more_code_finish_wl['bg'] = self.back_color
        frame_more_code_finish_wl['fg'] = '#735943'
        frame_more_code_finish_botton = Button(finish_frame, text="下一步", font=("宋体", self.text_size14),command = self.frame_check_var.crawl_window_open)
        frame_more_code_finish_botton.pack(side=LEFT, padx=(50, 0))
        finish_frame['bg'] = self.back_color
        finish_frame.pack(side=BOTTOM)
        self.frame_report.pack_propagate(0)
        self.frame_report.pack_forget()
    def frame_more_code_def(self):
        self.frame_more_code = Frame(self.root, width=820, height=610)
        r_wl1 = Label(self.frame_more_code, text="您已打开多股公告批量下载 part !", font=("宋体", self.text_size16, 'bold'), fg="#735943")
        r_wl1.pack(pady=(5, 25))
        r_wl1['fg'] = '#735943'
        self.sktcd_frame = Frame(self.frame_more_code)
        sk_c_wl = Label(self.sktcd_frame, text="股票代码输入/上传(输入一种并点击确认,均未选择默认选择全部股票)", font=("宋体", self.text_size14, "bold"))
        sk_c_wl.pack(anchor=W, pady=(0, 6), padx=(10, 10))
        sk_wl_1 = Label(self.sktcd_frame, text="(1)可直接输入股票代码(逗号隔开，示例：000001,000002)", font=("宋体", self.text_size14, "bold"))
        sk_wl_1.pack(anchor=W, pady=(5, 5), padx=(25, 20))
        sk_sktcd_1_frame = Frame(self.sktcd_frame)
        sk_sktcd_wl_1 = Label(sk_sktcd_1_frame, text="股票代码:", font=("仿宋", self.text_size13, "bold"), fg=self.wl_color)
        sk_sktcd_wl_1.pack(side=LEFT, anchor=W, pady=3, padx=(80, 10))
        self.sk_sktcd_entry_more = Entry(sk_sktcd_1_frame, width=45, font=("Times", self.text_size13, ""))
        self.sk_sktcd_entry_more.pack(side=LEFT, pady=3)
        sk_sktcd_1_button = Button(sk_sktcd_1_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.code_check1)
        sk_sktcd_1_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        sk_sktcd_1_frame.pack(anchor=W, fill=X, pady=(0, 5))
        sk_wl_2 = Label(self.sktcd_frame, text="(2)数量较多可将股票代码放入excel(放在同一列且有列名)", font=("宋体", self.text_size14, "bold"),
                        fg=self.wl_color)
        sk_wl_2.pack(anchor=W, pady=(5, 3), padx=(25, 20))
        sk_sktcd_2_frame = Frame(self.sktcd_frame)
        sk_sktcd_wl_2 = Label(sk_sktcd_2_frame, text="文件路径:", font=("仿宋", self.text_size13, "bold"))
        sk_sktcd_wl_2.pack(side=LEFT, anchor=W, pady=3, padx=(80, 10))
        self.sk_sktcd_file_entry_more = Entry(sk_sktcd_2_frame, width=24, font=("Times", self.text_size13, ""))
        self.sk_sktcd_file_entry_more.pack(side=LEFT, pady=3)
        sk_sktcd_wl_3 = Label(sk_sktcd_2_frame, text="列名:", font=("仿宋", self.text_size13, "bold"))
        sk_sktcd_wl_3.pack(side=LEFT, anchor=W, pady=3, padx=(15, 10))
        self.sk_sktcd_columns_entry_more = Entry(sk_sktcd_2_frame, width=12, font=("Times", self.text_size13, ""))
        self.sk_sktcd_columns_entry_more.pack(side=LEFT, pady=3)
        sk_sktcd_2_button = Button(sk_sktcd_2_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.code_check2)
        sk_sktcd_2_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        sk_sktcd_2_frame.pack(anchor=W, fill=X)
        self.sktcd_frame.pack(fill="x",pady = (0,10))
        self.search_key_frame = Frame(self.frame_more_code)
        sk_s_wl = Label(self.search_key_frame, text="您可输入搜索关键词（非必填 | 多个关键词用空格隔开）", font=("宋体", self.text_size14, "bold"),
                      fg=self.wl_color)
        sk_s_wl.pack(anchor=W, pady=(0, 6), padx=(10, 10))
        sk_search_key_frame = Frame(self.search_key_frame)
        sk_search_key_wl = Label(sk_search_key_frame, text="关键词:  ", font=("仿宋", self.text_size13, "bold"), fg=self.wl_color)
        sk_search_key_wl.pack(side=LEFT, anchor=W, pady=3, padx=(80, 10))
        self.sk_search_key_entry_more = Entry(sk_search_key_frame, width=45, font=("Times", self.text_size13, ""), bg="white")
        self.sk_search_key_entry_more.pack(side=LEFT, pady=3)
        sk_search_key_1_button = Button(sk_search_key_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.keyword_check)
        sk_search_key_1_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        sk_search_key_frame.pack(anchor=W, fill=X, pady=(0, 5))
        self.search_key_frame.pack(fill="x")
        self.report_type_frame = Frame(self.frame_more_code)
        self.report_type_frame['bg'] = self.back_color
        sk_r_wl = Label(self.report_type_frame, text="报告类型(非必填 | 未选择，默认为全选)", font=("宋体", self.text_size14, "bold"))
        sk_r_wl.pack(anchor=W, pady=(15, 6), padx=(10, 10))
        choice_type_frame = Frame(self.report_type_frame)
        report_type_list = ["年报", "半年报", "一季度报", "三季度报",'其他']
        choice_wl = Label(choice_type_frame, text="请选择： ", font=("仿宋", self.text_size13, 'bold'),)
        choice_wl.pack(side=LEFT, padx=(80, 2))
        self.report_type_vlist_more = []
        for r_type in report_type_list:
            self.report_type_vlist_more.append(StringVar())
            check_buttion = Checkbutton(choice_type_frame, text=r_type, variable=self.report_type_vlist_more[-1], onvalue=r_type, offvalue="",
                                        font=("仿宋", self.text_size12),)
            check_buttion['bg'] = self.back_color
            check_buttion.pack(side=LEFT, padx=(0, 10))
        choice_button = Button(choice_type_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.report_type_check)
        choice_button.pack(side=RIGHT, pady=3, padx=(0, 20))
        choice_type_frame.pack(fill=X)
        self.report_type_frame.pack(fill=X)

        self.year_frame = Frame(self.frame_more_code)
        time_wl = Label(self.year_frame, text="时间选择(非必填 | 若未选择，默认为2024年)", font=("宋体", self.text_size14, "bold"),)
        time_wl.pack(anchor=W, pady=(15, 6), padx=(10, 10))
        year_choice_frame = Frame(self.year_frame)
        b_year_choice_frame = Frame(year_choice_frame)
        beginyear_wl = Label(b_year_choice_frame, text="起始日期:", font=("仿宋", self.text_size13, 'bold'), )
        beginyear_wl.pack(side=LEFT, padx=(80, 2))
        startdate = datetime.strptime('2024-01-01', '%Y-%m-%d')
        enddate = datetime.strptime('2024-12-31', '%Y-%m-%d')
        self.begindate_entry_more = tkb.DateEntry(b_year_choice_frame, bootstyle="primary",width=10,startdate=startdate,dateformat='%Y-%m-%d')
        self.begindate_entry_more.pack(side=LEFT, padx=(15, 2))
        e_year_choice_frame = Frame(year_choice_frame)
        endyear_wl = Label(e_year_choice_frame, text="终止日期:", font=("仿宋", self.text_size13, 'bold'), )
        endyear_wl.pack(side=LEFT, padx=(15, 2))
        self.enddate_entry_more = tkb.DateEntry(e_year_choice_frame, bootstyle="primary",width=10,startdate=enddate,dateformat='%Y-%m-%d')
        self.enddate_entry_more.pack(side=LEFT, padx=(10, 2))

        choice_button = Button(year_choice_frame, text='确定', font=("仿宋", self.text_size12, ""),command = self.frame_check_var.begin_end_time_check)
        choice_button.pack(side=RIGHT, anchor = SE,pady=3, padx=(0, 20))
        b_year_choice_frame.pack(side = LEFT,pady = (10,0),padx = (0,12))
        e_year_choice_frame.pack(side = LEFT,pady = (10,0))
        year_choice_frame.pack(fill=X)
        self.year_frame.pack(fill=X)

        r_wl2 = Label(self.frame_more_code, text="PS: 以上所有筛选信息，若有选择/输入，必须点击最右的'确定'！！！", font=("仿宋", self.text_size13, 'bold'),
                      fg="#735943")
        r_wl2.pack(pady=(20, 0))
        r_wl2['fg'] = 'red'
        self.back_color_fix(
            [self.frame_more_code,self.frame_report, r_wl1, self.sktcd_frame, sk_c_wl, sk_sktcd_1_frame, sk_sktcd_wl_1,self.plate_frame,
             sk_wl_1,sk_wl_2,sk_sktcd_wl_1,sk_sktcd_wl_2,sk_sktcd_wl_3,choice_type_frame, choice_wl, self.report_type_frame,
             self.year_frame, time_wl,year_choice_frame,sk_sktcd_2_frame,beginyear_wl, endyear_wl,b_year_choice_frame,
             e_year_choice_frame,year_choice_frame,endyear_wl,beginyear_wl,sk_s_wl,sk_search_key_frame,sk_search_key_wl,
             self.search_key_frame,sk_r_wl,r_wl2])
        finish_frame = Frame(self.frame_more_code)
        frame_more_code_finish_wl = Label(finish_frame, text="完成填写并进行信息确定可进入下一步", font=("宋体", self.text_size14, 'bold'))
        frame_more_code_finish_wl.pack(side=LEFT)
        frame_more_code_finish_wl['bg'] = self.back_color
        frame_more_code_finish_wl['fg'] = '#735943'
        frame_more_code_finish_botton = Button(finish_frame, text="下一步", font=("宋体", self.text_size14),command = self.frame_check_var.crawl_window_open)
        frame_more_code_finish_botton.pack(side=LEFT, padx=(50, 0))
        finish_frame['bg'] = self.back_color
        finish_frame.pack(side = BOTTOM)

        self.frame_more_code.pack_propagate(0)
        self.frame_more_code.pack_forget()
    def frame_message_def(self):
        self.frame_message = Frame(self.root, width=800, height=610)
        class_frame = Frame(self.frame_message)
        # 第二个功能的介绍
        class_wl2 = Label(class_frame, text="关于", font=("宋体", self.text_size14, "bold"))
        class_wl2.pack(anchor=W, pady=(15, 6))
        class_2_frame = Frame(class_frame, width=800, height=100)
        class_2_wl_frame = Frame(class_2_frame)
        class_2_wl1 = Label(class_2_wl_frame, text=" 本文件本软件仅供学习和研究之用，不得用于非法用途。", font=("仿宋", self.text_size12,))
        class_2_wl1.pack(anchor=W, pady=(1, 6))
        class_2_wl2 = Label(class_2_wl_frame, text=" 用户在使用本软件时必须严格遵守所在国家/地区的法律、法规和政策。", font=("仿宋", self.text_size12,))
        class_2_wl2.pack(anchor=W,pady=(1, 6))
        class_2_wl3 = Label(class_2_wl_frame, text=" 因违反有关法律、法规和政策而导致的任何后果或责任由用户自行承担。",
                            font=("仿宋", self.text_size13,))
        class_2_wl3.pack(anchor=W)
        class_2_wl_frame.pack(side=LEFT)
        class_2_frame.pack(fill=X, anchor=W, padx=25)
        class_2_frame.pack_propagate(0)
        # 第三个功能的介绍
        class_wl3 = Label(class_frame, text="说明", font=("宋体", self.text_size14, "bold"))
        class_wl3.pack(anchor=W, pady=(15, 6))
        class_3_frame = Frame(class_frame, width=600, height=80)
        class_3_wl_frame = Frame(class_3_frame)
        class_3_wl1 = Label(class_3_wl_frame, text=" 下载速度取决于网络状况", font=("仿宋", self.text_size12,))
        class_3_wl1.pack(anchor=W, pady=(1, 6))
        class_3_wl2 = Label(class_3_wl_frame, text=" 目前看来，下载速度较慢，量较大请耐心等待哦", font=("仿宋", self.text_size12,))
        class_3_wl2.pack(anchor=W)
        class_3_wl_frame.pack(side=LEFT)
        class_3_frame.pack(fill=X, anchor=W, padx=25)
        class_3_frame.pack_propagate(0)
        class_frame.pack(anchor=W, padx=(15, 0))
        # class_frame.pack_propagate(0)
        self.back_color_fix(
            [self.frame_message, class_frame, class_wl2, class_wl3])
        self.frame_message.pack_propagate(0)
        self.frame_message.pack_forget()
    def window_quit(self):
        self.root.destroy()
    class one_code_frame_check_get:
        def __init__(self, father):
            self.father = father
            self.mess_get_dict = {
                'plate':[''],
                'stock':[''],
                'searchkey':[''],
                'category': [''],
                'seDate':'2023-01-01~2023-12-31',
            }
            self.result_stock_from_1 = 0
            self.result_stock_from_2 = 0
            self.beginyear = 2023
            self.endyear = 2023
            # self.code_get = self.code_check()
            # self.code_check()
            # self.check_window.mainloop()
        def check_window_open(self,title):
            self.check_window = Toplevel(master=self.father.root)
            self.width = 600
            self.height = 250
            self.begin_height = (self.father.screenheight - self.height) / 2
            self.begin_width = (self.father.screenwidth - self.width) / 2
            self.check_window.geometry('%dx%d+%d+%d' % (self.width, self.height, self.begin_width, self.begin_height))
            self.title_check_label = Label(self.check_window, text=f"{title} 确定窗口",
                                     font=("宋体", 14, "bold"))
            self.title_check_label.pack(pady = (5,10))
            self.check_label = Label(self.check_window, text="",
                                     font=("仿宋", 12, ""))
            self.check_label.pack(pady=(5, 10))
            self.result_label1 = Label(self.check_window, text="",
                                     font=("仿宋", 12, ""))
            self.result_label1.pack(pady=(10, 10))
            self.result_label2 = Label(self.check_window, text="",
                                      font=("仿宋", 12, ""))
            self.result_label2.pack(pady=(0, 10))
            self.check_button = Button(self.check_window, text="",
                                     font=("仿宋", 12, ""),command = self.check_window_close)
            self.check_button.pack(pady=(10,0))
        def check_window_close(self):
            self.check_window.destroy()
        def crawl_window_close(self):
            self.crawl_window.destroy()
            self.mess_get_dict = {
                    'plate': [''],
                    'stock': [''],
                    'searchkey': [''],
                    'category': [''],
                    'seDate': '2024-01-01~2024-12-31'
            }
            self.father.frame_more_code_finish_botton['command'] = self.crawl_window_open
            # print(self.mess_get_dict)
            self.entry_delete(self.father.sk_sktcd_one_entry)
            self.entry_delete(self.father.sk_sktcd_entry_report)
            self.entry_delete(self.father.sk_sktcd_entry_more)
            self.entry_delete(self.father.sk_sktcd_file_entry_report)
            self.entry_delete(self.father.sk_sktcd_columns_entry_report)
            self.entry_delete(self.father.sk_sktcd_file_entry_more)
            self.entry_delete(self.father.sk_sktcd_columns_entry_more)
            self.entry_delete(self.father.sk_search_key_entry)
            self.entry_delete(self.father.sk_search_key_entry_more)
            if self.father.which_menu == 1:
                report_type_list = self.father.report_type_vlist_one
            elif self.father.which_menu == 2:
                report_type_list = self.father.report_type_vlist_report
            else:
                report_type_list = self.father.report_type_vlist_more
            for repo in report_type_list:
                repo.set('')
            for plate in self.father.plate_vlist_report:
                plate.set('')
            startdate = datetime.strptime('2024-01-01', '%Y-%m-%d')
            enddate = datetime.strptime('2024-12-31', '%Y-%m-%d')
            # self.father.begindate_entry.entry.insert(0,'2024-01-01')
            self.father.begindate_entry['startdate'] = startdate
            self.father.enddate_entry['startdate'] = enddate
            self.father.begindate_entry_more['startdate'] = startdate
            self.father.enddate_entry_more['startdate'] = enddate
        def entry_delete(self,entry):
            path = entry.get()
            path_len = len(path)
            entry.delete(0,path_len)
        def code_check_one_mode(self):
            code = self.father.sk_sktcd_one_entry.get()
            self.check_window_open("股票代码")
            if code in list(df_orgid["code"]):
                # print(1)
                self.check_label['text'] = "确定成功，"
                self.result_label1['text'] = f"您输入的股票代码为{code}"
                self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                self.check_button['text'] = '完成'
                code_r = [code]
            else:
                # print(0)
                self.check_label['text'] = "确定失败，请检查股票代码输入是否为六位数准确股票代码"
                self.check_button['text'] = '退出检查'
                code_r = ['']
            self.mess_get_dict['stock'] = code_r
        def code_check1(self):
            if self.father.which_menu == 2:
                code1 = self.father.sk_sktcd_entry_report.get()
                code2 = self.father.sk_sktcd_file_entry_report.get()
                code3 = self.father.sk_sktcd_columns_entry_report.get()
            else:
                code1 = self.father.sk_sktcd_entry_more.get()
                code2 = self.father.sk_sktcd_file_entry_more.get()
                code3 = self.father.sk_sktcd_columns_entry_more.get()
            self.check_window_open("股票代码")

            if self.result_stock_from_2 == 1:
                self.check_label['text'] = "上一方案已有结果，请先返回清空（删除另一方案内容并点击确定）"
                self.check_button['text'] = '退出'
            else:
                if code1 == '':
                    self.check_label['text'] = "您选择了录入但内容为空，可退出重新选择或跳过此项"
                    self.check_button['text'] = '退出'
                    self.result_stock_from_1 = 0
                else:
                    if code2 != '' or code3 != '':
                        self.check_label['text'] = "您同时录入了两种类型，请退出后选择一种录入即可选择了录入但内容为空，可退出重新选择或跳过此项"
                        self.check_button['text'] = '退出'
                    else:
                        code1 = code1.replace(' ','').replace('，',',')
                        stock_list = code1.split(',')
                        self.result_stock_list = []
                        for s in stock_list:
                            if s in  list(df_orgid["code"]):
                                self.result_stock_list.append(s)
                            else:
                                self.check_label['text'] = f"您的输入中：{s}确定失败，请检查其是否为六位数准确股票代码"
                                self.check_button['text'] = '退出检查'
                                break
                        if len(stock_list) == len(self.result_stock_list):
                            self.check_label['text'] = "确定成功，"
                            # print(self.result_stock_list)
                            if len(self.result_stock_list)>1:
                                self.result_label1['text'] = f"您输入的股票代码为{self.result_stock_list[:2]} 等"
                            else:
                                self.result_label1['text'] = f"您输入的股票代码为{self.result_stock_list[0]} 等"
                            self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                            self.check_button['text'] = '完成'
                            self.mess_get_dict['stock'] = self.result_stock_list
                            self.result_stock_from_1 = 1
                        else:
                            self.mess_get_dict['stock'] = ['']
        def code_check2(self):
            if self.father.which_menu == 2:
                code1 = self.father.sk_sktcd_entry_report.get()
                code2 = fr'{self.father.sk_sktcd_file_entry_report.get()}'
                code3 = self.father.sk_sktcd_columns_entry_report.get()
            else:
                code1 = self.father.sk_sktcd_entry_more.get()
                code2 = fr'{self.father.sk_sktcd_file_entry_more.get()}'
                code3 = self.father.sk_sktcd_columns_entry_more.get()
            self.check_window_open("股票代码")
            if self.result_stock_from_1 == 1:
                self.check_label['text'] = "上一方案已有结果，请先返回清空（删除另一方案内容并点击确定）"
                self.check_button['text'] = '退出'
            else:
                if code2 == '':
                    self.check_label['text'] = "您选择了录入但内容为空，可退出重新选择或跳过此项"
                    self.check_button['text'] = '退出'
                else:
                    if code3 == '':
                        self.check_label['text'] = "您选择了录入但未输入列名，可退出重新选择或跳过此项"
                        self.check_button['text'] = '退出'
                    else:
                        if code1 != '':
                            self.check_label['text'] = "您同时录入了两种类型，请退出后选择一种录入即可选择了录入但内容为空，可退出重新选择或跳过此项"
                            self.check_button['text'] = '退出'
                        else:
                            if os.path.exists(code2):
                                try:
                                    df_stock = pd.read_excel(code2,converters={code3:str})
                                    stock_list = list(df_stock[code3])
                                    self.result_stock_list = []
                                    for s in stock_list:
                                        if s in list(df_orgid["code"]):
                                            self.result_stock_list.append(s)
                                        else:
                                            self.check_label['text'] = f"您的输入中：{s}确定失败，请检查其是否为六位数准确股票代码"
                                            self.check_button['text'] = '退出检查'
                                            break
                                    if len(stock_list) == len(self.result_stock_list):
                                        self.check_label['text'] = "确定成功，"
                                        self.result_label1['text'] = f"您输入的股票代码为{self.result_stock_list[0]}等"
                                        self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                                        self.check_button['text'] = '完成'
                                        self.mess_get_dict['stock'] = self.result_stock_list
                                        self.result_stock_from_2 = 1
                                    else:
                                        self.mess_get_dict['stock'] = ['']
                                except:
                                    self.check_label['text'] = "文件路径输入有误"
                                    self.check_button['text'] = '退出'
                            else:
                                self.check_label['text'] = "文件路径输入有误，请返回检查后重新填写或跳过此项"
                                self.check_button['text'] = '退出'
        def keyword_check(self):
            if self.father.which_menu ==1:
                keyword = self.father.sk_search_key_entry.get()
            else:
                keyword = self.father.sk_search_key_entry_more.get()
            keyword = keyword.replace("   ","").replace("  ","")
            self.key_list = keyword.split(" ")
            self.check_window_open("关键词")
            if len(self.key_list) == 1 and self.key_list[0] == '':
                self.check_label['text'] = "您选择了录入但内容为空，可退出重新选择或跳过此项"
                self.check_button['text'] = '退出'
                self.key_list = ['']
            else:
                self.check_label['text'] = "确定成功，已录入"
                self.result_label1['text'] = f"您输入的检索关键词为：{'、'.join(self.key_list)}"
                self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                self.check_button['text'] =  '完成'
            self.mess_get_dict['searchkey']=self.key_list
        def plate_check_report(self):
            plate_report_list = self.father.plate_vlist_report
            self.plate_report_choose_list = []
            for plate_report in plate_report_list:
                plate_report_value = plate_report.get()
                if plate_report_value != '':
                    self.plate_report_choose_list.append(plate_report_value)
                else:
                    pass
            if len(self.plate_report_choose_list) == 0:
                self.plate_report_choose_list = ['']
            else:
                pass
            self.check_window_open("所属板块")
            if len(self.plate_report_choose_list) == 1 and self.plate_report_choose_list[0] == '' :
                self.check_label['text'] = "您选择了录入但内容为空，可退出重新选择或跳过此项"
                self.check_button['text'] = '退出'
            else:
                self.check_label['text'] = "确定成功，已录入"
                self.result_label1['text'] = f"您输入的板块类型为：{'、'.join(self.plate_report_choose_list)}"
                self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                self.check_button['text'] = '完成'
            self.mess_get_dict["category"] = self.plate_report_choose_list
        def report_type_check(self):
            if self.father.which_menu == 1:
                report_type_list = self.father.report_type_vlist_one
            elif self.father.which_menu == 2:
                report_type_list = self.father.report_type_vlist_report
            else:
                report_type_list = self.father.report_type_vlist_more
            self.report_type_choose_list = []
            for report_type in report_type_list:
                report_type_value = report_type.get()
                if report_type_value != '':
                    self.report_type_choose_list.append(report_type_value)
                else:
                    pass
            if len(self.report_type_choose_list) == 0:
                self.report_type_choose_list = ['']
            else:
                pass
            self.check_window_open("报告类型")
            if len(self.report_type_choose_list) == 1 and self.report_type_choose_list[0] == '' :
                self.check_label['text'] = "您选择了录入但内容为空，可退出重新选择或跳过此项"
                self.check_button['text'] = '退出'
            else:
                self.check_label['text'] = "确定成功，已录入"
                self.result_label1['text'] = f"您输入的报告类型为：{'、'.join(self.report_type_choose_list)}"
                self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                self.check_button['text'] = '完成'
            self.mess_get_dict["category"] = self.report_type_choose_list
        def begin_end_time_check(self):
            if self.father.which_menu == 1:
                begin_time = self.father.begindate_entry.entry.get()
                end_time = self.father.enddate_entry.entry.get()
            elif self.father.which_menu == 3:
                begin_time = self.father.begindate_entry_more.entry.get()
                end_time = self.father.enddate_entry_more.entry.get()
            else:
                self.beginyear = self.father.beginyear_combobox.get()
                self.endyear = self.father.endyear_combobox.get()
                if self.beginyear == '':
                    self.beginyear = 2023
                else:
                    pass
                if self.endyear == '':
                    self.endyear = 2023
                else:
                    pass
                begin_time = f'{self.beginyear}-01-01'
                end_time = f'{str(int(self.endyear)+1)}-12-31'
            self.check_window_open("起始时间")
            if begin_time > end_time:
                self.check_label['text'] = "终止日期应大于或等于起始日期，请重新选择"
                self.check_button['text'] = '退出'
            else:
                self.check_label['text'] = "确定成功，已录入"
                if self.father.which_menu == 2:
                    if self.beginyear == self.endyear:
                        self.result_label1['text'] = f"您输入的报告范围为：{self.beginyear}年"
                    else:
                        self.result_label1['text'] = f"您输入的报告范围为：{self.beginyear}年 ~ {self.endyear}年"
                else:
                    self.result_label1['text'] = f"您输入的起始时间为：{begin_time} ~ {end_time}"
                self.result_label2['text'] = f"若要更改，可点击完成后重新输入并确定"
                self.check_button['text'] = '完成'
            self.mess_get_dict["seDate"] = f'{begin_time} ~ { end_time}'
        def crawl_window_open(self):
            # print(self.mess_get_dict)
            mess_dict = self.mess_get_dict
            if self.father.which_menu == 2 and mess_dict['category'] == ['']:
                self.mess_get_dict['category'] = ['年报','半年报','一季度报','三季度报']
            self.father.frame_more_code_finish_botton['command'] = ''
            # print(self.mess_get_dict)
            self.crawl_window = Toplevel(master=self.father.root)
            self.crawl_width = 1000
            self.crawl_height = 500
            self.crawl_begin_height = (self.father.screenheight - self.crawl_height) / 2
            self.crawl_begin_width = (self.father.screenwidth - self.crawl_width) / 2
            self.crawl_window.geometry('%dx%d+%d+%d' % (self.crawl_width, self.crawl_height, self.crawl_begin_width, self.crawl_begin_height))
            self.title_check_label = Label(self.crawl_window, text=f"您已进入批量下载阶段",
                                           font=("宋体", 14, "bold"))
            self.title_check_label.pack(pady=(5, 25))
            self.total_label = Label(self.crawl_window, text="",font=("仿宋", 13, "bold"))
            self.total_label.pack(pady=(10, 10))
            self.button_frame = Frame(self.crawl_window)
            crawl_begin_button = Button(self.button_frame, text="", font=("仿宋", 13, "bold"))
            crawl_begin_button.pack(padx=(10, 20),side = LEFT)
            crawl_back_button = Button(self.button_frame, text="返回", font=("仿宋", 13, "bold"),command = self.crawl_window_close)
            crawl_back_button.pack(side = LEFT)
            self.button_frame.pack(pady=(10, 10))
            dict_for_convert = self.mess_get_dict
            self.re_data = cnifo_data_convert(dict_for_convert)
            self.url_cninfo = "http://www.cninfo.com.cn/new/hisAnnouncement/query"
            resp = requests.post(url=self.url_cninfo, data=self.re_data)
            resp_json = resp.json()
            self.totalAnnouncement = resp_json['totalAnnouncement']
            # print(self.totalAnnouncement)
            if self.totalAnnouncement % 30 == 0:
                self.totalpages = self.totalAnnouncement/30
            else:
                self.totalpages = self.totalAnnouncement//30+1
            self.first_announcements = resp_json['announcements']
            # print(self.mess_get_dict)
            # print(self.father.which_menu)
            if self.father.which_menu == 1:
                if self.mess_get_dict['stock'] == '':
                    self.total_label['text'] = f"您还未输入股票代码"
                    crawl_begin_button['text'] = '退出'
                    crawl_begin_button['command'] = self.crawl_window_close
                else:
                    if self.first_announcements == None:
                        self.total_label['text'] = f"未检索到内容，请退出重试或联系我们了解原因~"
                        crawl_begin_button['text'] = '退出'
                        crawl_begin_button['command'] = self.crawl_window_close
                    else:
                        if self.father.which_menu == 2:
                            self.total_label[
                                'text'] = f"一共为您检索{self.totalpages}页公告，合计{self.totalAnnouncement}篇公告【可能存在上一年度，后续会剔除】"
                        else:
                            self.total_label['text'] = f"一共为您检索{self.totalpages}页公告，合计{self.totalAnnouncement}篇公告"
                        crawl_begin_button['text'] = '下一步'
                        crawl_begin_button['command'] = self.push_to_file_enrty
            else:
                if self.first_announcements == None:
                    self.total_label['text'] = f"未检索到内容，请退出重试或联系我们了解原因~"
                    crawl_begin_button['text'] = '退出'
                    crawl_begin_button['command'] = self.crawl_window_close
                else:
                    if self.father.which_menu == 2:
                        self.total_label['text']=f"一共为您检索{self.totalpages}页公告，合计{self.totalAnnouncement}篇公告【可能存在上一年度，后续会剔除】"
                    else:
                        self.total_label['text'] = f"一共为您检索{self.totalpages}页公告，合计{self.totalAnnouncement}篇公告"
                    crawl_begin_button['text'] = '下一步'
                    crawl_begin_button['command'] = self.push_to_file_enrty
        def push_to_file_enrty(self):
            self.file_entry_frame = Frame(self.crawl_window)
            self.file_wl = Label(self.file_entry_frame, text="请输入保存的文件路径（不可为空）", font=("仿宋", 13, "bold"))
            self.file_wl.pack(pady=(10, 10))
            self.file_entry = Entry(self.file_entry_frame, font=("仿宋", 13, "bold"),width = 30)
            self.file_entry.pack(pady=(10, 10))
            self.file_button_frame = Frame(self.file_entry_frame)
            self.file_confirm_button = Button(self.file_button_frame, text="确定", font=("仿宋", 13, "bold"),command = self.file_confirm)
            self.file_confirm_button.pack(side=LEFT, padx=(10, 20))
            self.file_confirm_button = Button(self.file_button_frame, text="清除", font=("仿宋", 13, "bold"),command = self.file_delete)
            self.file_confirm_button.pack(side=LEFT)
            self.file_button_frame.pack(pady=(10, 10))
            self.file_check_wl = Label(self.file_entry_frame, text="", font=("仿宋", 13, "bold"))
            self.begin_request_button = Button(self.file_entry_frame, text="开始下载", font=("仿宋", 13, "bold"),command = self.begin_request_frame)
            self.file_check_wl.pack(pady=(10, 10))
            self.file_entry_frame.pack(pady=(5, 10))
        def file_confirm(self):
            self.file_output_path = self.file_entry.get()
            if os.path.exists(self.file_output_path):
                self.file_check_wl['text'] = '已识别文件夹，点击下一步即可开始下载'
                self.begin_request_button.pack(padx=(20, 20))
            else:
                try:
                    os.makedirs(self.file_output_path)
                    self.file_check_wl['text'] = '已识别文件夹，点击下一步即可开始下载'
                    self.begin_request_button.pack(padx=(20, 20))
                except:
                    self.file_check_wl['text'] = '未识别文件夹，请重新输入，建议选择现有文件夹'
        def file_delete(self):
            path = self.file_entry.get()
            path_len = len(path)
            self.file_entry.delete(0,path_len)
        def begin_request_frame(self):
            self.file_entry_frame.pack_forget()
            self.requesting_frame = Frame(self.crawl_window)
            self.requesting_wl = Label(self.requesting_frame, text="下载进行中...", font=("仿宋", 13, "bold"))
            self.requesting_wl.pack(pady=(10, 10))
            self.progressbar = tkb.Progressbar(self.requesting_frame,bootstyle='primary-striped')
            self.progressbar.pack(pady=20, ipadx=100)
            self.request_sucess_wl = Label(self.requesting_frame, text="", font=("仿宋", 13, "bold"))
            self.request_sucess_wl.pack(pady=(10,0))
            self.request_progress_wl = Label(self.requesting_frame, text="", font=("仿宋", 13, "bold"))
            self.request_progress_wl.pack(pady=(5, 10))
            self.announcements = self.get_announcements()
            self.progressbar['maximum'] = len(self.announcements)-1
            self.requesting_frame.pack(pady=(5, 10))
            self.begin_request_def()
            self.finish_button_frame = Frame(self.requesting_frame)
            self.request_finish_button = Button(self.finish_button_frame, text="继续", font=("仿宋", 13, "bold"),command = self.crawl_window_close)
            self.request_finish_button.pack(side = LEFT,padx = (10,20))
            self.request_quick_button = Button(self.finish_button_frame, text="退出", font=("仿宋", 13, "bold"),command = self.father.window_quit)
            self.request_quick_button.pack(side = LEFT,padx = (10,20))
            self.finish_button_frame.pack(pady=(10, 10))
        def get_announcements(self):
            announcements = self.first_announcements
            if self.totalpages == 1:
                pass
            else:
                all_announcements = self.first_announcements
                for i in range(2,self.totalpages+1):
                    after_data = self.re_data
                    after_data['pageNum'] = i
                    after_resp = requests.post(url=self.url_cninfo, data=after_data)
                    after_resp_json = after_resp.json()
                    after_announcements = after_resp_json['announcements']
                    all_announcements += after_announcements
                announcements = all_announcements
            return announcements

                    # break
        def begin_request_def(self):
            self.result_path = f'{self.file_output_path}\\result'
            if os.path.exists(self.result_path):
                pass
            else:
                os.makedirs(self.result_path)
            if self.father.which_menu == 2:
                # print(self.beginyear)
                announcements_menu2 = self.announcements
                announcements_menu2_fix = []
                for i in range(len(announcements_menu2)):
                    ann = self.announcements[i]
                    ann_title = ann['announcementTitle']
                    begin = int(self.beginyear)
                    end = int(self.endyear)+1

                    for year in range(begin,end):
                        year_str = str(year)
                        if year_str in ann_title and '摘要' not in ann_title and '英文' not in ann_title and '取消' not in ann_title:
                            announcements_menu2_fix.append(ann)

                            break
                        else:
                            continue
                self.announcements = announcements_menu2_fix
                self.progressbar['maximum'] = len(self.announcements) - 1
                self.total_label['text'] = f"一共为您检索{self.totalpages}页公告，合计{len(self.announcements)}篇公告"
                self.progressbar['maximum'] = len(self.announcements) - 1

            for i in range(len(self.announcements)):
                ann = self.announcements[i]
                ann_stock = ann['secCode']
                ann_stock_name = ann['secName']
                ann_title = ann['announcementTitle']
                # 清理HTML标签和非法文件名字符
                import re
                ann_title = re.sub(r'<[^>]+>', '', ann_title)  # 移除所有HTML标签
                illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
                for char in illegal_chars:
                    ann_title = ann_title.replace(char, '')
                    ann_stock_name = ann_stock_name.replace(char, '')  # 清理股票名称(如*ST)
                ann_url = ann['adjunctUrl']
                ann_time = ann_url.split('/')[1]
                ann_allurl_for_download = f"http://static.cninfo.com.cn/{ann_url}"
                file_name = f"{i+1}_{ann_stock}_{ann_stock_name}_{ann_title}.pdf"
                ann_resp = requests.get(ann_allurl_for_download)
                file_path = os.path.join(self.result_path, file_name)
                # print(file_path)
                try:
                    with open(file_path, 'wb') as pdf_file:
                        pdf_file.write(ann_resp.content)
                    self.request_sucess_wl['text'] = f"{ann_stock_name}_{ann_title}_{ann_time} 成功"
                except:
                    self.request_sucess_wl['text'] = f"{ann_stock_name}_{ann_title}_{ann_time} 失败"
                self.request_progress_wl['text'] = f'共有{len(self.announcements)}条，已经完成{i+1}条'
                self.progressbar['value'] = i
                self.crawl_window.update()
                time.sleep(0.1)
            self.request_progress_wl['text'] = '下载任务已完成'
            self.requesting_wl['text'] = '下载完成'


def cnifo_data_convert(fram_dict):
    df_orgid_t = df_orgid
    report_type_convert_dict = {
        "年报": 'category_ndbg_szsh',
        "半年报": 'category_bndbg_szsh',
        "一季度报": 'category_yjdbg_szsh',
        "三季度报": 'category_sjdbg_szsh',
        "其他": '',
    }
    plate_convert_dict = {
        '主板[沪]': 'shmb',
        '主板[深]': 'szmb',
        '创业板': 'szcy',
        '科创板': 'shkcp',
        '北交所': 'bj'
    }
    dict_for_c = fram_dict
    search = dict_for_c['searchkey']
    search_j = ';'.join(search)
    dict_for_c['searchkey'] = search_j
    stock = dict_for_c['stock']
    if stock != ['']:
        new_dict_value_list = []
        for s in stock:
            gssz_stock = list(df_orgid_t['orgId'][df_orgid_t['code'] == s])[0]
            new_v = f'{s},{gssz_stock}'
            new_dict_value_list.append(new_v)
        dict_for_c['stock'] = ';'.join(new_dict_value_list)
    else:
        dict_for_c['stock'] = ''
    plate = dict_for_c['plate']
    plate_list = []
    if plate != ['']:
        for p in plate:
            p_c = plate_convert_dict[p]
            plate_list.append(p_c)
        plate_c = ';'.join(plate_list)
        dict_for_c['plate'] = plate_c
    else:
        dict_for_c['plate'] = ''

    category = dict_for_c['category']
    category_list = []
    if category != ['']:
        for cat in category:
            cat_c = report_type_convert_dict[cat]
            category_list.append(cat_c)
        category_c = ';'.join(category_list)
        dict_for_c['category'] = category_c
    else:
        dict_for_c['category'] = ''
    data = {
        'pageNum': 1,
        'pageSize': 30,
        'column': 'szse',
        'tabName': 'fulltext',
        'plate': dict_for_c['plate'],#板块
        'stock': dict_for_c['stock'],#股票代码
        'searchkey': dict_for_c['searchkey'],#检索关键词
        'secid': '',
        'category': dict_for_c['category'],#category,报告类型
        'trade': '',
        'seDate':  dict_for_c['seDate'],#时间 xx~xx
        'sortName': '',
        'sortType': '',
        'isHLtitle': 'true'}
    return data

tk_cnifo()

