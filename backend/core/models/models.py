from .base import Base
from sqlalchemy.types import BigInteger
from typing import List
from datetime import date, datetime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import (
    Table,
    ForeignKey,
    Column,
    String,
    Text
)
import enum


class Status(enum.Enum):
    DONE = 'Done'
    IN_REVIEW = 'In review'
    IN_PROCESS = 'In process'
    PENDING = 'Pending'


class Priority(enum.Enum):
    HIGH = 'High'
    NORMAL = 'Normal'
    LOW = 'Low'


task_tag = Table(
    'task_tag_association',
    Base.metadata,
    Column('task_id', ForeignKey('tasks.id'), primary_key=True, nullable=False),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True, nullable=False),
)

team_user = Table(
    'team_user_association',
    Base.metadata,
    Column('team_id', ForeignKey('teams.id'), primary_key=True, nullable=False),
    Column('user_id', ForeignKey('users.id'), primary_key=True, nullable=False),
)


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    created_at: Mapped[date] = mapped_column(nullable=False, default=date.today)

    organizations: Mapped[List['Organization']] = relationship(back_populates='owner')

    tasks: Mapped[List['Task']] = relationship(back_populates='worker')

    teams: Mapped[List['Team']] = relationship(secondary=team_user, back_populates='workers')


class Organization(Base):
    __tablename__ = 'organizations'

    name: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    created_at: Mapped[date] = mapped_column(nullable=False, default=date.today)

    teams: Mapped[List['Team']] = relationship(back_populates='organization')

    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    owner: Mapped['User'] = relationship(back_populates='organizations')


class Team(Base):
    __tablename__ = 'teams'

    name: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[date] = mapped_column(nullable=False, default=date.today)

    organization_id: Mapped[int] = mapped_column(ForeignKey('organizations.id'))
    organization: Mapped['Organization'] = relationship(back_populates='teams')

    boards: Mapped[List['Board']] = relationship(back_populates='team')

    workers: Mapped[List['User']] = relationship(secondary=team_user, back_populates='teams')


class Board(Base):
    __tablename__ = 'boards'

    name: Mapped[str] = mapped_column(String(60), nullable=False)

    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    team: Mapped['Team'] = relationship(back_populates='boards')

    tasks: Mapped[List['Task']] = relationship(back_populates='board')


class Task(Base):
    __tablename__ = 'tasks'

    name: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[Status]
    priority: Mapped[Priority]
    deadline: Mapped[datetime]
    created_at: Mapped[date] = mapped_column(nullable=False, default=date.today)

    board_id: Mapped[int] = mapped_column(ForeignKey('boards.id'))
    board: Mapped['Board'] = relationship(back_populates='tasks')

    worker_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    worker: Mapped['User'] = relationship(back_populates='tasks')

    tags: Mapped[List['Tag']] = relationship(secondary=task_tag, back_populates='tasks')


class Tag(Base):
    name: Mapped[str] = mapped_column(String(60), nullable=False)

    tasks: Mapped[List['Task']] = relationship(secondary=task_tag, back_populates='tags')
