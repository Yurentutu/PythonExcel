import numpy as np
import pandas as pd
import openpyxl
import Levenshtein











bd =pd.read_excel('D:/劳动力信息采集表.xlsx',sheet_name='本省地址',header =None)
gz =pd.read_excel('D:/劳动力信息采集表.xlsx',sheet_name='工种分类',header =0)
jx = pd.read_excel('D:/源.xlsx',sheet_name='旧县镇',header =3)




jx.columns =['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
       'Unnamed: 5', '户籍地址', '省市县乡村(外省填写省市县).1', 'Unnamed: 8',
       '毕业院校', '毕业时间', '专业', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
       'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
       'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22',
       'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26',
       'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', '有无意愿',
       '意愿国家', '期望薪资\n（月平均）', 'Unnamed: 34', '未就业原因', '失业类型', '失业原因', '原单位名称',
       '失业时间', '职位/工种（大类）', '职位/工种（子类一）', '职位/工种（子类二）', '单位类型', '单位名称',
       '职位/工种（大类）.1', '职位/工种（子类一）.1', '职位/工种（子类二）.1', '单位地址', '劳动合同', '创业类型',
       '享受扶持政策情况', '下(返)乡创业', '灵活就业方式', '新业态就业方式', '是否', '人力资源服务机构名称', '机构性质',
       'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 'Unnamed: 61',
       'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 'Unnamed: 65',
       'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69']

chang = len(jx)
a=0
i=0
lie = list(range(chang))
for olddizhi in jx.户籍地址.astype(str):
        a = 0
        for newdizhi in bd[0].astype(str):
                temp = Levenshtein.ratio(olddizhi,newdizhi)
                if temp>a:
                        a=temp
                        lie[i]=newdizhi
        print(lie[i])
        i=i+1


jx['新户籍地址']=lie


jx.to_excel('D:/旧县镇修改地址.xlsx',index=False)

