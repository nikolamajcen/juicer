#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class ProjectCommand:
    """
    Class which defines commands for project manipulation.
    """

    WHAT_VERSION = 'agvtool what-marketing-version -terse1'
    UPDATE_VERSION = 'agvtool new-marketing-version'
    WHAT_BUILD_NUMBER = 'agvtool what-version -terse'
    UPDATE_BUILD_NUMBER = 'agvtool next-version --all'
