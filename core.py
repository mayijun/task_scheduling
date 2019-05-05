import datetime

from ortools.sat.python import cp_model


# class named as BaseXXXX is solver related


# the base of task assignment is converting it to slot-based / time-grain based assignment
# every slot is present by its' start time and united durations

class BaseSlot:

    _Unit = 30*60           # every slot present to 30  minutes (30*60 seconds) time grains by default

    def __init__(self, start_time):
        if self.is_slot_serializable(start_time):
            self.__start_time = start_time
        else:
            raise ValueError

    def is_slot_serializable(self, start_time):
        if isinstance(start_time, datetime.datetime):
            pass
        else:
            return False


class BaseSlotSet:

    def __init__(self, slot_array):
        pass

    def __contains__(self, item):
        pass



class BaseTask:
    # Base Class for all tasks. scheduling impacted information should defined here. all tasks use the same solver

    def __init__(self, required_skills):
        self.__required_skills = required_skills

    def id(self):
        pass

    def required_skill(self):
        return self.__required_skills

    ''' for appointment based tasks , possible start_time maybe is a range 
    (example: customer provide his availability about task start time)'''

    def possible_appointments_start(self):
        pass

    '''start time of task fixed after confirmation of appointment to customer'''

    def confirmed_appointment_start(self):
        pass

    def durations(self):
        pass

    def slots(self):
        pass

    def soft_handover_times(self):
        pass

    '''flag which mean this task can skip some hard constraint,
    user should only use this flag in emergency unscheduled task'''

    def hard_forced_assigned(self):
        pass

    # this may lead to infeasible solution
    '''
    def soft_forced_assigned(self):
        pass
    '''

    '''soft constraint, try to assign task to target worker if possible'''

    def soft_desired_workers(self):
        pass

    '''prevent task to be assigned to another worker'''

    def fixed(self):
        now = datetime.datetime.now()

    '''quantized task's difficulty which prevent workers from doing  multiple tasks in parallel,
    related to workers width'''

    def width(self):
        pass


class BaseSkill:
    def __init__(self):
        pass


class BaseWorker:
    def __init__(self, skill_set):
        pass

    def id(self):
        pass

    '''quantized ability to do multiple task in parallel, sum of assigned tasks' width should <= soft_width, or a
      linear penalty on the delta will be added to the objective. '''

    def soft_width(self):
        pass

    '''quantized ability to do multiple task in parallel, sum of assigned tasks' width should <= hard_width
    '''

    def hard_width(self):
        pass


# define
class BaseAvailability:
    def __init__(self, worker_id, slot_set):
        pass

    def soft_threshold(self):
        pass

    def hard_threshold(self):
        pass


class BaseSchedulingProblemConstructor:
    def __init__(self, workers_array, tasks_array, availablilty_array):
        pass

    # worker's availability should align with task slot requirement to shrink problem search space
    def align_slot_and_serialize(self):
        pass


class BaseSchedulingSolutionRecorder(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def solution_count(self):
        return self.__solution_count


class BaseSchedulingSolutionModeler:

    def __init__(self, problem, allow_unassigned=True, unassign_penalty_coeff=100):
        self.__problem = problem
        self.__allow_unassigned = allow_unassigned
        self.__unassign_penalty_coeff = unassign_penalty_coeff
        self.model = cp_model.CpModel()
        self.modeler()
        self.solver = cp_model.CpSolver()

    def modeler(self):
        pass

    def solve(self, solve_time_limit=None):
        # Sets a time limit of solver
        if solve_time_limit:
            self.solver.parameters.max_time_in_seconds = solve_time_limit
        self.solver.Solve(self.model)
