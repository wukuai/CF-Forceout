# -*- coding: utf-8 -*- 
import requests
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
ISOTIMEFORMAT='%Y-%m-%d %X'

print unicode('请将待查询QQ号信息存储在本软件根目录in.txt中','utf-8') 
print unicode('支持的查询格式：','utf-8')  
print unicode('1.  1234567-...（-符号后为其它信息）','utf-8')  
print unicode('2.  1234567（纯QQ号）','utf-8')  
print unicode('QQ号长度应为5位-10位','utf-8')
print unicode('查询完毕后未解封账号信息将保存至out1.txt','utf-8')
print unicode('查询完毕后正常状态账号信息将保存至out2.txt','utf-8')
print unicode('       ****即将开始查询****      ','utf-8')       


os.system('pause') 

currenttime=time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))
wjftime=currenttime

url = "http://apps.game.qq.com/cgi-bin/cf/a20090409forceout/getinfo.cgi"

flag=1


def myprint(daqu,files):
    response=requests.post(url,files=files)
    response.encoding = 'gb2312'
    if unicode(str('系统繁忙'),'utf-8') in response.text:
        print unicode(str(line)+str(' 在  ')+str(daqu)+str('  未创建角色'),'utf-8')
    elif unicode(str('正常'),'utf-8') in response.text:
        print unicode(str(line)+str(' 在  ')+str(daqu)+str('  是正常状态！'),'utf-8')
#         out2.write(line+' 在  '+daqu+'  是正常状态！\n')
    elif '>20' in response.text:
        timestr=response.text[response.text.index('>20'):response.text.index('</td>\n</tr>')]
        timestr=timestr.strip('>')
        if str(currenttime)<str(timestr):
            global flag
            flag=0
            global wjftime
            wjftime=timestr
            print unicode(str(line)+str(' 在  ')+str(daqu)+str('  封停期限为  ')+str(timestr)+str('  **未解封**'),'utf-8')
#             out1.write(line+' 在  '+daqu+'  封停期限为  '+timestr+'  **未解封**\n')
        else:
            print unicode(str(line)+str(' 在  ')+str(daqu)+str('  封停期限为  ')+str(timestr)+str('  目前正常'),'utf-8')
#             out2.write(line+' 在  '+daqu+'  封停期限为  '+timestr+'  目前正常\n')
#     else:
#         print unicode(str(line)+str(' 在  ')+str(daqu)+str('  因网络问题未查询成功'),'utf-8')      
    return
 
f = open("in.txt", "r")
out1= open("out1.txt","w")
out2= open("out2.txt","w")


while True:  
    line = f.readline()
    lineyuan=line
    flag=1
    if line:  
        line=line.strip()  
        if '-' in line:
            line=line[:line.index('-')]
        if len(line)>=5:
            print unicode('当前读取QQ号为'+str(line),'utf-8')   
            #分大区查询 

            temp = {'ssn':(None,'320'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('上海电信一区'),'utf-8'),temp)  
            
            temp = {'ssn':(None,'326'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('上海电信二区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'318'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('广东电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'327'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('广东电信二区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'338'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('广东电信三区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'339'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('广东电信四区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'353'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('广西电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'342'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('南方电信大区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'341'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('湖南电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'340'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('湖南电信二区'),'utf-8'),temp) 
             
            hbdx1 = {'ssn':(None,'328'),
                     'Uin':(None,str(line))}
            myprint(str('湖北电信一区'),hbdx1)
            
            hbdx2 = {'ssn':(None,'329'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('湖北电信二区'),'utf-8'),hbdx2)  
                
            zjdx1 = {'ssn':(None,'325'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('浙江电信一区'),'utf-8'),zjdx1)  
             
            zjdx2 = {'ssn':(None,'349'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('浙江电信二区'),'utf-8'),zjdx2) 
            
          


            
            temp = {'ssn':(None,'344'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('江苏电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'357'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('江苏电信二区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'324'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('福建电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'352'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('江西电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'330'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('陕西电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'333'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('四川电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'356'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('四川电信二区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'332'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('重庆电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'347'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('安徽电信一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'348'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('云南电信一区'),'utf-8'),temp) 
       
            temp = {'ssn':(None,'343'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('北方网通大区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'322'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('辽宁网通一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'323'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('辽宁网通二区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'336'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('辽宁网通三区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'350'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('黑龙江网通区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'351'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('吉林网通一区'),'utf-8'),temp) 
            

            
            temp = {'ssn':(None,'319'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('北京网通一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'321'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('北京网通二区'),'utf-8'),temp) 
               
            temp = {'ssn':(None,'334'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('北京网通三区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'335'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('北京网通四区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'346'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('山东网通一区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'358'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('山东网通二区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'354'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('山西网通一区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'345'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('河南网通一区'),'utf-8'),temp) 
            
            temp = {'ssn':(None,'359'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('河南网通二区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'355'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('河北网通一区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'360'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('移动专区'),'utf-8'),temp) 
             
            temp = {'ssn':(None,'361'),
                     'Uin':(None,str(line))}
            myprint(unicode(str('教育网专区'),'utf-8'),temp) 
            
            if(flag):
                out2.write(lineyuan)
            else :
                out1.write(lineyuan.strip('\n')+' '+wjftime+' **未解封**\n')
#             print flag
         
            print " "        
    else:  
        break
# out.write("55456456456456\n")
f.close()
out1.close()
out2.close()
print unicode(str('查询完毕，未解封账号信息已导出到out1.txt！'),'utf-8')
print unicode(str('查询完毕，正常状态账号信息已导出到out2.txt！'),'utf-8')
os.system('pause') 

# print unicode('成功:','utf-8')  

# 上海电信一区320
# 上海电信二区326
# 广东电信一区318
# 广东电信二区327
# 广东电信三区338
# 广东电信四区339
# 广西电信一区353
# 南方电信大区342
# 湖南电信一区341
# 湖南电信二区340
# 湖北电信一区  328
# 湖北电信二区 329
# 浙江电信一区 325
# 浙江电信二区 349

# 江苏电信一区 344
# 江苏电信二区 357
# 福建电信一区324**
# 江西电信一区352
# 陕西电信一区330
# 四川电信一区333
# 四川电信二区356
# 重庆电信一区332
# 安徽电信一区347
# 云南电信一区348


# 北方网通大区343
# 辽宁网通一区322
# 辽宁网通二区323
# 辽宁网通三区336
# 黑龙江网通区350
# 吉林网通一区351
# 北京网通一区319
# 北京网通二区321
# 北京网通三区334
# 北京网通四区335

# 山东网通一区346
# 山东网通二区358
# 山西网通一区354
# 河南网通一区345
# 河南网通二区359
# 河北网通一区355
# 移动专区360
# 教育网专区361
#42


# s = r 'E:/Inetpub/wwwroot/cgi-bin/admin ' 
# if 'cgi-bin ' in s: s = s[:s.index( 'cgi-bin ')] 
# print s 


# 
# i=97491116
# 
# files = {'ssn':(None,'329'),
#              'Uin':(None,str(i))}
# url = "http://apps.game.qq.com/cgi-bin/cf/a20090409forceout/getinfo.cgi"
# response=requests.post(url,files=files)
# response.encoding = 'gb2312'
# print response.text
# print 46546  #coding=utf-8




