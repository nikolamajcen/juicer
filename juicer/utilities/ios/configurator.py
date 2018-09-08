#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from pbxproj import XcodeProject
from utilities.ios.commander import ProjectCommander

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
        self.__commander = ProjectCommander(project_dir)
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
        project.remove_flags('CURRENT_PROJECT_VERSION')
        project.add_flags('VERSIONING_SYSTEM', 'apple-generic')
        project.save()


    def update_version(self, version: str) -> (bool, str):
        """
        Updates current application version to provided one.

        Arguments:
            version {str} -- Defines new version.

        Returns:
            {(bool, str)} -- Returns bool flag for success and output from process.
        """
        process = self.__commander.execute("{} {}".format(ProjectCommander.COMMAND_UPDATE_VERSION, version))
        (output, _) = process.communicate()
        return (process.returncode == 0, output)


    def update_build_number(self) -> (bool, str):
        """
        Updates current build number of the application.

        Returns:
            {(bool, str)} -- Returns bool flag for success and output from process.
        """
        process = self.__commander.execute(ProjectCommander.COMMAND_UPDATE_BUILD_NUMBER)
        (output, _) = process.communicate()
        return (process.returncode == 0, output)
