#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class GitCommand:
    """
    Class which defines commands used for git manipulation.
    """

    ADD_CHANGES = 'git add .'
    CREATE_COMMIT = 'git commit -m "{}"'
    CREATE_TAG_WITH_MESSAGE = 'git tag "{}" -a -m "{}"'
    PUSH_CHANGES = 'git push origin HEAD --tags'
