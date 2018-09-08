#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from subprocess import Popen
from subprocess import PIPE

class ProjectCommander:

    COMMAND_WHAT_VERSION = 'agvtool what-marketing-version -terse'
    COMMAND_UPDATE_VERSION = 'agvtool new-marketing-version %s'
    COMMAND_WHAT_BUILD_NUMBER = 'agvtool what-version -terse'
    COMMAND_UPDATE_BUILD_NUMBER = 'agvtool next-version --all'

    def execute(self, command, cwd, shell=True):
        return Popen([command], cwd=cwd, shell=shell, stdin=PIPE, stdout=PIPE, stderr=PIPE)
