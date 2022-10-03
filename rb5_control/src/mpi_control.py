from megapi import MegaPi


# MFR = 2     # port for motor front right
# MBL = 3     # port for motor back left
# MBR = 10    # port for motor back right
# MFL = 11    # port for motor front left

# ROBOT FRONT => IR SENSOR
#MFR = 11
#MFL = 2
#MBR = 3
#MBL = 10

# ROBOT FRONT => BUMPER
MFR = 10
MBL = 3
MFL = 11
MBR = 2

RATIO_FL = 1
RATIO_FR = 1
RATIO_BL = 1
RATIO_BR = 1


class MegaPiController:
    def __init__(self, port='/dev/ttyUSB0', verbose=True):
        self.port = port
        self.verbose = verbose
        if verbose:
            self.printConfiguration()
        self.bot = MegaPi()
        self.bot.start(port=port)
        self.mfr = MFR  # port for motor front right
        self.mbl = MBL  # port for motor back left
        self.mbr = MBR  # port for motor back right
        self.mfl = MFL  # port for motor front left

    def printConfiguration(self):
        print('MegaPiController:')
        print("Communication Port:" + repr(self.port))
        print("Motor ports: MFR: " + repr(MFR) +
              " MBL: " + repr(MBL) +
              " MBR: " + repr(MBR) +
              " MFL: " + repr(MFL))

    def setFourMotors(self, vfl=0, vfr=0, vbl=0, vbr=0):
        if self.verbose:
            print("Set Motors: vfl: " + repr(int(round(vfl, 0))) +
                  " vfr: " + repr(int(round(vfr, 0))) +
                  " vbl: " + repr(int(round(vbl, 0))) +
                  " vbr: " + repr(int(round(vbr, 0))))
        self.bot.motorRun(self.mfl, vfl * RATIO_FL)
        self.bot.motorRun(self.mfr, vfr * RATIO_FR)
        self.bot.motorRun(self.mbl, vbl * RATIO_BL)
        self.bot.motorRun(self.mbr, vbr * RATIO_BR)

    def carStop(self):
        if self.verbose:
            print("CAR STOP:")
        self.setFourMotors()

    def testAll(self):
        if self.verbose:
            print("TEST 4 WHEELS:")
        print("Front Left")
        speed = 50
        self.bot.motorRun(self.mfl, speed)
        time.sleep(5)
        print("Front Right")
        self.bot.motorRun(self.mfr, speed)
        time.sleep(5)
        print("Back Left")
        self.bot.motorRun(self.mbl, speed)
        time.sleep(5)
        print("Back Right")
        self.bot.motorRun(self.mbr, speed)

    def carStraight(self, speed):
        if self.verbose:
            print("CAR STRAIGHT:")
        self.setFourMotors(-speed, speed, -speed, speed)

    def carRotate(self, speed):
        if self.verbose:
            print("CAR ROTATE:")
        self.setFourMotors(-speed, -speed, -speed, -speed)

    def carSlide(self, speed):
        if self.verbose:
            print("CAR SLIDE:")
        self.setFourMotors(-speed, -speed, speed, speed)

    def carMixed(self, v_straight, v_rotate, v_slide):
        if self.verbose:
            print("CAR MIXED")
        self.setFourMotors(
            v_rotate-v_straight+v_slide,
            v_rotate+v_straight+v_slide,
            v_rotate-v_straight-v_slide,
            v_rotate+v_straight-v_slide
        )

    def close(self):
        self.bot.close()
        self.bot.exit()


if __name__ == "__main__":
    import time
    mpi_ctrl = MegaPiController(port='/dev/ttyUSB0', verbose=True)
    time.sleep(1)
    # mpi_ctrl.testAll()
    # time.sleep(2)
    # mpi_ctrl.carStraight(50)
    # time.sleep(2)
#    mpi_ctrl.carSlide(50)
#    time.sleep(2)
    mpi_ctrl.carRotate(80)
    time.sleep(5)
    mpi_ctrl.carStop()
    # print("If your program cannot be closed properly, check updated instructions in google doc.")
