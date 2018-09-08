#!/bin/sh

#
# This script updates current application version.
# Version to which app must be update needs to be provided.
#

if [ $# -eq 0] || [ -z "$0" ]; then
    # Application version is not provided
    exit 1
fi

agvtool new-marketing-version $0
