import time
from Visa_Process import *
import os
import sys
import xlwt
from INST_CMW500 import *
from Agilent_DCsource_66XX import *
import readini_writexls



def measure():

    #test_band = list(set([int(test_band_info[i]) for i in range(len(test_band_info))]))  # [1,2,3,4,5,...]
    test_band=readini_writexls.test_band
    print('Test band is band',test_band)
    #test_bandwidth = list(set([int(test_bandwidth_info[i]) for i in range(len(test_bandwidth_info))]))  # [5,10,15,20]
    test_bandwidth=readini_writexls.test_bandwidth
    print('Test bandwidth is ',test_bandwidth,'MHz')
    CMW_addr = readini_writexls.CMW_addr[0]
    print('cmw adress is',CMW_addr)
    Agilent_66XX_addr = readini_writexls.Agilent_66XX_addr[0]
    print('current meter adress is',Agilent_66XX_addr)
    volt=readini_writexls.volt
    dl_channel=readini_writexls.dl_channel
    trace_loss = readini_writexls.trace_loss
    data=readini_writexls.data
    RB=readini_writexls.RB


    def exchange_ACLR(aclr_1):   #修改aclr1里power和aclr顺序
        aclr_2 = []
        aclr_2.append(aclr_1[4])
        aclr_2.extend(aclr_1[1:])
        aclr_2.pop(4)
        return (aclr_2)


    #测试流程。。。。。。。。。。。。。。。。。
    start = time.time()  # start time of program
    CMW = INST_CMW500(CMW_addr)
    if Agilent_66XX_addr!='0':
        DC_Source = Agilent_DCsource_66XX(Agilent_66XX_addr)
        DC_Source.config_volt_current('3.8')


    CMW.mode_preset()
    CMW.config_DL_level(-70)
    CMW.TRX_port_config('RF1C')
    CMW.DL_mode(test_band[0])
    CMW.config_Band_channel(test_band[0])
    CMW.switch_on_cmw()
    CMW.setup_connection()
    CMW.meas_condition_on()
    CMW.CMW_trig_source('FrameTrigger')
    CMW.CMW_MEAS_rep('CONT')

    # 生成测试数据存在data字典
    for k in volt:
        for i in test_bandwidth:
            volt_bandwidth = k + 'V_' + i + 'M'
            for j in range(len(dl_channel[volt_bandwidth])):
                if  eval(dl_channel[volt_bandwidth][j]) <=0:  #处理band8没有20M
                    data[volt_bandwidth].append([0,0,0,0,0,0,0,0,0,0])
                    continue
                if Agilent_66XX_addr != '0':
                    DC_Source.config_volt_current(k)
                CMW.CMW_TPC('MAXP')
                CMW.TRX_ext_atten(trace_loss[j//3])
                CMW.intra_handover(test_band[j//3],dl_channel[volt_bandwidth][j],i)

                if RB=='fullRB':
                    config_RB(i, RB, 'low')
                    aclr = CMW.meas_aclr('CURR')
                    aclr_1 = aclr.split(',')
                    aclr_1=exchange_ACLR(aclr_1)
                    data[volt_bandwidth].append(aclr_1)
                else:
                    config_RB(i, RB, 'low')
                    aclr = CMW.meas_aclr('CURR')
                    aclr_1 = aclr.split(',')
                    aclr_1 = exchange_ACLR(aclr_1)
                    data[volt_bandwidth].append(aclr_1)

                    config_RB(i, RB, 'high')
                    aclr = CMW.meas_aclr('CURR')
                    aclr_1 = aclr.split(',')
                    aclr_1 = exchange_ACLR(aclr_1)
                    data[volt_bandwidth].append(aclr_1)

                if Agilent_66XX_addr != '0':
                    Curr1 = DC_Source.meas_current()
                    data[volt_bandwidth][j].append(Curr1)
                    CMW.CMW_TPC('CLO','-30')
                    time.sleep(1)
                    Curr2 = DC_Source.meas_current()
                    data[volt_bandwidth][j].append(Curr2)
                    delta_curr=Curr1-Curr2
                    data[volt_bandwidth][j].append(delta_curr)


    readini_writexls.writexls(data,RB)






    #CMW.switch_off_cmw()  # close CMW500
    #DC_Source.DCsource_close()

    CMW.close()  # visa close
    if Agilent_66XX_addr != '0':
        DC_Source.close()



    end = time.time()
    print('Total test time is about %s seconds' % round((end-start),3))
    #input()








