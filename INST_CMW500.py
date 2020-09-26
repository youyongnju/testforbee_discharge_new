import os
import re
import sys

sys.path.append("../../")
from Visa_Process import *


class INST_CMW500(Visa_Process):
    def __init__(self, inst_addr = 'GPIB0::20::0::INSTR'):
        super(INST_CMW500, self).__init__()
        self.instrument_connection_config(obj_instrument_link=inst_addr,timeout_ms=5000)
        #self.instr_address=inst_addr
        #self.open()
        self.CMW500 = self.conn_instrument_instance
        idn = self.CMW500.query('*IDN?')
        print('%s is existed!' %(idn[0:len(idn)-2]))


    def mode_preset(self):
        ini = ['*RST', '*CLS']
        for i in ini:
            self.CMW500.write(i)  # initialize the pwr source

    # Select duplex mode FDD, automatic SCC activation mode and disable audio tests
    def DL_mode(self, band = '1',SCC_AutoMode = 'AUTO', AudioMode = 'OFF'):
        mode='FDD'
        if band in ['34','38','39','40','41']:
            mode='TDD'
        self.CMW500.write('CONFigure:LTE:SIGN:DMODe ', mode)
        self.CMW500.write('CONFigure:LTE:SIGN:SCC:AMODe ', SCC_AutoMode)
        self.CMW500.write('CONFigure:LTE:SIGN:ESCode ', AudioMode)

    #
    def TRX_port_config(self, trport = 'RF1C'):
        self.CMW500.write('ROUTe:LTE:SIGN:SCENario:SCELl %s,RX1,%s,TX1' % (trport, trport))

    def TRX_ext_atten(self, atten = 1):
        self.CMW500.write('CONFigure:LTE:SIGN:RFSettings:EATTenuation:OUTPut ', str(atten))
        self.CMW500.write('CONFigure:LTE:SIGN:RFSettings:EATTenuation:INPut ', str(atten))

    def switch_on_cmw(self):
        self.CMW500.write('SOURce:LTE:SIGN:CELL:STATe ON')
        self.CMW500.write('CONFigure:LTE:MEAS:MEValuation:MSUBframes 0,10,2')
        while True:
            status = self.CMW500.query('SOURce:LTE:SIGN:CELL:STATe:ALL?')
            if(status == "ON,ADJ\n"):
                print('CMW500 LTE signaling is ON!')
                break

    def switch_off_cmw(self):
        self.CMW500.write('SOURce:LTE:SIGN:CELL:STATe OFF')
        status = self.CMW500.query('SOURce:LTE:SIGN:CELL:STATe?')
        if status[0:3] == 'OFF':
            print('CMW500 LTE signaling is OFF!')
        else:
            print('CMW500 LTE signaling is still ON, please switch off!')

    def setup_connection(self):
        time.sleep(0.5)
        while True:
            conn_status = self.CMW500.query('FETCh:LTE:SIGN:PSWitched:STATe?')
            if(conn_status == 'ATT\n') or (conn_status == 'CEST\n'):
                break
        print('UE is connected to CMW500')
        self.CMW500.write('CALL:LTE:SIGN:PSWitched:ACTion CONNect')
        while True:
            conn_estability_status = self.CMW500.query('FETC:LTE:SIGN:PSW:STAT?')
            if(conn_estability_status == 'CEST\n'):
                print('Connection Establish is OK!')
                break

    def config_DL_level(self, dl_level = -70):
        self.CMW500.write('CONFigure:LTE:SIGN:DL:PCC:RSEPre:LEVel ', str(dl_level))
        self.CMW500.write('CONFigure:LTE:SIGN:DL:PCC:PSS:POFFset -3')
        self.CMW500.write('CONFigure:LTE:SIGN:DL:PCC:SSS:POFFset -3')
        self.CMW500.write('CONFigure:LTE:SIGN:DL:PCC:PBCH:POFFset 0')
        self.CMW500.write('CONFigure:LTE:SIGN:DL:PCC:PCFich:POFFset 0')
        self.CMW500.write('CONFigure:LTE:SIGN:DL:PCC:PDCCh:POFFset -3')

    def config_Band_channel(self,band = 1, freq = 1950e6, bw = 5e6):
        self.CMW500.write('CONFigure:LTE:SIGN:PCC:BAND OB', str(band))
        '''
        # self.CMW500.write('CONFigure:LTE:SIGN:RFSettings:PCC:CHANnel:DL  ', str(chan))
        time.sleep(0.05)
        self.CMW500.write('CONFigure:LTE:SIGN:RFSettings:PCC:FREQ:UL  ', str(freq))
        if bw == 1.4e6:
            bw_idx = 'B014'
        elif bw == 3e6:
            bw_idx = 'B030'
        elif bw == 5e6:
            bw_idx = 'B050'
        elif bw == 10e6:
            bw_idx = 'B100'
        elif bw == 15e6:
            bw_idx = 'B150'
        else:
            bw_idx = 'B200'
        time.sleep(0.05)
        self.CMW500.write('CONFigure:LTE:SIGN:CELL:BANDwidth:PCC:DL ', bw_idx)
        time.sleep(0.05)
        freq_rb = self.CMW500.query('CONFigure:LTE:SIGN:RFSettings:PCC:FREQ:UL?')
        bw_rb = self.CMW500.query('CONFigure:LTE:SIGN:CELL:BANDwidth:PCC:DL?')
        if bw_rb.split()[0] == bw_idx and int(freq_rb) == int(freq):
            print('CMW500 freq %sMHz and bandwidth %sMHz configuration is Ok!' % (freq/1e6, bw/1e6))
        '''
    def config_RB(self,test_bandwidth,RBnumber,RBlocation):
        if test_bandwidth=='5':
            if RBnumber=='fullRB':
                self.CMW500.write('')
            elif RBnumber=='partialRB':
                self.CMW500.write('')
            elif RBnumber=='1RB':
                self.CMW500.write('')
        elif test_bandwidth=='10':
            if RBnumber=='fullRB':
                self.CMW500.write('')
            elif RBnumber=='partialRB':
                self.CMW500.write('')
            elif RBnumber=='1RB':
                self.CMW500.write('')
        elif test_bandwidth=='20':
            if RBnumber=='fullRB':
                self.CMW500.write('')
            elif RBnumber=='partialRB':
                self.CMW500.write('')
            elif RBnumber=='1RB':
                self.CMW500.write('')



    def config_phy_cell(self):
        self.CMW500.write('')
        self.CMW500.write('')
        self.CMW500.write('')
        self.CMW500.write('')

    def intra_handover(self,band = '1', channel = '300', bw = '5'):
        mode='FDD'
        if band in ['34','38','39','40','41']:
            mode='TDD'
   #     self.CMW500.write('PREPare:LTE:SIGN:HANDover:DESTination "LTE Sig1"')
        if bw == '1.4':
            bw_idx = 'B014'
        elif bw == '3':
            bw_idx = 'B030'
        elif bw == '5':
            bw_idx = 'B050'
        elif bw == '10':
            bw_idx = 'B100'
        elif bw == '15':
            bw_idx = 'B150'
        else:
            bw_idx = 'B200'

       # self.CMW500.write('PREP:LTE:SIGN:HAND:ENH ', mode, ' OB'+band, channel, bw_idx, 'NS01')
        print('PREP:LTE:SIGN:HAND:ENH '+mode+', OB' + band+', '+ channel +', '+ bw_idx +', NS01')
        self.CMW500.write('PREP:LTE:SIGN:HAND:ENH '+mode+', OB' + band+', '+ channel +', '+ bw_idx +', NS01')
        self.CMW500.write('CALL:LTE:SIGN:PSWitched:ACTion HANDover')
        time.sleep(1.5)


    def inter_handover(self):
        self.CMW500.write('')
        self.CMW500.write('')
        self.CMW500.write('')
        self.CMW500.write('')


    def meas_condition_on(self):
        self.CMW500.write('INIT:LTE:MEAS:MEValuation ')
        while True:
            status = self.CMW500.query('FETCh:LTE:MEAS:MEValuation:STATe?')
            if status == 'RDY\n':
                print('LTE Meas is ready!')
                break

    def CMW_trig_source(self, *args):
        if args[0] == 'FrameTrigger':
            self.CMW500.write('TRIG:LTE:MEAS:MEV:SOUR "LTE Sig1: FrameTrigger"')
        elif args[0] == 'TPC Trigger':
            self.CMW500.write('TRIG:LTE:MEAS:MEV:SOUR "LTE Sig1: TPC Trigger"')
        elif args[0] == 'Fast Sync':
            self.CMW500.write('TRIG:LTE:MEAS:MEV:SOUR "Free Run (Fast Sync)"')
        elif args[0] == 'No Sync':
            self.CMW500.write('TRIG:LTE:MEAS:MEV:SOUR "Free Run (No Sync)"')
        elif args[0] == 'IF Power':
            self.CMW500.write('TRIG:LTE:MEAS:MEV:SOUR "IF Power"')

    def CMW_MEAS_rep(self, *args):
        self.CMW500.write('ROUTe:LTE:MEAS:SCENario:CSPath "LTE Sig1"')
        self.CMW500.write('CONF:LTE:MEAS:MEV:REP SING')
        self.CMW500.write('CONF:LTE:SIGN:EBL:REP SING')
        self.CMW500.write('CONF:LTE:MEAS:MEV:SCON NONE')
        self.CMW500.write('CONF:LTE:MEAS:MEV:MOD:MSCH AUTO')
        self.CMW500.write('CONF:LTE:MEAS:MEV:RBAL:AUTO ON')
        if args[0] == 'CONT':
            self.CMW500.write('CONF:LTE:MEAS:MEV:REP CONT')
            # self.CMW500.write('CONF:LTE:SIGN:CONNection:MCLuster:UL')
            # self.CMW500.write('CONF:LTE:SIGN:CONNection:RMC:UL')
            # self.CMW500.write('CONF:LTE:SIGN:CONNection:RMC:DL')
            # self.CMW500.write('ABOR:LTE:SIGN:EBL')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:RBAL:AUTO')
            # self.CMW500.write('CONF:LTE:MEAS:MEV CTYP')

            # self.CMW500.query('CONFigure:LTE:SIGN:CONNection:MCLuster:UL?')
            # self.CMW500.query('CONFigure:LTE:SIGN:CONNection:RMC:UL?')
            # self.CMW500.write('CONFigure:LTE:SIGN:CONNection:RMC:UL N25,KEEP,KEEP')
            # self.CMW500.query('CONFigure:LTE:SIGN:CONNection:RMC:DL?')
            # self.CMW500.write('CONFigure:LTE:SIGN:CONNection:RMC:DL N25,KEEP,KEEP')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:CTYP AUTO')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:MOD:MSCH QPSK')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:RES:ACLR ON')
            # self.CMW500.write('ABOR:LTE:SIGN:EBL')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:RBAL:AUTO ON')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:CTYP AUTO')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:MOD:MSCH QPSK')
            # self.CMW500.write('CONF:LTE:MEAS:MEV:RES:ACLR ON')
        elif args[0] == 'SING':
            self.CMW500.write('CONF:LTE:MEAS:MEV:REP SING')


    def CMW_TPC(self,*args):
        if(len(args) == 1 and args[0]== 'MAXP'):
            self.CMW500.write('CONFigure:LTE:SIGN:UL:PUSCh:TPC:SET MAXP')

        elif len(args) == 2 and args[0] == 'CLO':
            self.CMW500.write('CONFigure:LTE:SIGN:UL:PUSCh:TPC:SET  ', args[0])
            self.CMW500.write('CONF:LTE:SIGN:UL:PUSCh:TPC:CLTPower ', str(args[1]))

    def meas_aclr(self, mode = 'AVER'):
        time.sleep(0.1)
        self.CMW500.write('CONF:LTE:MEAS:MEV:RES:ALL ON,ON,ON,ON,ON,ON,ON,ON,ON,ON,ON,ON,ON,ON')
        self.CMW500.write('CONFigure:LTE:MEAS:MEValuation:SPEC:ACLR:ENABle ON,ON,ON')
        self.CMW500.write('CONF:LTE:MEAS:MEV:SPEC:ACLR:ENABle')
        time.sleep(0.1)
        self.CMW500.write('INIT:LTE:MEAS:MEValuation')
        time.sleep(0.1)
        self.CMW500.write('INIT:LTE:MEAS:MEValuation')
        time.sleep(0.1)
        status = self.CMW500.query('FETCh:LTE:MEAS:MEValuation:STATe?')
        if status == 'RDY\n':
            pass
        self.CMW500.write('INIT:LTE:MEAS:MEValuation')
        status = self.CMW500.query('FETCh:LTE:MEAS:MEValuation:STATe?')
        if status == 'RDY\n':
            pass
        if mode == 'AVER':
            aclr_meas = self.CMW500.query('FETCh:LTE:MEAS:MEValuation:ACLR:AVER?')
        elif mode == 'CURR':
            aclr_meas = self.CMW500.query('FETCh:LTE:MEAS:MEValuation:ACLR:CURR?')

        # if ACLR test data can't get, will retest 50 times
        n = 0
        while aclr_meas.split(',')[1] == 'INV' and n < 30:
            if n>20:
                input('请重新连接。。。。。。。。')
            self.CMW_MEAS_rep('CONT')
            self.CMW500.write('INITiate:LTE:MEAS:MEValuation')
            aclr_meas = self.CMW500.query('FETCh:LTE:MEAS:MEValuation:ACLR:CURR?')
            time.sleep(1)
            n = n + 1
            print('ACLR retest the %dth time!' % n)

        if n>=30:
            print('ACLR test fail, please double check!')
            return 0
        else:
            return aclr_meas

    def meas_evm(self):
        time.sleep(1)


if __name__ == '__main__':
    inst_addr = "192.168.105.17"
    cmw = INST_CMW500(inst_addr)

    cmw.mode_preset()



