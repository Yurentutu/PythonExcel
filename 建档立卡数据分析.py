import numpy as np
import pandas as pd
import re
import openpyxl

#列名称、顺序相同的表直接行堆叠合并
BeiPing = pd.read_excel('D:\源.xlsx',sheet_name='北平镇',header=2,index_col=None)
GuYang = pd.read_excel('D:\源.xlsx',sheet_name='古阳镇',header=2,index_col=None)
ShiBi = pd.read_excel('D:\源.xlsx',sheet_name='石壁乡',header=2,index_col=None)
YongLe =pd.read_excel('D:\源.xlsx',sheet_name='永乐乡',header=2,index_col=None)
NanYuan =pd.read_excel('D:\源.xlsx',sheet_name='南垣乡',header=2,index_col=None)
YueYang =pd.read_excel('D:\源.xlsx',sheet_name='岳阳镇',header=2,index_col=None)
df = pd.concat([BeiPing,GuYang,ShiBi,YongLe,NanYuan,YueYang])

#列名称不同，但行没有重复的表，修改表2的列名称，然后直接行堆叠合并
df.columns=['序号', '采集日期', '区县', '乡(镇)', '行政村', '自然村', '户编号', '姓名', '身份证号', '民族',
       '与户主关系', '婚姻状况', '手机号码', '户口性质', '户籍地址', '健康状况', '年收入(元)', '文化程度',
       '毕业院校', '所学专业', '毕业日期', '特殊人群标识', '就业失业类型',
       '单位类型',
       '单位名称', '就业工种', '单位地址', '劳动合同',
       '是否劳务输入', '人力资源机构名称', '机构性质', '创业类型', '享受扶持政策',
       '是否返乡创业', '灵活就业类型', '新业态就业类型', '失业类型', '原单位名称',
       '失业时间', '原工种', '未就业原因', '求职意愿', '求职行业',
       '求职工种', '求职地点', '期望薪资', '劳务输入意愿',
       '输出方式', '输出意向地', '输出薪资', '是否有培训经历', '培训日期',
       '培训机构', '培训工种', '工种等级', '培训意愿', '意愿培训日期',
       '意愿培训地点', '意愿培训工种', '意愿工种等级', '有无专业技术职称信息', '专业技术职称',
       '层级', '获取时间', '聘任状态', '有无职业技能信息',
       '证书类别', '证书工种名称', '证书等级', '证书获取时间','证书编号', '技能大赛获奖信息']
JiuXian = pd.read_excel('D:\源.xlsx',sheet_name='旧县镇',header=2,index_col=None)
JiuXian.columns=[ '姓名', '身份证号', '民族','婚姻状况', '手机号码', '户口性质', '户籍地址','居住地址', '文化程度',
       '毕业院校',  '毕业日期','所学专业', '健康状况', '年收入(元)','特殊人群标识','特殊人群标识2','特殊人群标识3', '培训意愿', '意愿培训日期',
       '意愿培训地点', '意愿培训工种', '意愿培训工种2', '意愿培训工种3', '意愿工种等级', '求职意愿', '求职行业',
       '求职工种','求职工种2','求职工种3', '期望薪资', '求职地点', '劳务输入意愿', '输出意向地', '输出薪资', '就业失业类型', '未就业原因',
       '失业类型','失业原因', '原单位名称',
       '失业时间', '原工种','原工种2','原工种3','单位类型',
       '单位名称', '就业工种','就业工种2','就业工种3', '单位地址', '劳动合同','创业类型', '享受扶持政策',
       '是否返乡创业', '灵活就业类型', '新业态就业类型',
       '是否劳务输入', '人力资源机构名称', '机构性质', '有无职业技能信息',
       '证书类别', '证书工种名称', '证书等级', '证书获取时间','证书编号','有无专业技术职称信息', '专业技术职称',
       '层级', '获取时间', '聘任状态', '技能大赛获奖信息']
HuiZong = pd.concat([df,JiuXian])



