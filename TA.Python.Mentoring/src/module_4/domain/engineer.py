from .employee import Employee


def repeate(work_hours, burnout_hours):
    from .log_configurator import get_logger
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(work_hours):
                return_value = func(*args, **kwargs)
                if i >= burnout_hours:
                    get_logger("engineer").info(f"I have been working for {burnout_hours} hours. Burnout is coming. Stop working")
                    break
            return return_value

        return wrapper

    return actual_decorator


class Engineer(Employee):

    @repeate(12, 8)
    def do_work(self):
        self.log.info("I am working on task")
        if self.is_employed:
            self.company.assign_task(self)
