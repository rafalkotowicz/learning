from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __init__(self, task, deadline=datetime.today()):
        self.task = task
        self.deadline = deadline

    def __repr__(self):
        return f"Task({self.id}, {self.task}, {self.deadline})"

    def __str__(self):
        return self.task


class DbHandler:
    engine = create_engine('sqlite:///todo.db?check_same_thread=False',
                           echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session: Session = Session()

    def print_all_tasks(self):
        rows = self.session.query(Task).order_by(Task.deadline).all()
        print_rows(rows, True)
        return rows

    def print_todays_tasks(self):
        rows: list = self.session.query(Task).filter(Task.deadline ==
                                                     datetime.today().date()).all()
        print(f"Today {datetime.today().strftime('%d %B')}:")
        print_rows(rows)

    def print_week(self):
        for day_offset in range(7):
            day = datetime.today() + timedelta(days=day_offset)
            rows: list = self.session.query(Task).filter(Task.deadline ==
                                                         day.date()).all()
            print(f"{get_name_of_weekday(day)} {day.strftime('%d %B')}")
            print_rows(rows)
            print()

    def print_missed_tasks(self):
        rows: list = self.session.query(Task).filter(Task.deadline <
                                                     datetime.today().date()).all()
        print("Missed tasks:")
        if (len(rows) == 0):
            print("Nothing is missed!")
        else:
            print_rows(rows, True)
        print()

    def add_task(self, task_text="NO_TITLE", deadline=datetime.now()):
        self.session.add(Task(task_text, deadline=deadline))
        self.session.commit()

    def delete_task(self, task):
        self.session.delete(task)
        self.session.commit()
        print("The task has been deleted!")


def print_rows(rows: list, with_deadline=False):
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        i = 1
        for row in rows:
            if with_deadline:
                print(
                    f"{i}. {str(row.task)}. {row.deadline.strftime('%d %B')}")
            else:
                print(f"{i}. {str(row.task)}")
            i += 1


def get_name_of_weekday(date: datetime):
    day = date.isoweekday()
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"


def gui(dbHandler: DbHandler):
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
        user_input = int(input())
        if 1 == user_input:
            dbHandler.print_todays_tasks()
        elif 2 == user_input:
            dbHandler.print_week()
        elif 3 == user_input:
            dbHandler.print_all_tasks()
        elif 4 == user_input:
            dbHandler.print_missed_tasks()
        elif 5 == user_input:
            print("Enter task")
            task = input()
            print("Enter deadline")
            deadline = datetime.fromisoformat(input())
            dbHandler.add_task(task, deadline)
        elif 6 == user_input:
            print("Choose the number of the task you want to delete:")
            rows = dbHandler.print_all_tasks()
            id = int(input())
            dbHandler.delete_task(rows[id - 1])
        elif 0 == user_input:
            print("Bye!")
            exit(0)
        else:
            print("Invalid option chosen")


dbHandler = DbHandler()
gui(dbHandler)
