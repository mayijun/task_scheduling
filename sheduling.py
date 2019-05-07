from core import BaseSlot, BaseSkill
import datetime


class Slot(BaseSlot):
    __unit = datetime.timedelta(minutes=30)  # every slot is 30 minutes

    def is_slot_serializable(self, start_time):
        if isinstance(start_time, datetime.datetime):
            if (start_time.minute == 30 or start_time.minute == 0) and start_time.second == 0:
                return True
            else:
                return False
        else:
            return False


class TaskTemplate:
    pass


class ProductSkill(BaseSkill):
    pass


class Language(BaseSkill):
    pass
