import time
import threading


# PyAGC
# Victor Mout, 2021
# GNU License
#
# C U R R E N T  I N S T R U C T I O N S #
# AD
# ADS
# CA
# TS
# bCH
# AUG


# TODO: Add TIME4/5/6 counter offset once fetch cycle is implemented

currentOpcode = "26000"
currentArgument = "233"
# Define Memory and ROM
class Memory:
    UNSWITCHED_WRITABLE_Memory = [0] * 767
    EB1 = [0] * 256
    EB2 = [0] * 256
    EB3 = [0] * 256
    EB4 = [0] * 256
    EB5 = [0] * 256
    EB6 = [0] * 256
    EB7 = [0] * 256

    FB1 = [0] * 1024
    FB2 = [0] * 1024

    UNSWITCHED_UNWRITABLE_Memory = [0] * 2048
    ACTIVE_UNWRITABLE_BANK = EB1
    ACTIVEBANK = EB1
    Memory = UNSWITCHED_WRITABLE_Memory + ACTIVEBANK + ACTIVE_UNWRITABLE_BANK + UNSWITCHED_UNWRITABLE_Memory
    IO_SPACE = [0] * 511


# AGC object
class AGC(object):
    globals()

    def __init__(self):
        self.A = 0b00
        self.L = 0b00
        self.Q = 0b00
        self.EB = 0b000
        self.FB = 0b00000
        self.Z = 0b00
        self.BB = 0b00
        self.zero = 0b00
        self.ARUPT = 0b00
        self.LRUPT = 0b00
        self.QRUPT = 0b00
        self.ZRUPT = 0b00
        self.BBRUPT = 0b00
        self.BRUPT = 0b00
        self.CYR = 0b00
        self.SR = 0b00
        self.CYL = 0b00
        self.EDOP = 0b00
        self.TIME2 = 0b00
        self.TIME1 = 0b00
        self.TIME3 = 0b00
        self.TIME4 = 0b00
        self.TIME5 = 0b00
        self.TIME6 = 0b00
        self.SAMPTIME1 = self.TIME1
        self.SAMPTIME2 = self.TIME2
        self.CDUX = 0b00
        self.CDUY = 0b00
        self.CDUZ = 0b00
        self.OPTY = 0b00
        self.OPTX = 0b00
        self.PIPAX = 0b00
        self.PIPAY = 0b00
        self.PIPAZ = 0b00
        self.INLINK = 0b00
        self.RNRAD = 0b00
        self.GYROCTR = 0b00
        self.CDUbCMD = 0b00
        self.CDUYCMD = 0b00
        self.CDUZCMD = 0b00
        self.OPTYCMD = 0b00
        self.OPTXCMD = 0b00
        self.OUTLINK = 0b00

        # Interrupt flags
        self.INTERRUPTFL = False
        self.T3RUPT = False
        self.T4RUPT = False

        # Arbitrary logic flags
        self.t4logicflag = True

        # EXTRACODE flag
        self.EXTRACODE = False
    # cycle length =  0.00000000048828125

        self.opcodes = {
            "AD" : "60000",

            "ADS" : "26000",

            "AUG": "24000",

            "BZF": "10000",

            "BZF": "10000",

            "BZMF": "60000",

            "CA": "30000",

            "CAE": "30000",

            "CAF": "30000",

            "CCS": "10000",

            "COM": "40000",

            "CS": "40000",

            "DAS": "20001",

            "DCA": "30001",

            "DCOM": "40001",

            "DCS": "40001",

            "DDOUBL": "20001",

            "DIM": "26000",

            "DOUBLE": "60000",

            "DTCB": "52006",

            "DTCF": "52005",

            "DV": "10000",

            "DXCH": "52001",

            "EDRUPT": "07000",

            "EXTEND": "00006",

            "INCR": "24000",

            "INDEX": "50000",

            "INHINT": "00004",

            "LXCH": "22000",

            "MASK": "70000",

            "MP": "70000",

            "MSU": "20000",

            "NOOP": "30000",

            "NOOP": "10000",

            "OVSK": "54000",

            "QXCH": "22000",

            "RAND": "02000",

            "READ": "00000",

            "RELINT": "00003",

            "RESUME": "50017",

            "RETURN": "00002",

            "ROR": "04000",

            "RXOR": "06000",

            "SQUARE": "70000",

            "SU": "60000",

            "TC": "00000",

            "TCAA": "54002",

            "TCF": "10000",

            "TS": "54000",

            "WAND": "03000",

            "WOR": "05000",

            "WRITE": "01000",

            "XCH": "56000",

            "XLQ": "00001",

            "XXALQ": "00000",

            "ZL": "22007",

            "ZQ": "22007"

        }




    def registerHandler(self):
        Memory.ACTIVEBANK = ("Memory.EB" + str(AGC.EB))
        Memory.ACTIVE_UNWRITABLE_BANK = ("Memory.FB" + str(AGC.FB))

        self.BB = ((self.FB << 10) + self.EB)

        tmp = AGC.CYR & 0b111111111111111
        self.CYR = AGC.CYR >> 1
        tmp = tmp << 14
        tmp = tmp & 0b100000000000000
        self.CYR = tmp + AGC.CYR

        tmp = AGC.CYL & 0b111111111111111
        self.CYL = AGC.CYL << 1
        tmp = tmp >> 14
        tmp = tmp & 0b000000000000001
        self.CYL = tmp + AGC.CYL

        self.SR = self.SR >> 1

        self.EDOP = self.EDOP >> 7



    def fetch(self):
        if (currentOpcode == self.opcodes["AD"] and self.EXTRACODE == False):
                self.A = self.A + Memory.Memory[int(currentArgument)]

        if (currentOpcode == self.opcodes["ADS"] and self.EXTRACODE == False):
                Memory.Memory[int(currentArgument)] = Memory.Memory[int(currentArgument)] + self.A




    def interruptHandler(self):
        pass


AGC = AGC()


# Main function
def main():
    AGC.A = 123
    AGC.fetch()
    print(Memory.Memory[223])


# name/main run check
if __name__ == '__main__':
    main()

