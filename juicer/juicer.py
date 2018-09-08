#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from utilities.ios.configurator import ProjectConfigurator
from utilities.ios.inspector import ProjectInspector

class Juicer:
    """
    Initial class which implements functionalities for iOS deployment.
    """

    @staticmethod
    def start():
        """
        It starts pre-deployment process of an iOS application.
        """
        configurator = ProjectConfigurator('res/Juicer/Juicer.xcodeproj/project.pbxproj')
        configurator.enable_versioning()

        inspector = ProjectInspector('res/Juicer/')
        print("versioning enabled:", inspector.is_versioning_enabled())
        print("version:", inspector.get_version())
        print("build number:",inspector.get_build_number())
