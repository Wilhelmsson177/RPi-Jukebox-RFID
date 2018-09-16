import subprocess
import os

import nxppy
import time

mifare = nxppy.Mifare()

# get absolute path of this script
dir_path = os.path.dirname(os.path.realpath(__file__))

while True:
        # reading the card id
        try:
            uid = mifare.select()
            print uid
            subprocess.call(["{}/rfid_trigger_play.sh --cardid={}".format(dir_path, uid)], shell=True)
        except nxppy.SelectError:
            # SelectError is raised if no card is in the field.
            pass
        except OSError as e:
            print "Execution failed: {}".format(e)
        time.sleep(0.5)
