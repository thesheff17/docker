#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016, Dan Sheffner Digital Imaging Software Solutions, INC
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
docker_pal.py -- wrapper around docker

Usage:
completely clean build:
docker_pal.py --clean --image image_name

"""

# python imports
import subprocess
import argparse
import datetime

# pip imports


class Pal(object):

    version = "0.1"

    def __init__(self):
        pass

    def query_image(self, image_name):
        process = subprocess.Popen(['docker', 'images'], stdout=subprocess.PIPE)
        out, err = process.communicate()

        # formatting
        out1 = out.decode("utf-8")
        out2 = out1.split('\n')

        # fixes last line that is blank
        out3 = out2[:-1]

        for each in out3:
            each2 = each.split()
            if each2[0] == image_name:

                # removing the image
                command1 = ['docker', 'rmi', each2[0] + ":" + each2[1]]
                subprocess.call(command1)

    def query_container(selfi, image_name):
        command1 = "docker ps -a --format '{{.Image}} {{.Names}} {{.Status}}'"
        output = subprocess.check_output(command1, shell=True)

        # formatting
        out1 = output.decode("utf-8")
        out2 = out1.split('\n')

        # fixes last line that is blank
        out3 = out2[:-1]

        for each in out3:
            each2 = each.split()
            if each2[0] == image_name:

                # stopping containers
                if each2[2] != 'Exited':
                    command2 = ['docker', 'stop', each2[1]]
                    subprocess.call(command2)

                # removing containers
                command3 = ['docker', 'rm', each2[1]]
                subprocess.call(command3)

    def build(self, location, name):
        tag = (datetime.datetime.now().strftime("%Y%m%d"))
        command1 = 'cd ' + location + '; docker build . -t ' + name + ":" + tag
        subprocess.call(command1, shell=True)

if __name__ == "__main__":

    print ("docker_pal.py started...")
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", help="will clean docker builds",
                        action='store_true')
    parser.add_argument("--image_name", help="image name you want to clean")
    parser.add_argument("--build_location", help="location of Dockerfile")

    args = parser.parse_args()

    pal = Pal()

    if args.clean:
        pal.query_container(args.image_name)
        pal.query_image(args.image_name)
        pal.build(args.build_location, args.image_name)

    print ("docker_pal.py completed")
