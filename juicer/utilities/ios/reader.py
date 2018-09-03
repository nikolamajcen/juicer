#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class ProjectReader:
    """
    This class is used to read project informations from iOS project file.
    """

    def read_property(self, property_name: str) -> str:
        """
        This method reads property value for provided name from project file.

        Arguments:
            property_name {str} -- Property name in project file.

        Returns:
            str -- Property value as str from project file.
        """
        return 'project_value'