#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from pbxproj import XcodeProject

class ProjectConfigurator:
    """
    Class which is used to configure pbxproj file.
    """

    def __init__(self, path):
        self.__path = path


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
