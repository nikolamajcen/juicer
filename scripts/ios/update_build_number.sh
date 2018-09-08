#!/bin/sh

#
# This script updates current application build number.
# Build number is incremented by one.
#

agvtool next-version -all
