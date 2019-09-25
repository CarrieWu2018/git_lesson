# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:42:39 2019
Read Excel file and write the permit charges to csv files
Name:
Read_excel_file_get_fees_charged -using pandas.py
Input dir:
    "P:/Back Office/Back Office Internet Projects/10183_C1_Production\
_support/CHIOPS-1287 Access fee billing impact from Feb 2018 till May 2019/"
Input filename:
    "Permits used to trade OO upto May2019 v2.xlsx"
Output filenames:
    'Permits and MM access fees upto May2019.csv'
    'Permits used vs charged upto May2019.csv'
    'Permits add SPX Tier charges upto May2019.csv'
Reference:
https://www.pyxll.com/blog/tools-for-working-with-excel-and-python/#xlrd
xlwt - the excel write tool is for old excel, no longer the best choice

pandas is used in this version

@author: wuc
"""

import xlrd
import os
import pandas as pd


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
    spath =("P:/Back Office/Back Office Internet Projects/10183_C1_Production\
_support/CHIOPS-1287 Access fee billing impact from Feb 2018 till May 2019/")
#    sname ="Permits addSPX to charged upto May2019 report3.xlsx"
    sname ="Permits used to trade OO upto May2019 v2.xlsx"
    sloc = os.path.join(spath, sname)
    print(sloc)
 
    oospx_df = pd.read_excel(sloc, sheet_name='SPX-W trades w vol')
    oospx_df =oospx_df.drop(columns=['PROD CLASS SYM','SUM(CONTR QTY)'])
    oospx_df = oospx_df.drop_duplicates()
    # rmovee NULL SEAT NBR rows after manual check
    oospx_df = oospx_df.dropna()
    _df_ym = pd.to_datetime(oospx_df['TRANS DATE']).dt.to_period('M')
    _df_ym = _df_ym.astype(str)
    oospx_df['YearMon'] = _df_ym
    _permit = oospx_df['SEAT NBR']
    oospx_df['YearMon_Permit'] = ( _df_ym + '_' + _permit )

# get permits that are being shared with appointed MM with SPX 
    s2name = "Permits shared upto May2019 report.xlsx"
    s2loc = os.path.join(spath, s2name)
    shared_df = pd.read_excel(s2loc,
                              sheet_name='Permit shared summary')
    shared_df = shared_df.dropna()
    shared_df =shared_df.drop(columns=['TRDNG USER ACR',
                                 'MM TRDNG APPT IND',
                                 'MM NAME'])
    shared_df = shared_df.drop_duplicates()
    
    _df_ym = pd.to_datetime(shared_df['TRANS DATE']).dt.to_period('M') 
    _df_ym = _df_ym.astype(str)
    shared_df['YearMon_Permit'] = (_df_ym + '_' + shared_df['SEAT NBR'])

    # minus already charge items
    spx_df = oospx_df.query('YearMon_Permit not in @shared_df.YearMon_Permit')
    
    
fpath = ("P:/EDMG/DWS/Support/Billing/IBS to Accounting Spreadsheets/")
filemon = [
#        "2017/2017_12_DEC/",
#           "2018/2018_01_JAN/",
#           "2018/2018_02_FEB/",
#           "2018/2018_03_MAR/",
#           "2018/2018_04_APR/",
#           "2018/2018_05_MAY/",
#           "2018/2018_06_JUNE/",
#           "2018/2018_07_JULY/",
#           "2018/2018_08_AUG/",
#           "2018/2018_09_SEP/",
#           "2018/2018_10_OCT/",
           "2018/2018_11_NOV/",
#           "2018/2018_12_DEC/",
           "2019/2019_01_JAN/"
#           ,
#           "2019/2019_02_FEB/",
#           "2019/2019_03_MAR/",
#           "2019/2019_04_APR/",
#           "2019/2019_05_MAY/"
           ]

filenames = [
#        "Access_Fee_Report_All_Firms_201712.xls",
#             "Access_Fee_Report_All_Firms_201801.xls",
#             "Access_Fee_Report_All_Firms_201802.xls",
#             "Access_Fee_Report_All_Firms_201803.xls",
#             "Access_Fee_Report_All_Firms_201804.xls",
#             "Access_Fee_Report_All_Firms_201805.xls",
#             "Access_Fee_Report_All_Firms_201806.xls",
#             "Access_Fee_Report_All_Firms_201807.xls",
#             "Access_Fee_Report_All_Firms_201808.xls",
#             "Access_Fee_Report_All_Firms_201809.xls",
#             "Access_Fee_Report_All_Firms_201810.xls",
             "Access_Fee_Report_All_Firms_201811.xls",
#             "Access_Fee_Repot_All_Firms_201812.xls",
             "Access_Fee_Repot_All_Firms_201901.xls"
#             ,
#             "Access_Fee_Report_All_Firms_201902.xls",
#             "Access_Fee_Report_All_Firms_201903.xls",
#             "Access_Fee_Report_All_Firms_201904.xls",
#             "Access_Fee_Report_All_Firms_201905.xls"
             ]

nbr_files = len(filenames)

charged = [] 
for file_i in range(nbr_files):
    loc = os.path.join(fpath, filemon[file_i], filenames[file_i]) 
    print(filemon[file_i])
    # get year month 2017_12_DEC, from the second field after split
    yearmon_str = filemon[file_i].split('/')[1]
    yearmon = yearmon_str[0:7]
    # to matchup Year month format
    yearmon = yearmon.replace('_','-')
    rows = get_fees_from_file(loc)
    for i, row in enumerate(rows):
        # add YEARMON column header and date in year mon form
        if file_i == 0 and i == 0:  
            row.append('YearMon')
#            print(file_i, i, row[9])
            header = row
        else:
            row.append(yearmon)
        # Get MM access fee- if MM in Permit column, and not VIP, add row
        if row[6][0:2] == 'MM':
            if row[3][0:12] =='Market Maker' and row[3][13:16] != 'VIP':
                charged.append(row)

#convert list to pandas DataFrame            
charged_df = pd.DataFrame(charged, columns = header)

#find given YearMon permit if were charged
seat2 = charged_df[((charged_df['FIRM_ID']== 99762) &
            (charged_df['YearMon']=='2019-01') &
            ( charged_df['PERMIT_NUMBER']=='MMP0350' ))]

seat1 = charged_df[((charged_df['FIRM_ID']== 56826) &
            (charged_df['YearMon']=='2018-11') &
            ( charged_df['PERMIT_NUMBER']=='MMP0581' ))]    

