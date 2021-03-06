#! /usr/bin/env python

from setuptools import setup
import os
import commands

def list_files(target_dir, install_dir):
    '''List files for option `data_files`.'''
    results = []
    for root, dirs, files in os.walk(target_dir):
        for filepath in files:
            data_dir = os.path.dirname(os.path.join(root, filepath))
            data_file = os.path.join(root, filepath)
            results.append((data_dir, [data_file]))
            print results
    return results                

def pkg_config_cflags(pkgs):
    '''List all include paths that output by `pkg-config --cflags pkgs`'''
    return map(lambda path: path[2::], commands.getoutput('pkg-config --cflags-only-I %s' % (' '.join(pkgs))).split())

setup(name='dsc',
      version='0.1',
      description='Deepin software center.',
      long_description ="""Deepin software center.""",
      author='Linux Deepin Team',
      author_email='wangyong@linuxdeepin.com',
      license='GPL-3',
      url="https://github.com/manateelazycat/deepin-software-center",
      download_url="git://github.com/manateelazycat/deepin-software-center.git",
      platforms = ['Linux'],
      )

