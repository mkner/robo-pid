#! /usr/bin/env python

from setuptools import Command, Extension, setup, find_packages
from setuptools.command.build_ext import build_ext


DISTNAME = "robo-pid"
#DESCRIPTION = "pid "

#mk  works
import robopid


if __name__ == "__main__":
    setup()
