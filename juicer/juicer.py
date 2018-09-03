#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from utilities.ios.reader import ProjectReader

class Juicer:
    """
    Initial class which implements functionalities for iOS deployment.
    """

    @staticmethod
    def start():
        """
        It starts pre-deployment process of an iOS application.
        """
        print("Juicer started...")
        reader = ProjectReader()
        property = reader.read_property('property')
        print("Something...")
        print(property)