#替换所有的空字符串为空值NAN
HuiZong.replace(to_replace=r'^\s*$',value=np.nan,regex=True,inplace=True)
#丢掉身份证号列为空值的行
HuiZong=HuiZong.dropna(subset=['身份证号'])
#新增列取残疾人证号的前18位身份证号
HuiZong['18位身份证号'] = HuiZong.身份证号.astype('str').str[0:18]



'''
#使用combine合并,需要重新设置行索引，重新设置行索引前，要调整目标列的位置，
HuiZong = HuiZong[['18位身份证号','序号', '采集日期', '区县', '乡(镇)', '行政村', '自然村', '户编号', '姓名', '身份证号', '民族',
       '与户主关系', '婚姻状况', '手机号码', '户口性质', '户籍地址', '健康状况', '年收入(元)', '文化程度',
       '毕业院校', '所学专业', '毕业日期', '特殊人群标识', '就业失业类型', '单位类型', '单位名称', '就业工种',
       '单位地址', '劳动合同', '是否劳务输入', '人力资源机构名称', '机构性质', '创业类型', '享受扶持政策',
       '是否返乡创业', '灵活就业类型', '新业态就业类型', '失业类型', '原单位名称', '失业时间', '原工种', '未就业原因',
       '求职意愿', '求职行业', '求职工种', '求职地点', '期望薪资', '劳务输入意愿', '输出方式', '输出意向地',
       '输出薪资', '是否有培训经历', '培训日期', '培训机构', '培训工种', '工种等级', '培训意愿', '意愿培训日期',
       '意愿培训地点', '意愿培训工种', '意愿工种等级', '有无专业技术职称信息', '专业技术职称', '层级', '获取时间',
       '聘任状态', '有无职业技能信息', '证书类别', '证书工种名称', '证书等级', '证书获取时间', '证书编号',
       '技能大赛获奖信息', '居住地址', '特殊人群标识2', '特殊人群标识3', '意愿培训工种2', '意愿培训工种3', '求职工种2',
       '求职工种3', '失业原因', '原工种2', '原工种3', '就业工种2', '就业工种3']]
#重新设置行索引前，还要删除索引列中存在的重复行
HuiZong.drop_duplicates(subset='18位身份证号',keep='first',inplace = True)
#重新设置行索引
HuiZong.set_index('18位身份证号',inplace = True)

'''
#读入表2
df1500 = pd.read_excel('D:/1572源.xlsx',sheet_name='台账',header=2,index_col=None)
#丢掉表2不需要的列
df2 = df1500.loc[:,['乡镇','行政村','系统户主姓名','身份证号','迁入地址']]
#使用merge合并之前，也要调整两表对应列名一致。方便之后_x,_y查看
df2.columns=[ '乡(镇)', '行政村', '姓名','18位身份证号','迁入地址']
'''
#列名称不同，但行没有重复的表，修改表2的列名称，然后直接行堆叠合并或combine合并
df2.columns=[ '乡(镇)', '行政村', '姓名','18位身份证号','迁入地址']
#使用combine合并,需要重新设置行索引，重新设置行索引前，要调整目标列的位置，
df2 = df2[['18位身份证号','乡(镇)', '行政村', '姓名','迁入地址']]
#重新设置行索引
df2.set_index('18位身份证号',inplace = True)
#使用combine_first之前需要设置好行索引和列名。根据行索引，HuiZong缺少的列值会被df2中对应列值所替代。
df3 = HuiZong.combine_first(df2)
'''
df3=pd.merge(HuiZong,df2,on=['18位身份证号'],how='outer')





#merge合并之后，除依据的索引列之外，用表2相同列的值填充表1的列。
df3['姓名_x'].fillna(df3['姓名_y'],inplace = True)
df3['乡(镇)_x'].fillna(df3['乡(镇)_y'],inplace = True)
df3['行政村_x'].fillna(df3['行政村_y'],inplace = True)
#删掉来自表2的多余的相同列
df.drop(['乡(镇)_y','行政村_y','姓名_y'],axis=1,inplace=True)

df3.to_excel('D:/增加迁出地址.xlsx',index=False)
