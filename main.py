import time

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

# TODO: Add line by line file reader
# TODO: Finish all instructions
# TODO: Add function logic
# TODO: Add I/O logic
# TODO: Add DSKY output
# TODO: Finish registers
# TODO: Add nessecary ROM data



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
        INTERRUPTFL = False

    #cycle length =  0.00000000048828125

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




    def timerLoop(self):

            time.sleep(0.010)
            self.TIME1 = self.TIME1 + 1
            if self.TIME1 == 0b11111111111111:
                self.TIME1 = 0b000000000000000
                self.TIME2 = self.TIME2 + 1

    def interruptHandler(self):
        pass
    def processInstruction(self, instruction: str):
        splitInstruction = instruction.split()

AGC = AGC()

# Main function
def main():
    while True:
        AGC.timerLoop()
# name/main run check
if __name__ == '__main__':
    main()
