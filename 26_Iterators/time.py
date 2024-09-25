class Time:
    def __init__(self, seconds):
        self.s = seconds

    def convert_to_minutes(self):
        m, s = divmod(self.s, 60)
        return f"{m}:{s}"

    def convert_to_hours(self):
        m, s = divmod(self.s, 60)
        h, m = divmod(m, 60)
        return f"{h}:{m}:{s}"


time = Time(2131230)
print(time.convert_to_minutes())
print(time.convert_to_hours())