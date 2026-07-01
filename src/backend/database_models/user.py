from .base import Base

from uuid import uuid4, UUID
from datetime import datetime

from sqlalchemy import Mapped, func
from sqlalchemy.orm import mapped_column, relationship
from 


class Students(Base):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now)

    tasks: Mapped[list["Tasks"]] = relationship(back_populates="student")


class StudentsCourses(Base):
    __tablename__ = "students_courses"

    student_id: Mapped[UUID] = relationship()
    course_id: Mapped[UUID] = relationship()