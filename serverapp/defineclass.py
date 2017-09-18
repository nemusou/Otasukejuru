import random
import datetime as dt


class Task:
    def __init__(self, task_name: str, registration_date: dt.datetime,
                 due_date: dt.datetime, priority: int,
                 run_time: int):
        self.registration_date: dt.datetime = registration_date  # 登録日
        self.due_date: dt.datetime = due_date  # 期限
        self.task_name: str = task_name
        self.priority: int = priority
        self.run_time: int = run_time  # 作業時間(単位(時間))
        self.progress: float = 0.

    def __lt__(self, other):
        if self.priority == other.priority:
            if self.progress == other.progress:
                return self.due_date < other.due_date
            else:
                return self.progress < other.progress
        else:
            return self.priority > other.priority

    def update_priority(self, new_priority: int) -> None:
        # 優先度が決まるのって期限までの日数でだっけ
        self.priority = new_priority

    def update_progress(self, new_progress: int) -> None:
        self.progress = new_progress


class Schedule:
    def __init__(self, schedule_name: int, date: dt.datetime):
        self.schedule_name: str = schedule_name
        self.date = date


if __name__ == '__main__':
    l = [Task(str(i), dt.datetime.now(), dt.datetime.now(), i % 2, i * 10) for i
         in range(10)]
    random.shuffle(l)
    s = sorted(l)
    for i in s:
        print(
            "x: {}, due_date: {}, priority: {}".format(i.task_name, i.due_date,
                                                       i.priority))