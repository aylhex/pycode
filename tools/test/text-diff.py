#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/12/19

import email  
import mimetypes  
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEText import MIMEText  
from email.MIMEImage import MIMEImage  
import smtplib  
  
def sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText):  
  
        strFrom = fromAdd  
        strTo = ', '.join(toAdd)  
  
        server = authInfo.get('server')  
        user = authInfo.get('user')  
        passwd = authInfo.get('password')  
  
        if not (server and user and passwd) :  
                print 'incomplete login info, exit now'  
                return  
  
        # 设定root信息  
        msgRoot = MIMEMultipart('related')  
        msgRoot['Subject'] = subject  
        msgRoot['From'] = strFrom  
        msgRoot['To'] = strTo  
        msgRoot.preamble = 'This is a multi-part message in MIME format.'  
  
        # Encapsulate the plain and HTML versions of the message body in an  
        # 'alternative' part, so message agents can decide which they want to display.  
        msgAlternative = MIMEMultipart('alternative')  
        msgRoot.attach(msgAlternative)  
  
        #设定纯文本信息  
#        msgText = MIMEText(plainText, 'plain', 'utf-8')  
#        msgAlternative.attach(msgText)  
  
        #设定HTML信息  
        msgText = MIMEText(htmlText, 'html', 'utf-8')  
        msgAlternative.attach(msgText)  
  
       #设定内置图片信息  
#        fp = open('test.jpg', 'rb')  
#        msgImage = MIMEImage(fp.read())  
#        fp.close()  
#        msgImage.add_header('Content-ID', '<image1>')  
#        msgRoot.attach(msgImage)  
  
       #发送邮件  
        smtp = smtplib.SMTP()  
       #设定调试级别，依情况而定  
        smtp.set_debuglevel(1)  
        smtp.connect(server)  
        smtp.login(user, passwd)  
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())  
#        smtp.sendmail(strFrom, strTo, msgRoot.as_string())  
        smtp.quit()  
        return  
  
