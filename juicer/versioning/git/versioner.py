#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from utilities.commander import Commander
from versioning.git.command import GitCommand

class GitVersioner:
    """
    Class which is for interaction with git and version control.
    """

    def __init__(self, project_dir: str):
        """
        Initializes git versioner.

        Arguments:
            project_dir {str} -- Defines project root directory.
        """
        self.__commander = Commander(project_dir)


    def add_changes(self) -> (bool, str):
        """
        It collects all changes from the latest commit.

        Returns:
            {(bool, str)} -- Returns tuple with flag for success and output message.
        """
        process = self.__commander.execute(GitCommand.ADD_CHANGES)
        (output, _) = process.communicate()
        return (process.returncode == 0, output)


    def create_commit(self, message: str) -> (bool, str):
        """
        Creates a new commit with provided message.

        Returns:
            {(bool, str)} -- Returns tuple with flag for success and output message.
        """
        process = self.__commander.execute(GitCommand.CREATE_COMMIT.format(message))
        (output, _) = process.communicate()
        return (process.returncode == 0, output)


    def create_tag(self, name: str, message: str=None) -> (bool, str):
        """
        Creates a new tag for the latest commmit.

        Returns:
            {(bool, str)} -- Returns tuple with flag for success and output message.
        """
        if message is None:
            message = ""
        process = self.__commander.execute(GitCommand.CREATE_TAG_WITH_MESSAGE.format(name, message))
        (output, _) = process.communicate()
        return (process.returncode == 0, output)


    def push_changes(self) -> (bool, str):
        """
        Pushes current changes which includes both commits and tags from current branch.

        Returns:
            {(bool, str)} -- Returns tuple with flag for success and output message.
        """
        process = self.__commander.execute(GitCommand.PUSH_CHANGES)
        (output, _) = process.communicate()
        return (process.returncode == 0, output)
