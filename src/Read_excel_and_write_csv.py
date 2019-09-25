# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:42:39 2019
Read Excel file and write the permit charges to csv file
Read_excel_file.py

https://www.pyxll.com/blog/tools-for-working-with-excel-and-python/#xlrd
xlwt - the excel write tool is for old excel, no longer the best choice

@author: wuc
"""

import xlrd
import os

#from datetime import datetime


def get_seats(sloc:str) ->list:
    from xlrd.xldate import xldate_as_tuple
    wb = xlrd.open_workbook(sloc)
    sheet = wb.sheet_by_name("OO SPX")
    seats = []
    for row in range(1, sheet.nrows):
        seat = sheet.cell_value(row,4)
        MM_acr = sheet.cell_value(row,2)
        firm = sheet.cell_value(row, 6)
        if seat != '':
            adate = int(sheet.cell_value(row,0))
            adttup = xldate_as_tuple(adate,0)
            year, month = adttup[0:2]  
#            print(year, month, seat)
            # create a two-element list and add to seats list
            new_elem = [str(year) + "_" + str(month), seat, MM_acr, firm]
            if new_elem not in seats:
                seats.append(new_elem)
    return seats

def get_fees_from_file(loc:str) ->list:
    fee_charged = [] 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        row = sheet.row_values(i)
        # remove comma "," from $ amount 
        row[8]= row[8].replace(',','')
        row[2]= row[2].replace(',',' ')
        fee_charged.append(row)
    return fee_charged


if __name__=='__main__':
    spath =("../data/")
    sname ="monthly.xlsx"
    sloc = os.path.join(spath, sname)
    print(sloc)
    ym_seats = get_seats(sloc)
#    unique_seats = set(ym_seats.values())

fpath = ("P:/EDMG/DWS/Support/Billing/IBS to Accounting Spreadsheets/")
filemon = ["2017/2017_12_DEC/",
           "2018/2018_03_MAR/",
           "2018/2018_08_AUG/",
           "2018/2018_09_SEP/",
           "2018/2018_10_OCT/",
           "2018/2018_11_NOV/",
           "2018/2018_12_DEC/",
           "2019/2019_01_JAN/",
           "2019/2019_02_FEB/",
           "2019/2019_03_MAR/",
           "2019/2019_04_APR/",
           "2019/2019_05_MAY/"
#           ,
#           "2019/2019_06_JUN/", 
#           "2019/2019_07_JUL/",
#           "2019/2019_08_AUG/"
           ]
filenames = ["Access_Fee_Report_All_Firms_201712.xls",
            "Access_Fee_Report_All_Firms_201803.xls",
            "Access_Fee_Report_All_Firms_201808.xls",
            "Access_Fee_Report_All_Firms_201809.xls",
            "Access_Fee_Report_All_Firms_201810.xls",
            "Access_Fee_Report_All_Firms_201811.xls",
            "Access_Fee_Repot_All_Firms_201812.xls",
#?            "Access_Fee_Report_All_Firms_201901.xls",
            "Access_Fee_Repot_All_Firms_201901.xls",
            "Access_Fee_Report_All_Firms_201902.xls",
            "Access_Fee_Report_All_Firms_201903.xls",
            "Access_Fee_Report_All_Firms_201904.xls",
            "Access_Fee_Report_All_Firms_201905.xls"
#            ,
#            "Access_Fee_Report_All_Firms_201906.xls",
#            "Access_Fee_Report_All_Firms_201907.xls",
#            "Access_Fee_Report_All_Firms_201908.xls"
            ]
nbr_files = len(filenames)

charged = [] 
for file_i in range(2): #nbr_files):
    loc = os.path.join(fpath, filemon[file_i], filenames[file_i]) 
    print(filemon[file_i])
    # get year month 2017_12_DEC
    yearmon_str = filemon[file_i].split('/')[1]
    yearmon = yearmon_str[0:7]
    # remove 0 from _0 so that 2019_07 becomes 2019_7
    yearmon = yearmon.replace('_0','_')
    rows = get_fees_from_file(loc)
    for i, row in enumerate(rows):
        # add YEARMON column header and date in year mon
        if file_i == 0 and i == 0:  
            row.append('YEARMON')
#            print(file_i, i, row[9])
            charged.append(row)
        else:
            row.append(yearmon)
        # save the rows that in selected seat list ym_seats
        if [row[9],row[6]] in ym_seats[0:1] and row[8]=='$3,000':
#            print(file_i, i, row[9], row[6])
            charged.append(row)
    
with open('output_OO.csv', 'w') as f:
    for item in charged:
        if type(item) == list:
            for col in (item):
                f.write("%s," % col)
        else:
            f.write("%s" % item)
        f.write("\n")
