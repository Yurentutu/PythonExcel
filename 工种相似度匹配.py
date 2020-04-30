Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> import pandas
>>> import openpyxl
>>> import Levenshtein
>>> gz =pd.read_excel('D:/劳动力信息采集表.xlsx',sheet_name='工种分类',header =0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    gz =pd.read_excel('D:/劳动力信息采集表.xlsx',sheet_name='工种分类',header =0)
NameError: name 'pd' is not defined
>>> import numpy as np
>>> import pandas as pd
>>> gz =pd.read_excel('D:/劳动力信息采集表.xlsx',sheet_name='工种分类',header =0)
>>> gz.shape
(665, 3)
>>> gx.head(3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    gx.head(3)
NameError: name 'gx' is not defined
>>> gz.head(3)
      大类     子类一      子类二
0  单位负责人  企业管理人员     部门经理
1    NaN     NaN  生产或经营经理
2    NaN     NaN     财务经理
>>> gz.head(20)
         大类     子类一         子类二
0     单位负责人  企业管理人员        部门经理
1       NaN     NaN     生产或经营经理
2       NaN     NaN        财务经理
3       NaN     NaN        行政经理
4       NaN     NaN        人事经理
5       NaN     NaN     销售和营销经理
6       NaN     NaN     广告和公关经理
7       NaN     NaN        采购经理
8       NaN     NaN     计算机服务经理
9       NaN     NaN     研究和开发经理
10      NaN     NaN        餐厅经理
11      NaN     NaN        客房经理
12      NaN     NaN       采购部经理
13      NaN     NaN        项目经理
14      NaN     NaN    其他企业管理人员
15  专业、技术人员    科研人员        科研人员
16      NaN  工程技术人员  地质勘探工程技术人员
17      NaN     NaN    测绘工程技术人员
18      NaN     NaN       测绘技术员
19      NaN     NaN    矿山工程技术人员
>>> chang = len(gz)
>>> i = 0
>>> lie = list(range(chang))
>>> for dl in gz.大类.astype(str):
        if dl==np.nan:
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
>>> lie[0:3]
['单位负责人', 'nan', 'nan']
>>> i = 0
>>> for dl in gz.大类.astype(str):
        if(dl==np.nan):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
>>> lie[0:6]
['单位负责人', 'nan', 'nan', 'nan', 'nan', 'nan']
>>> i = 0
>>> for dl in gz.大类:
        if(dl==np.nan):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
>>> lie[0:6]
['单位负责人', nan, nan, nan, nan, nan]
>>> i = 0
>>> for dl in gz.大类:
        if(dl.isnull()):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    if(dl.isnull()):
AttributeError: 'str' object has no attribute 'isnull'
>>> for dl in gz.大类:
        if(dl==pd.NA):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    if(dl==pd.NA):
  File "pandas\_libs\missing.pyx", line 360, in pandas._libs.missing.NAType.__bool__
TypeError: boolean value of NA is ambiguous
>>> for dl in gz.大类.astype(str):
        if(dl==''):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
>>> lie[0:6]
['单位负责人', 'nan', 'nan', 'nan', 'nan', 'nan']
>>> i=0
>>> for dl in gz.大类.astype(str):
        if(pd.isnull(dl)):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1

        
>>> lie[0:6]
['单位负责人', 'nan', 'nan', 'nan', 'nan', 'nan']
>>> for dl in gz.大类.astype(str):
        if(pd.isnull(dl)):
                lie[i]=lie[i-1]
                print(lie[i-1])
        else:
                lie[i]=dl
        i=i+1

        
Traceback (most recent call last):
  File "<pyshell#41>", line 6, in <module>
    lie[i]=dl
IndexError: list assignment index out of range
>>> i=0
>>> for dl in gz.大类.astype(str):
        if(pd.isnull(dl)):
                lie[i]=lie[i-1]
                print(lie[i-1])
        else:
                lie[i]=dl
        i=i+1

        
>>> i=0
>>> for dl in gz.大类:
	#print(dl)
        if(pd.isnull(dl)):
                lie[i]=lie[i-1]
                print(lie[i-1])
        else:
                lie[i]=dl
        i=i+1

        
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人
单位负责人

其他
其他
>>> gz.head(3)
      大类     子类一      子类二
0  单位负责人  企业管理人员     部门经理
1    NaN     NaN  生产或经营经理
2    NaN     NaN     财务经理
>>> gz.大类 = lie
>>> gz.head(3)
      大类     子类一      子类二
0  单位负责人  企业管理人员     部门经理
1  单位负责人     NaN  生产或经营经理
2  单位负责人     NaN     财务经理
>>> chang = len(gz)
>>> i = 0
>>> lie = list(range(chang))
>>> for zl_1 in gz.子类一:
        if(pd.isnull(zl_1)):
                lie[i]=lie[i-1]
        else:
                lie[i]=zl_1
        i=i+1

>>> gz.子类一 = lie
>>> gz.head(3)
      大类     子类一      子类二
0  单位负责人  企业管理人员     部门经理
1  单位负责人  企业管理人员  生产或经营经理
2  单位负责人  企业管理人员     财务经理
>>> gz['大大类']=gz.大类.str + gz.子类一.str +gz.子类二.str
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    gz['大大类']=gz.大类.str + gz.子类一.str +gz.子类二.str
TypeError: unsupported operand type(s) for +: 'StringMethods' and 'StringMethods'
>>> gz['大大类']=gz.大类.str&gz.子类一.str&gz.子类二.str
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    gz['大大类']=gz.大类.str&gz.子类一.str&gz.子类二.str
TypeError: unsupported operand type(s) for &: 'StringMethods' and 'StringMethods'
>>> import str
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    import str
ModuleNotFoundError: No module named 'str'
>>> import string
>>> gz['大大类']=gz.大类.str + gz.子类一.str +gz.子类二.str
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    gz['大大类']=gz.大类.str + gz.子类一.str +gz.子类二.str
TypeError: unsupported operand type(s) for +: 'StringMethods' and 'StringMethods'
>>> gz['大大类']=gz.大类 + gz.子类一 +gz.子类二
>>> gz.head(10)
      大类     子类一      子类二                 大大类
0  单位负责人  企业管理人员     部门经理     单位负责人企业管理人员部门经理
1  单位负责人  企业管理人员  生产或经营经理  单位负责人企业管理人员生产或经营经理
2  单位负责人  企业管理人员     财务经理     单位负责人企业管理人员财务经理
3  单位负责人  企业管理人员     行政经理     单位负责人企业管理人员行政经理
4  单位负责人  企业管理人员     人事经理     单位负责人企业管理人员人事经理
5  单位负责人  企业管理人员  销售和营销经理  单位负责人企业管理人员销售和营销经理
6  单位负责人  企业管理人员  广告和公关经理  单位负责人企业管理人员广告和公关经理
7  单位负责人  企业管理人员     采购经理     单位负责人企业管理人员采购经理
8  单位负责人  企业管理人员  计算机服务经理  单位负责人企业管理人员计算机服务经理
9  单位负责人  企业管理人员  研究和开发经理  单位负责人企业管理人员研究和开发经理
>>> wd = pd.read_excel('D:/古县建档立卡贫困劳动力稳定就业人员花名单.xlsx')
>>> wd.head(3)
           户籍地址  区县 乡(镇)   行政村  自然村  ... 是否解决安全饮用水    人均纯收入 特殊人群标识  特殊人群标识2 特殊人群标识3
0  古县北平镇党家山村党家山  古县  北平镇  党家山村  党家山  ...         是   7600.0  一般脱贫户      NaN     NaN
1  古县北平镇党家山村党家山  古县  北平镇  党家山村  党家山  ...         是   4760.0  一般脱贫户      NaN     NaN
2  古县北平镇党家山村党家山  古县  北平镇  党家山村  党家山  ...         是  11500.0  一般脱贫户      NaN     NaN

[3 rows x 100 columns]
>>> wd.columns.values
array(['户籍地址', '区县', '乡(镇)', '行政村', '自然村', '居住地址', '迁入地址', '采集日期', '序号',
       '姓名', '18位身份证号', '死亡情况', '婚姻状况', '民族', '户口性质', '文化程度', '毕业院校',
       '所学专业', '毕业日期', '健康状况', '身份证号', '手机号码', '年收入(元)', '就业失业类型', '单位类型',
       '单位名称', '就业工种', '就业工种2', '就业工种3', '单位地址', '劳动合同', '是否劳务输入',
       '人力资源机构名称', '机构性质', '创业类型', '享受扶持政策', '是否返乡创业', '灵活就业类型',
       '新业态就业类型', '失业类型', '失业原因', '原单位名称', '失业时间', '原工种', '原工种2', '原工种3',
       '未就业原因', '求职意愿', '求职行业', '求职工种', '求职工种2', '求职工种3', '求职地点', '期望薪资',
       '劳务输入意愿', '输出方式', '输出意向地', '输出薪资', '是否有培训经历', '培训日期', '培训机构',
       '培训工种', '工种等级', '培训意愿', '意愿培训日期', '意愿培训地点', '意愿培训工种', '意愿培训工种2',
       '意愿培训工种3', '意愿工种等级', '有无专业技术职称信息', '专业技术职称', '层级', '获取时间', '聘任状态',
       '有无职业技能信息', '证书类别', '证书工种名称', '证书等级', '证书获取时间', '证书编号', '技能大赛获奖信息',
       '贫困户属性', '脱贫属性', '脱贫年度', '首次识别时间', '贫困人员识别时间', '致贫原因1', '户编号',
       '与户主关系', '在校生状况', '劳动技能', '务工状况', '参加大病医疗', '危房户', '是否解决安全饮用水',
       '人均纯收入', '特殊人群标识', '特殊人群标识2', '特殊人群标识3'], dtype=object)
>>> wd['大大类']=wd.单位名称+wd.就业工种+wd.就业工种2+wd.就业工种3
>>> wd.head(3)
           户籍地址  区县 乡(镇)   行政村  自然村  ...    人均纯收入 特殊人群标识 特殊人群标识2  特殊人群标识3  大大类
0  古县北平镇党家山村党家山  古县  北平镇  党家山村  党家山  ...   7600.0  一般脱贫户     NaN      NaN  NaN
1  古县北平镇党家山村党家山  古县  北平镇  党家山村  党家山  ...   4760.0  一般脱贫户     NaN      NaN  NaN
2  古县北平镇党家山村党家山  古县  北平镇  党家山村  党家山  ...  11500.0  一般脱贫户     NaN      NaN  NaN

[3 rows x 101 columns]
>>> wd['大大类'].head(3)
0    NaN
1    NaN
2    NaN
Name: 大大类, dtype: object
>>> wd['大大类']=wd.单位名称+wd.就业工种
>>> wd['大大类'].head(3)
0    蔺润煤业工人
1    货运公司司机
2    蔺润煤业工人
Name: 大大类, dtype: object
>>> wd['大大类']=wd.单位名称.astype(str)+wd.就业工种.astype(str)+wd.就业工种2.astype(str)+wd.就业工种3.astype(str)
>>> wd['大大类'].head(3)
0    蔺润煤业工人nannan
1    货运公司司机nannan
2    蔺润煤业工人nannan
Name: 大大类, dtype: object
>>> chang = len(wd)
>>> a=0
>>> i=0
>>> lie = list(range(chang))
>>> for oldddl in wd.大大类.astype(str):
        a = 0
        for newddl in gz['大大类'].astype(str):
                temp = Levenshtein.ratio(oldddl,newddl)
                if temp>a:
                        a=temp
                        lie[i]=newddl
        print(lie[i])
        i=i+1

        
专业、技术人员工程技术人员测绘技术员
生产运输工人运输设备操作人员及有关人员A照司机
专业、技术人员工程技术人员测绘技术员
生产运输工人建筑和工程施工人员管工
专业、技术人员工程技术人员测绘技术员

专业、技术人员教学人员中学教师
>>> wd['标准工种']=lie
>>> wd.to_excel('D:/稳定就业标准工种.xlsx',index = False)
>>> i=0
>>> for oldddl in wd.就业工种.astype(str):
        a = 0
        for newddl in gz['大大类'].astype(str):
                temp = Levenshtein.ratio(oldddl,newddl)
                if temp>a:
                        a=temp
                        lie[i]=newddl
        i=i+1

        
>>> wd['标准工种']=lie
>>> wd.to_excel('D:/稳定就业标准工种.xlsx',index = False)
>>> 
