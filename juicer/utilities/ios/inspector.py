#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from utilities.ios.commander import ProjectCommander

class ProjectInspector:
    """
    Class which provides information about project functionalities.
    """

    def __init__(self, path):
        self.__commander = ProjectCommander()
        self.__project_path = path


    def is_versioning_enabled(self):
        """
        Checks if versioning is enabled for current project.

        Returns:
            bool -- returns True if versioning is enabled for current project.
        """
        process = self.__commander.execute(ProjectCommander.COMMAND_WHAT_VERSION, self.__project_path)
        (_, _) = process.communicate()
        return process.returncode == 0


    def get_version(self):
        """
        Returns application version for all targets.

        Returns:
            {str: str} -- returns dictionary which contains all targets with their versions.
        """
        return 1


    def get_build_number(self):
        """
        Return build number for all targets or configuration.

        Returns:
        """

        return 1

