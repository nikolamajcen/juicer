#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from utilities.ios.commander import ProjectCommander

class ProjectInspector:
    """
    Class which provides information about project functionalities.
    """

    def __init__(self, project_dir: str):
        """
        Initializes project inspector.

        Arguments:
            project_dir {str} -- Defines root directory of the project.
        """
        self.__commander = ProjectCommander(project_dir)


    def is_versioning_enabled(self):
        """
        Checks if versioning is enabled for current project.

        Returns:
            bool -- returns True if versioning is enabled for current project.
        """
        process = self.__commander.execute(ProjectCommander.COMMAND_WHAT_VERSION)
        (_, _) = process.communicate()
        return process.returncode == 0


    def get_version(self) -> (bool, str):
        """
        Returns current application version.

        Returns:
            (bool, str) -- returns tuple which contains flag for success and script output (version).
        """
        process = self.__commander.execute(ProjectCommander.COMMAND_WHAT_VERSION)
        (output, _) = process.communicate()
        return (process.returncode == 0, self.__formatted_output(output))


    def get_build_number(self) -> (bool, int):
        """
        Returns current application build number.

        Returns:
            (bool, int) -- Returns tuple which contains flag for success and script output
        """
        process = self.__commander.execute(ProjectCommander.COMMAND_WHAT_BUILD_NUMBER)
        (output, _) = process.communicate()
        return (process.returncode == 0, int(self.__formatted_output(output)))


    def __formatted_output(self, output: bytes) -> str:
        """
        Formats bytes to string.

        Arguments:
            output {bytes} -- Bytes representation of value.

        Returns:
            str -- Formatted bytes value without whitespaces.
        """
        return output.decode('utf-8').strip()
