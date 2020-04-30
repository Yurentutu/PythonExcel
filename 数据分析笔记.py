import numpy as np
import pandas as pd
import re
import openpyxl
import Levenshtein







'''
import numpy as np
import pandas as pd
import re

#判断字串相似度
Levenshtein.ratio(str1,str2)
chang = len(jx)#手填表表长
a=0
i=0
lie = list(range(chang))#暂存数组
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



#########################################################
chang = len(gz)
i = 0
lie = list(range(chang))
for dl in gz.大类:
        if(pd.isnull(dl)):
                lie[i]=lie[i-1]
        else:
                lie[i]=dl
        i=i+1
gz.大类 = lie


chang = len(gz)
i = 0
lie = list(range(chang))
for zl_1 in gz.子类一:
        if(pd.isnull(zl_1)):
                lie[i]=lie[i-1]
        else:
                lie[i]=zl_1
        i=i+1
gz.子类一 = lie

gz['大大类']=gz.大类 + gz.子类一 +gz.子类二

>>> wd['大大类']=wd.单位名称+wd.就业工种
>>> wd['大大类'].head(3)
0    蔺润煤业工人
1    货运公司司机
2    蔺润煤业工人

>>> wd['大大类']=wd.单位名称.astype(str)+wd.就业工种.astype(str)+wd.就业工种2.astype(str)+wd.就业工种3.astype(str)
>>> wd['大大类'].head(3)
0    蔺润煤业工人nannan
1    货运公司司机nannan
2    蔺润煤业工人nannan

################################################################

#加载数据
df = pd.read_excel('c:/a/b.xlsx')
#print(df)
#加载并设置列索引，行索引，设置好列索引后，其上行被抛弃，设置好目标列为行索引后，其左列被抛弃，在写入表时，行索引也会被抛弃
df_JX = pd.read_excel('C:/金鑫.xls',header=2,index_col=None)
df_JX = pd.read_excel('C:/金鑫.xls',sheet_name='',header=2,index_col=0)
df = pd.read_excel('c:/a/b.xlsx',names=['','',''])
df = pd.read_excel('c:/a/b.xlsx',header=0,names=['','',''])#会覆盖0行的原有列名
#丢掉表2不需要的列
df2 = df1500.loc[:,['乡镇','行政村','系统户主姓名','身份证号','迁入地址']]
#源表没有列名行
df = pd.read_excel('c:/a/b.xlsx',header=None)#列名设置为默认列名01234
#加载数据1
df = pd.DataFrame(pd.read_excel('c:/a/b.xlsx'))
#写入数据
s = pd.Series([1,3,4,np.nan,6,8])#Series()的参数为一个列表，数组？
dates = pd.date_range('20130101',periods = 6)#生成日期数组
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])#DataFrame(值,index=['数组'],columns=['数组'])
df = pd.DataFrame(np.arange(12).reshape((3,4)))#index和columns的值为默认值.只给出矩阵值.
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))#
df = pd.DataFrame({'A':1.,
		   'B':pd.Timestamp('20130102'),
		   'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		   'D':np.array([3]*4,dtype='int32'),
		   'E':pd.Categorical(['test','train','test','train']),#这个是最最普通的方式。
		   'F':'fool'}) #参数为{col_1:b,col_2:d,col_3:f}字典




#调整列的顺序
df = df[['18位身份证号','乡(镇)', '行政村', '姓名','迁入地址']]#将18位身份证号调到了首列
#调整单列的顺序
ID = df.18位身份证号
df = df.drop('18位身份证号',axis =1)
df.insert(0,'18位身份证号',ID)





#去重
ChongFu =  HuiZong.drop_duplicates(subset='18位身份证号',keep='first',inplace = True)#留副本
HuiZong.drop_duplicates(subset='18位身份证号',keep='first',inplace = True)#不留副本




#重新设置列名
df.columns=[ '乡(镇)', '行政村', '姓名','18位身份证号','迁入地址']
df.columns=['','','']#
df = df.reindex(columns=['','','',''])#列索引
#重新设置索引
df.set_index('18位身份证号',inplace = True)
df.set_index('序号')#设置序号列为行索引
df = df.reindex()#重设为默认行索引,原来的行索引成为第一列
df = df.reindex(drop = True)#原来的行索引被删除
df.reindex(inplace = True,drop = True)
df = df.reindex(['','','',''],drop = False)#行索引
#修改列名
df.rename({0:'Name'},inplace=True)
#删除列名中的空格
df.rename(columns = lambda x: x.strip())
df.rename(columns = lambda x:x.replace('$',''),inplace=True)
addSiWang.rename(columns = lambda x: x.replace('_x',''),inplace=True)







#查看行数和列数
df.shape
#查看列名,数据类型等整体信息
df.info()
df.index#查看行名
df.columns#查看列名
#打印列名不全使用
addSiWang.columns.values
#打印表，列名显示不全使用
pd.set_option('display.max_columns',None)
df.dtypes#查看所有列的数据类型
df['列名']#查看该列数据类型
df.values#查看表的数据值
df.values=array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'fool'],
                [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'fool'],
                [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'fool'],
                [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'fool']],
               dtype=object)
df.head(3)#查看前3行数据
df.head(3)['列名']#查看前3行某列的值
df.tail(3)#查看最后3行数据
#查看空值
df.isnull()
df['列名'].isnall()#查看某列空值
#查看符合条件的数据
df[(df.收入==0)|(df.收入=='无收入')]
df[(df.收入>0)&(df.收入<3000)]
df[df.学历=='本科'].head(10)
df[df.采集日期.astype(str)=='20200325'].head(10)
#查看符合条件的数据2
isUni = df['学历'].str.contains('大学')
df[isUni]
df[df.str.contains('大学')]
#定位查看
df['A']#查看A列
df.A#查看A列
df[0:3]#查看0-3行
df['20130102':'20130104']#查看102到104中间的行
df.loc['20130102']#定位该行
df.loc[:,['A','B']]#定位所有行的A列和B列
df.iloc[[1,3,5],1:3]#定位1,3,5行，1-3列
df.ix[:3,['A','C']]#定位前三行，A列和C列
df[df.A>8]#定位A列大于8的行










#新增一列
df['F']=np.nan#新增列
df['F']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
df['group']= np.where(df['收入']>0,'有收入','无收入')
df.loc[(df['收入']>0)&(df['收入']<=3000),'收入分级']='0-3千元'
df.loc[df.收入<3000,'收入']='0-3000元'





#替换空字符串为空值，其中r''为正则表达式，\s表示空白字符，匹配任何空白字符，*$表示任意个空白字符
df.replace(to_replace=r'^\s*$',value=np.nan,regex=True,inplace=True)
#填充空值为其他数据
df.fillna(value=0)#使用数字0填充数据表中的空值。
df3['姓名_x'].fillna(df3['姓名_y'],inplace = True)#使用完merge后需要用
#删除某几列为空值的行
df=df.dropna(subset=['身份证号','姓名'])
df.dropna(axis=0,how='all')#删除空值所在行，axis=0为删除行，axis=1为删除列，how=any为有一个空值就删，how=all为全为空值就删
#删除某行
df.drop('index')
df.drop(['index1','index2','index3'])
df.drop([0,4])
#删除某列包含特殊字符的行
df = df[~df['就业状况'].str.contain('稳定就业')]
#删除某列
df.drop(['col_1'],axis=1,inplace=True)
df.drop(['乡(镇)_y','行政村_y','姓名_y'],axis=1,inplace=True)
#修改身份证号最后一位小写x为大写X

#定位修改
df.iloc[2,2]=1111
df.loc['20130101','B']=2222
df.loc[:,'身份证号'] = df.身份证号.astype('str').str[0:18]#不保留源列
df.loc[:,['A','B']]#定位所有行的A列和B列
df.B[df.A>4]=0
#固定长度分列
df['18位身份证号'] = df.身份证号.astype('str').str[0:18]#保留源列
#词语替换
df.loc[df['学历'].str.contains('初中')|df['学历'].str.contains('小学'),'学历']='初中及以下'
df['学历'].str.replace('一年级','')#部分替换，注意加了.str
df.loc[df.str.contains('大学'),'学历']='本科'
df['学历'].replace('本科一年级','本科')#一对一替换
df['学历'].replace({'本科一年级':'本科','小学一年级':'小学','初中一年级':'初中'},inplace=True)#多对多替换inplace参数的含义为传值还是传址，
df.replace(['大学生','小学僧','中学生'],['本科','小学','初中'])#多对多替换
df.replace(['小学','初中'],'初中及以下')#多对一替换
#正则查找模糊词并替换为标准词，不会，不管用呢？？？？？？？？？？？？
df.replace(to_replace=r'^.*本科.*$',value='本科',regex=True,inplace=True)#参数regex的含义为是否使用正则表达式进行模糊查找












#正则表达式的用法
re_str='^abc'#^匹配字符串开始位置，表示abc,且在一个字符串的开头
re_str='abc$'   # $匹配字符串结尾位置，表示abc,且在一个字符串的结尾
re_str=[abc]#[]内为字符集，对单个字符给出取值范围。表示a、b、c
re_str=[^abc]      #[]内为字符集，对单个字符给出排除范围。表示非a、非b、非c的单个字符
re_str='.'#.表示任何单个字符
re_str='abc?'#?前一个字符0次或1次扩展,表示ab、abc
re_str='abc|def'#|左右表达式任意一个,表示abc、def
# *代表前一个字符出现0次或多次，+代表前面的字符出现1次或多次
re_str='ab{2}c'#{m}扩展前一个字符m次，表示abbc
re_str='ab{1,2}c'#{m,n}扩展前一个字符m至n次(含n),表示abc、abbc
re_str='(abc|def)'#()分组标记，内部只能使用|操作符。








#数据表简单合并
#横向堆叠，要保证两表列名一致，否则跟你想的堆叠会不一样！！！！
pd.concat([df1,df2,df3])#默认axis=0,横向堆叠合并，要指定columns,否则跟你想的横向堆叠不太一样
#纵向堆叠，要保证两表行名一致
pd.concat([df1,df2,df3],axis=1)#纵向堆叠合并，要指定index,否则跟你想的纵向堆叠不太一样
pd.concat([s1*5,s3])#乘5是矩阵运算，数乘的那个乘。
pd.concat([s1,s4],keys={'from_s1','from_s4'})#可以区分合并后的结果
pd.concat([s1,s4],axis=1,join='inner')#取行的交集，共有行
pd.concat([s1,s4],axis=1,join_axes=[['a','c','b','f']])#指定新表的横向索引
#数据表vlooup合并
pd.merge(df1,df2)#未指定合并的列，默认选取两者重复的列k,也可以指定
pd.merge(df1,df2,on='k')
pd.merge(df1,df2,how='outer',on='k')#尽量避免k列有重复值，看的太乱
pd.merge(df1,df2,left_on='身份证号',right_on='证件号码',how='outer')
pd.merge(df1,df2,on=['户籍','姓名','性别'],how='outer')#不行
ZuiZhong = pd.merge(YuanFupin,add_outaddress,on=['区县', '乡(镇)_x', '行政村_x', '自然村', '户编号', '姓名_x', '身份证号',
       '与户主关系', '民族'],how='outer')
pd.merge(df1,df2,on='k',how='outer',suffixes=('from_df1','form_df2'))
pd.merge()
>>> df1 = pd.DataFrame({'k':['s','s','w','x','x','n','f','c'],'data1':range(8)})
>>> df2 = pd.DataFrame({'k':['w','w','s','s','x','f'],'data2':range(6)})
>>> pd.merge(df1,df2)#默认参数how为inner,取重复列的交集
pd.merge(df1,df2,how='outer')#尽量避免k列有重复值，看的太乱
df3 = HuiZong.combine_first(df2)#根据index,df1的空值被df2替代，如果df2的index多于df1，则更新到df1上。
df3 = HuiZong.combine_first(df2)
df3 = df3[['序号', '采集日期', …… '就业工种3']]#使用完combine后需要重新排序







#写入新Excel，需要import openpyxl模块
df.to_excel('c:/a/c.xlsx',index=False)
df.to_excel('c:/a/c.xlsx',index=True)
'''
