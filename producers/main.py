import time
import random
import background
import producer_classes
from settings import *

# Use 5 background threads.
background.n = 5


@background.task
def work(class_obj):
    """
        Multi-thread work method.
        Class passed as parameter.
        Instance created dynamically
    """
    msg_inst = class_obj()
    msg_inst.publish_message()


if __name__ == '__main__':

    while True:
        idx = random.randint(0, 3)
        class_ = getattr(producer_classes, PUBLISHER_CLASSES[idx])
        work(class_)
        time.sleep(1)
