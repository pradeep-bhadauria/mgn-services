#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
PREFERRED_URL_SCHEME = 'http'

SECRET_KEY = 'this-really-needs-to-be-changed'

SQLALCHEMY_DATABASE_URI = 'postgres://jcepytxffjskun:heHyQX9CwinC9EpJCZIceXAGR4@ec2-54-163-239-63.compute-1.amazonaws.com:5432/d241q24dttbkg1'
SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}


""" Openshift Config """
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = os.environ.get('SECRET_KEY','\xfb\x13\xdf\xa1@i\xd6>V\xc0\xbf\x8fp\x16#Z\x0b\x81\xeb\x16')
HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS','localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME','mgn')
IP = os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))