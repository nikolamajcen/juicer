#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from subprocess import Popen
from subprocess import PIPE

class Commander:
    """
    Class which defines generic command manager.
    """

    def __init__(self, project_dir: str):
        """
        Initializes commander object.

        Arguments:
            project_dir {str} -- Path to the project root directory.
        """
        self.__project_dir = project_dir


    def execute(self, command: str, cwd: str=None, shell: bool=True) -> Popen:
        """
        Executes provided command as a subprocess.

        Arguments:
            command {str} -- [description]

        Keyword Arguments:
            cwd {str} -- Defines in which directory is executed provided command.
                           As default is used project directory. (default: {None})
            shell {bool} -- Defines if command is executed via shell. (default: {True})

        Returns:
            Popen -- Returns started process
        """
        if cwd is None:
            cwd = self.__project_dir
        return Popen([command], cwd=cwd, shell=shell, stdin=PIPE, stdout=PIPE, stderr=PIPE)
