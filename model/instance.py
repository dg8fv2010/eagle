#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import Base

from sqlalchemy import Column, Integer, String, DateTime

class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    image_name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)
    is_deleted = Column(Integer, nullable=False)


class Instance(Base):
    __tablename__ = 'instance'
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    container_name = Column(String(128), nullable=False)
    container_serial = Column(String(128), nullable=False)
    host = Column(String(128), nullable=False)
    port = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    jump_server = Column(String(128), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)
    is_deleted = Column(Integer, nullable=False)

    def __init__(self, image_id, user_id, container_name, container_serial, host, port, status, jump_server, **kargs):
        self.image_id = image_id
        self.user_id = user_id
        self.container_name = container_name
        self.container_serial = container_serial
        self.host = host
        self.port = port
        self.status = status
        self.jump_server = jump_server
        self.create_time = kargs.get('create_time', '0000-00-00 00:00')
        self.update_time = kargs.get('update_time', '0000-00-00 00:00')
        self.is_deleted = kargs.get('is_deleted', 0)