if __name__ == '__main__' :  
        authInfo = {}  
        authInfo['server'] = 'bjmail.kingsoft.com'  
        authInfo['user'] = 'chenjun2@kingsoft.com'  
        authInfo['password'] = 'NuoYi20131121'  
        fromAdd = 'hhaa@kingsoft.com'  
        toAdd = ['chenjun2@kingsoft.com','chenjun1@ijinshan.com']  
        subject = 'test'  
        plainText = '这里是普通文本'  
        htmlText = """<STYLE type="text/css">  <!--@import url(scrollbar_3576.css); -->
        BODY { font-size: 14px; line-height: 1.5  } </STYLE><HEAD><META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
        </HEAD><div style="font-family:微软雅黑,Verdana; font-size:12pt; color:black">各位好，以下是&nbsp;<strong>12月20日 5:00 - 9:00</strong>
        &nbsp;时间段内，从kisdump数据库统计出的各产品 top3崩溃模块统计数据。</div><div style="font-family:微软雅黑,Verdana; font-size:12pt; color:black">
        <h5>毒霸 2012</h5>总dump上报数: 3520<br/></div><table border="1" style="font-size:75%;font-family:微软雅黑,Verdana;"> <tr><td>dump上报数
        </td><td>模块</td><td>崩溃版本</td><td>崩溃进程</td></tr><tr><td>267&nbsp;(7.59%)</td><td>kfloatwin</td><td>2013.12.16.128（173）； 
        0.0.0.0（47）； 2013.12.12.98（15）； 2013.12.10.8102（10）； 2013.12.15.121（10）； 2013.12.11.87（7）； 2013.12.14.120（2）； 2013.12.17.146（
        1）； 2013.12.18.153（1）； 2013.11.14.7690（1）； 2013.12.10.64（1）； </td><td>kxetray.exe（267）； </td></tr><tr><td>241&nbsp;(6.85%)</td
        ><td>kdgui2</td><td>2013.11.27.66（435）； 2013.12.18.69（77）； 2013.11.8.63（1）； </td><td>kxetray.exe（241）； </td></tr><tr><td>190&
        nbsp;(5.40%)</td><td>gr32</td><td>&lt;1970-01-01 08:00:00&gt;（203）； &lt;1970-03-19 16:52:51&gt;（25）； </td><td>kxetray.exe（190）； 
        </td></tr></table><br/><br/><div style="font-family:微软雅黑,Verdana; font-size:12pt; color:black"><h5>金山卫士</h5>总dump上报数: 780<br/>
        </div><table border="1" style="font-size:75%;font-family:微软雅黑,Verdana;"> <tr><td>dump上报数</td><td>模块</td><td>崩溃版本</td><td>
        崩溃进程</td></tr><tr><td>118&nbsp;(15.13%)</td><td>ksesscan</td><td>2012.6.9.2（118）； </td><td>KSafeSvc.exe（118）； </td></tr><tr>
        <td>66&nbsp;(8.46%)</td><td>ksftray</td><td>4.7.0.4086（22）； 4.6.0.3633（13）； 4.6.0.3674（11）； 4.7.0.4081（7）； 4.7.0.4037（3）； 4.2.0.2537（3）；
        0.0.0.0（2）； 4.7.10.3524（1）； 4.2.0.2553（1）； 4.6.0.3561（1）； 4.6.0.3568（1）； 4.6.0.3570（1）； 4.7.0.4078（1）； </td><td>KSafeTray.exe（66）； </td>
        </tr><tr><td>46&nbsp;(5.90%)</td><td>KSafeTray</td><td>3.3.1.1822（17）； 3.4.0.1914（15）； 3.7.0.52（4）； 3.3.2.1856（2）； 4.0.7.2408（2）； 4.0.7.2463（1）； 
        3.1.1.1608（1）； 3.3.2.1860（1）； 3.3.1.9（1）； 3.7.0.55（1）； 3.7.0.45（1）； </td><td>KSafeTray.exe（46）； </td></tr></table><br/><br/><div style="font-family:微软雅黑,
        Verdana; font-size:12pt; color:black"><h5>金山浏览器</h5>总dump上报数: 17965<br/></div><table border="1" style="font-size:75%;font-family:微软雅黑,Verdana;"> <tr><td>dump上报数
        </td><td>模块</td><td>崩溃版本</td><td>崩溃进程</td></tr><tr><td>7374&nbsp;(41.05%)</td><td>chrome</td><td>4.3.29.6063（1698）； 4.3.30.6142（1655）； 
        4.3.29.6059（1183）； 4.3.33.6561（668）； 4.5.34.6492（472）； 4.5.35.6563（250）； 4.3.32.6482（245）； 4.3.28.5991（223）； 4.3.29.6058（182）； 4.0.23.5095（144）； 4.5.34.6502（120）； 
        4.3.28.5985（76）； 4.5.36.6613（62）； 4.3.33.6499（52）； 4.3.32.6344（52）； 4.5.34.6570（49）； 4.3.33.6457（38）； 4.1.24.5252（27）； 3.4.18.4294（24）； 4.5.35.6604（22）； 4.0.23.5076（17）； 
        4.0.23.5092（13）； 4.3.32.6441（13）； 3.8.22.4810（9）； 1.2.6.2578（8）； 3.3.17.4145（7）； 4.3.30.6135（6）； 4.2.25.5488（5）； 4.3.27.5837（5）； 3.6.20.4527（5）； 1.3.8.2791（5）；
        3.6.20.4531（4）； 4.3.27.5822（4）； 4.2.25.5498（4）； 4.3.27.5839（3）； 4.3.29.6056（3）； 4.3.29.6443（3）； 3.8.22.4801（3）； 3.3.17.4147（3）； 3.0.14.3725（3）； 3.2.16.4048（3）； 
        3.0.14.3720（2）； 3.2.16.4032（2）； 1.3.8.2777（2）； 2.1.11.3343（2）； 3.6.20.4523（2）； 3.6.20.4525（2）； 3.6.20.4526（2）； 4.0.23.5072（2）； 4.2.25.5477（2）； 
        4.3.33.6435（2）； 4.3.31.6202（2）； 4.3.32.6341（2）； 4.3.27.5829（2）； 4.1.24.5236（2）； 4.0.23.5080（2）； 4.0.23.5082（2）； 4.0.23.5091（1）； 4.1.24.5232（1）； 
        4.3.27.5832（1）； 4.3.27.5818（1）； 4.2.25.5396（1）； 4.2.25.5417（1）； 4.0.23.5054（1）； 3.7.21.4667（1）； 3.8.22.4771（1）； 3.8.22.4785（1）； 3.8.22.4797（1）； 
        3.4.18.4300（1）； 3.5.19.4387（1）； 3.5.19.4391（1）； 3.5.19.4394（1）； 3.5.19.4397（1）； 2.1.11.3347（1）； 2.1.11.3355（1）； 2.1.11.3360（1）； 1.3.8.2790（1）； 1.5.9.2903（1）； 
        3.2.16.4033（1）； 3.2.16.4042（1）； 3.0.14.3727（1）； 3.0.14.3728（1）； 3.2.16.4030（1）； </td><td>liebao.exe（7374）； </td></tr><tr><td>840&nbsp;(4.68%)</td><td>GdiPlus</td>
        <td>5.2.6002.23084（738）； 5.2.6002.22791（51）； 5.2.6002.22509（23）； 6.1.7601.17825（12）； 6.1.7601.18120（6）； 5.1.3102.5512（4）； 5.1.3102.2180（3）； 
        6.1.7600.17007（3）； 5.2.6001.22319（2）； </td><td>KSbrowser_4.3.32.6482.exe（4）； KSbrowser_4.5.36.6613.exe（2）； lb.exe（1）； </br>liebao.exe（833）； 
        </td></tr><tr><td>691&nbsp;(3.85%)</td><td>liebao_10000000</td><td>4.3.30.6142（159）； 4.3.33.6561（139）； 4.3.29.6059（120）； 4.3.29.6063（111）； 4.3.32.6482（36）； 
        4.5.34.6502（22）； 4.3.28.5991（20）； 4.0.23.5095（18）； 4.5.35.6563（14）； 4.5.36.6613（11）； 4.5.34.6570（8）； 4.3.33.6457（7）； 4.3.29.6058（7）； 4.3.33.6499（5）； 
        4.5.35.6604（5）； 4.2.25.5498（3）； 4.3.32.6344（2）； 4.3.32.6441（1）； 4.3.30.6135（1）； 4.3.27.5829（1）； 4.3.28.5985（1）； 4.1.24.5252（1）； 4.0.23.5091（1）； 
        4.0.23.5092（1）； </td><td>（1）； liebao.exe（690）； </td></tr></table><br/><br/><div style="font-family:微软雅黑,Verdana; font-size:12pt; color:black"><br/><p>详细数据查询： http://kisdump.s.kingsoft.net/</p></div>"""  
        sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText)  