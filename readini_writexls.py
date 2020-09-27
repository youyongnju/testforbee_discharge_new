import configparser
import time
import xlwt,xlrd
#import GUI

#读ini文件
def rem_space(value):
    for i in range(len(value)):
        value[i] = value[i].strip()     #去列表内字符串空格
        if value[i]== '':
            value.pop(i)
    return value

config = configparser.ConfigParser() # 类实例化
path = 'config.ini'
config.read(path,encoding='UTF-8')
test_band = config.get('Band','band').split(',')
rem_space(test_band)
test_bandwidth= config.get('Bandwidth','BW').split(',')
rem_space(test_bandwidth)
CMW_addr=config.get('Instrument','CMW Adress').split(',')
rem_space(CMW_addr)

Agilent_66XX_addr=config.get('Instrument','Current Meter Adress').split(',')
rem_space(Agilent_66XX_addr)
volt=config.get('Volt','Volt').split(',')
rem_space(volt)
trace_loss=[]
for i in range(len(test_band)):
    trace_loss.append(config.get('Trace loss','band'+test_band[i]))
RB=config.get('RB number','RB').split(',')
rem_space(RB)







#aclr = '-40,-30,-20,23,-21,-31,-41,600,145,455'
#aclr_1 = aclr.split(',')


#初始化字典
channel,dl_channel,data={},{},{}

for k in volt:
    for i in test_bandwidth:
       for j in test_band:
           channel[k + 'V_' + i + 'M'] =[]
           dl_channel[k + 'V_' + i + 'M'] = []
           data[k + 'V_' + i + 'M'] = []



#生成channel字典
for k in volt:
    for i in test_bandwidth:
       for j in test_band:
          if i=='5':
              ch=config.get('Channel', 'band'+str(j)).split(',')
              channel[k+'V_'+i+'M'].extend(ch[0:3])
          if i=='10':
              ch=config.get('Channel', 'band'+str(j)).split(',')
              channel[k+'V_'+i+'M'].extend(ch[3:6])
          if i == '20':
              ch=config.get('Channel', 'band'+str(j)).split(',')
              channel[k+'V_'+i+'M'].extend(ch[6:9])
              #单个字符串用append， 字符串列表用extend


#生成dl_channel


for i in channel.keys():
    for j in range(len(channel[i])):
        dl_channel[i].append(str(eval(channel[i][j])-18000))
    for k in test_band:
        if k in ['34','38','39','40','41']:
            biaohao=test_band.index(k)
            dl_channel[i][biaohao*3]  =  channel[i][biaohao*3]
            dl_channel[i][biaohao*3+1]  =  channel[i][biaohao*3+1]
            dl_channel[i][biaohao*3+2]  =  channel[i][biaohao*3+2]

'''
#生成测试数据存在data字典
for k in volt:
    for i in test_bandwidth:
        volt_bandwidth = k + 'V_' + i + 'M'
        for j in range(len(dl_channel[volt_bandwidth])):
          # aclr_1=dl_channel[volt_bandwidth][j]
            data[volt_bandwidth].append(aclr_1)
'''




#写excel。。。。。。。。。。。。。。。。。
#if __name__=='__main__':
def writexls(data,RB='fullRB'):
    start = time.time()  # start time of program
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fname = 'ACLR_'+RB+'_Report_' + now + '.xls'

    if RB=='fullRB':
        header = ['Band', 'Channel', 'TX Power', 'UTRA2-', 'UTRA1-', 'E_UTRA1-', \
              'E_UTRA1+', 'UTRA1+', 'UTRA2+', 'Current(max)', 'Current(min)', 'Current(PA)']
    else :
        header = ['Band', 'Channel', 'TX Power', 'UTRA2-', 'UTRA1-', 'E_UTRA1-', \
                  'E_UTRA1+', 'UTRA1+', 'UTRA2+', 'UTRA2-', 'UTRA1-', 'E_UTRA1-', \
                  'E_UTRA1+', 'UTRA1+', 'UTRA2+','Current(max)', 'Current(min)', 'Current(PA)']

    f = xlwt.Workbook()
    #time.sleep(0.1)

    for k in volt:
        for i in test_bandwidth:
            volt_bandwidth = k + 'V_' + i + 'M'
            sheet1 = f.add_sheet(volt_bandwidth, cell_overwrite_ok=True)

            #设置单元格格式
            alignment = xlwt.Alignment() # Create Alignment
            alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
            alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
            style = xlwt.XFStyle() # Create Style
            style.alignment = alignment # Add Alignment to Style
            style.num_format_str = '0'

            # 写第一行
            for j in range( len(header)):
                sheet1.write(0, j , header[j],style)
            #写band
            for j in range(len(test_band)):
                sheet1.write_merge(j*3+1, j*3+3, 0, 0, float(test_band[j]),style)
            #写channel
            for j in range(len(channel[volt_bandwidth])):
                sheet1.write(j+1, 1 , float(channel[volt_bandwidth][j]),style  )
            style.num_format_str = '0.0'
            #写data
            for j in range(len(data[volt_bandwidth])):
                for m in range(10):
                    sheet1.write(j+1, m+2 , float(data[volt_bandwidth][j] [m]) ,style)
            #设列宽
            '''
            for j in range( len(header)):
                sheet1.col(j).width = len(header[j]) * 250
                if len(header[j])<9:
                    sheet1.col(j).width = 8*300
            '''
            for j in range( len(header)):
                sheet1.col(j).width = 8 * 350


    f.save(fname)

#writexls(data,RB[0])
