from .employee import Employee


class Manager(Employee):

    def do_work(self):
        self.log.info("I am a manager I care only about reporting")
        if self.is_employed:
            self.company.assign_reports(self)
