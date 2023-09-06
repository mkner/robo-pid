#! /usr/bin/env python

from setuptools import Command, Extension, setup, find_packages
from setuptools.command.build_ext import build_ext


DISTNAME = "basic-pid"
#DESCRIPTION = "pid "

#mk  works
import basicpid


if __name__ == "__main__":
    setup()
