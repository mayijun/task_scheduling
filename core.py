import abc
from ortools.sat.python import cp_model


class BaseSlotSerializer:
    # the base of task assignment is converting it to slot-based / time-grain based assignment
    # every slot is present by its' start time and pre-defined durations
    Unit = 30  # every slot present to 30 minutes time grains

    def __init__(self, start_time):
        pass

    @classmethod
    def check_start_time(cls, start_time):
        pass


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

    def slots(self):
        pass

    def handover(self):
        pass

    '''flag which mean this task can skip some hard constraint,
    user should only use this flag in emergency unscheduled task'''

    def forced_assigned(self):
        pass

    '''soft constraint, try to assign task to target worker if possible'''

    def soft_desired_workers(self):
        pass

    '''prevent task to be assigned to another worker'''

    def fixed(self):
        pass

    '''quantized task's difficulty which prevent workers from doing  multiple tasks in parallel,
    related to workers width'''

    def width(self):
        pass


class BaseAssignment:
    pass


class BaseSkill:
    def __init__(self):
        pass


class BaseWorker:
    def __init__(self, skill_set):
        pass

    def id(self):
        pass

    def width(self):  # quantized ability to do multiple task in parallel
        pass


# define
class BaseAvailability:
    def __init__(self, worker_id, slot_set):
        pass


class BaseSchedulingSolutionRecorder(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def solution_count(self):
        return self.__solution_count


def solve_task_scheduling( allow_unassigned = True ):
    model = cp_model.CpModel()
