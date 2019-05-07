from core import BaseSlot
import datetime


class Slot(BaseSlot):

    __unit = 30*60

    def is_slot_serializable(self, start_time):
        if isinstance(start_time, datetime.datetime):
            pass
        else:
            return False
