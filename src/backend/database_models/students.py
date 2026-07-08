from .base import Base

from uuid import uuid4, UUID
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Mapped, func, ForeignKey, Table, Column
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy

if TYPE_CHECKING:
    from .tasks import Tasks, Courses


class Quality(Enum):
    bad="bad"
    middle="middle"
    good="good"


class StudentsCourses(Base):
    __tablename__ = "students_courses"

    student_id: Mapped[UUID] = mapped_column(ForeignKey("students.id"), primary_key=True)
    course_id: Mapped[UUID] = mapped_column(ForeignKey("courses.id"), primary_key=True)
    enrolled_at: Mapped[datetime] = mapped_column(server_default=func.now())

    student: Mapped["Students"] = relationship(back_populates="enrollments")
    course: Mapped["Courses"] = relationship(back_populates="enrollments")


class Students(Base):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    tasks: Mapped[list["Tasks"]] = relationship(back_populates="student")
    topics_mastery: Mapped[list["TopicMastery"]] = relationship(back_populates="student")
    enrollments: Mapped[list["StudentsCourses"]] = relationship(back_populates="student")

    courses = association_proxy("enrollments", "course")


class TopicMastery(Base):
    __tablename__ = "topic_mastery"

    topic_id: Mapped[UUID] = mapped_column(ForeignKey("Topics.id"))
    quality: Mapped[Quality] = mapped_column()
    description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now)

