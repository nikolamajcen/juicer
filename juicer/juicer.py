#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from platforms.ios.configurator import ProjectConfigurator
from platforms.ios.inspector import ProjectInspector
from versioning.git.versioner import GitVersioner

class Juicer:
    """
    Initial class which implements functionalities for iOS deployment.
    """

    @staticmethod
    def start():
        """
        It starts pre-deployment process of an iOS application.
        """
        configurator = ProjectConfigurator('res/Juicer/', 'res/Juicer/Juicer.xcodeproj/project.pbxproj')
        inspector = ProjectInspector('res/Juicer/')

        if inspector.is_versioning_enabled() == False:
            configurator.enable_versioning()

        print()
        print("Versioning enabled:", inspector.is_versioning_enabled())
        print("Version:", inspector.get_version()[1])
        print("Build number:",inspector.get_build_number()[1])

        print()
        print(configurator.update_version("3.0.0")[1])
        print(configurator.update_build_number()[1])

        versioner = GitVersioner('res/Juicer/')
        versioner.add_changes()
        versioner.create_commit("Examle commit")
        versioner.create_tag("555_555")
        versioner.push_changes()