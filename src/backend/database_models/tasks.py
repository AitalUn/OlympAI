from .base import Base
from .user import Students

from datetime import datetime, timedelta
from uuid import UUID, uuid4
import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, Enum, ForeignKey

class TaskStatus(enum.Enum):
    waiting = "waiting"
    in_progress = "in_progress"
    is_done = "is_done"


class TaskDifficulty(enum.Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[UUID] = mapped_column(default=uuid4)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now)


class Topics(Base): 
    __tablename__ = "topics"

    course_id: Mapped[UUID] = mapped_column(ForeignKey("courses.id"))

    name: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now)

    problems: Mapped[list["Problems"]] = relationship(back_populates="topic")


class Problems(Base):
    __tablename__ = "problems"

    topic_id: Mapped[UUID] = mapped_column(ForeignKey("topics.id"))

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    solution: Mapped[str] = mapped_column()
    answer: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now)

    topic: Mapped["Topics"] = relationship(back_populates="problems")

class Tasks(Base):
    __tablename__ = "tasks"
    problem_id: Mapped[UUID] = mapped_column(ForeignKey("problems.id"))
    student_id: Mapped[UUID] = mapped_column(ForeignKey("students.id"))

    description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now)
    deadline: Mapped[datetime] = mapped_column(default =datetime.now() + timedelta(hours=48))
    task_status: Mapped[TaskStatus] = mapped_column(default = TaskStatus.waiting)

    problem: Mapped["Problem"] = 
    student: Mapped["Students"] = relationship(back_populates="tasks")



    