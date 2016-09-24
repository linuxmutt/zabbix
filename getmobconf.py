#!/usr/bin/python
# _*_ coding: utf-8 _*_

def _getmobconf():
    confDict = {}
    mobconf = open("/home/MobileServer/mob.conf", "r")
    confline = mobconf.read();
    confDict = confline.strip("\n")
    return confDict
    mobconf.close()

def returnmobconf():
    grains = {}
    grains['mob_conf'] = _getmobconf()
    return grains
