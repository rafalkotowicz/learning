from datetime import datetime

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
                           echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def print_all_tasks(self):
        rows = self.session.query(Task).all()
        print("Today:")
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print(f"{row.id}. {str(row)}")

    def print_todays_tasks(self):
        rows = self.session.query(Task).filter(Task.deadline ==
                                               datetime.today().date()).all()
        print(f"Today {datetime.today().strftime('%d %B')}:")
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print(f"{row.id}. {str(row)}")

    def add_task(self, task_text="NO_TITLE", deadline=datetime.now()):
        self.session.add(Task(task_text, deadline=deadline))
        self.session.commit()


def gui(dbHandler: DbHandler):
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Add task")
        print("0) Exit")
        user_input = int(input())
        if 1 == user_input:
            dbHandler.print_todays_tasks()
        elif 2 == user_input:
            pass
        elif 3 == user_input:
            dbHandler.print_all_tasks()
        elif 4 == user_input:
            print("Enter task")
            task = input()
            print("Enter deadline")
            deadline = datetime.fromisoformat(input())
            dbHandler.add_task(task, deadline)

        elif 0 == user_input:
            print("Bye!")
            exit(0)
        else:
            print("Invalid option chosen")


dbHandler = DbHandler()
# dbHandler.print_all_tasks()
gui(dbHandler)
