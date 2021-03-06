#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from pbxproj import XcodeProject
from utilities.commander import Commander
from platforms.ios.command import ProjectCommand

class ProjectConfigurator:
    """
    Class which is used to configure pbxproj file.
    """

    def __init__(self, project_dir: str, pbxproj_path: str):
        """
        Initializes project configuration object.

        Arguments:
            project_dir {str} -- Defines project root directory.
            pbxproj_path {str} -- Defines path to pbxproj project file.
        """
        self.__commander = Commander(project_dir)
        self.__path = pbxproj_path


    def enable_versioning(self, build_number: int=None):
        """
        This method adds missing flags for automatic versioning.
        With automatic versioning, project will be able to use
        agvtool.

        Keyword Arguments:
            build_number {int} -- Project build number which should be used.
                                  If not provided, it will be set to 1. (default: {None})
        """
        project = XcodeProject.load(self.__path)
        if build_number is None:
            build_number = 1
        project.set_flags('CURRENT_PROJECT_VERSION', str(build_number))
        project.set_flags('VERSIONING_SYSTEM', 'apple-generic')
        project.save()


    def disable_versioning(self):
        """
        Deletes flags for automatic versioning.
        """
        project = XcodeProject.load(self.__path)
        project.remove_flags('CURRENT_PROJECT_VERSION', None)
        project.remove_flags('VERSIONING_SYSTEM', None)
        project.save()


    def update_version(self, version: str) -> (bool, str):
        """
        Updates current application version to provided one.

        Arguments:
            version {str} -- Defines new version.

        Returns:
            {(bool, str)} -- Returns bool flag for success and output from process.
        """
        process = self.__commander.execute(ProjectCommand.UPDATE_VERSION.format(version))
        (output, _) = process.communicate()
        return (process.returncode == 0, self.__formatted_output(output))


    def update_build_number(self) -> (bool, str):
        """
        Updates current build number of the application.

        Returns:
            {(bool, str)} -- Returns bool flag for success and output from process.
        """
        process = self.__commander.execute(ProjectCommand.UPDATE_BUILD_NUMBER)
        (output, _) = process.communicate()
        return (process.returncode == 0, self.__formatted_output(output))


    def __formatted_output(self, output: bytes) -> str:
        """
        Formats bytes to string.

        Arguments:
            output {bytes} -- Bytes representation of value.

        Returns:
            {str} -- Formatted bytes value without whitespaces.
        """
        return output.decode('utf-8').strip()
