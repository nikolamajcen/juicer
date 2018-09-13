
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from argparse import ArgumentParser

class InputParser:
    """
    This class is used to define behaviour based on user input.
    """

    def  __init__(self):
        """
        Initializes default parsers.
        """
        self.__parser = ArgumentParser()
        subparsers = self.__parser.add_subparsers(dest='command')
        self.__add_version_parser(subparsers)
        self.__add_status_parser(subparsers)
        self.__add_flow_parser(subparsers)


    def parse(self):
        result = self.__parser.parse_args()
        if result.command == 'version':
            print('version')
            return

        if result.command == 'status':
            print('status')
            return

        if result.command == 'flow':
            print('flow')
            return


    def __add_version_parser(self, parser: ArgumentParser):
        _ = parser.add_parser('version',
                              help='Shows current version.')


    def __add_status_parser(self, parser: ArgumentParser):
        _ = parser.add_parser('status',
                              help='Shows current project status.')


    def __add_flow_parser(self, parser: ArgumentParser):
        push_parser = parser.add_parser('flow',
                                        help='It starts a process of pre-deployment for current changes.')
        push_parser.add_argument('-b',
                                 action='store_true',
                                 help='Increments current build number for all targets.')
        push_parser.add_argument('-p',
                                 action='store_true',
                                 help='Pushes changes to remote repository.')
        push_parser.add_argument('-t',
                                 action='store_true',
                                 help='Adds tag to current commit.')
        push_parser.add_argument('-v',
                                 action='store',
                                 help='Updates application version to provided one.',
                                 type=str)
