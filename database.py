from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(
        String(64),
        unique=True,
        nullable=False
    )

    password = Column(
        String(64),
        unique=True,
        nullable=False
    )

    currency_type = Column(
        String(64),
        ForeignKey("currency.id"),
        nullable=False,
        default='Hryvnia'
       )

    record = db.relationship(
        "RecordModel",
        back_populates="user",
        lazy="dynamic"
    )

    currency = db.relationship(
        "CurrencyModel",
        back_populates="user"
    )


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(
        String(64),
        unique=True,
        nullable=False
    )

    record = db.relationship(
        "RecordModel",
        back_populates="category",
        lazy="dynamic"
    )


class RecordModel(db.Model):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        unique=False,
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("category.id"),
        unique=False,
        nullable=False
    )

    currency_type = Column(
        String,
        ForeignKey("currency.name"),
        nullable=False
    )

    date = Column(TIMESTAMP, server_default=func.now())
    amount = Column(String, unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")
    currency = db.relationship("CurrencyModel", back_populates="record")


class CurrencyModel(db.Model):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    user = db.relationship("UserModel", back_populates="currency")
    record = db.relationship("RecordModel", back_populates="currency", lazy="dynamic")