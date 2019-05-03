# class named as BaseXXXX is solver related
class BaseTask:
    # Base Class for all tasks. scheduling impacted information should defined here as all tasks use the same solver

    def __init__(self, required_skills):
        self.__required_skills = required_skills

    def id(self):
        pass

    def required_skill(self):
        return self.__required_skills

    def possible_appointments_start(self):
        pass

    def durations(self):
        pass

    '''flag which mean this task can skip some hard constraint,
    user should only use this flag in emergency unscheduled task'''

    def forced_assigned(self):
        pass

    '''soft constraint, try to assign task to target worker if possible'''
    def desired_workers(self):
        pass

    '''prevent task to be assigned to another workers'''

    def fixed(self):
        pass

    '''quantized task's difficulty which prevent workers from doing  multiple tasks in parallel,
    related to workers width'''

    def width(self):
        pass


class BaseAssignment:
    pass


class TaskTemplate:
    pass


class BaseSkill:
    def __init__(self):
        pass


class Language(BaseSkill):
    pass


class BaseWorker:
    def __init__(self, skill_set):
        pass

    def width(self):  # quantized ability to do multiple task in parallel
        pass


class BaseShift:
    pass


class BaseSchedulingSolution:
    def __init__(self):
        pass
