#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @version: 1.0
    @author : Carrot
    @time   : 16/8/30 19:33
"""

from socket import *
from time import ctime
import json
import struct
import wpbMessage
import WPBCmd

PACKAGELEN = 4      # 包长
PACKHEADLEN = 20    # 包头长
BUFSIZE = 1024
HOST = ("wptest.baidao.com", 9103)

class WPBSocket(object):
	def __init__(self, host):
		super.__init__()
		assert host
		self.svr = None
		self.host = host
		self.connect()
	
	def connect(self):
		self.svr = socket(AF_INET, SOCK_STREAM)
		self.svr.recv()
		return self.svr.connect_ex(self.host)

seq = 0
def test():
	try:
		svr = socket(AF_INET, SOCK_STREAM)
		svr.connect(HOST)
		while True:
			totalLen = svr.recv(PACKAGELEN)
			length = struct.unpack('!i', totalLen)
			data = svr.recv(length[0] - PACKAGELEN)
			# data = svr.recv(length[0] - PACKAGELEN - PACKHEADLEN)
			# print ctime() + '收到数据:Len[%d]' % length
			msg = wpbMessage.WPBMessage()
			msg.initFromData(data, '')
			if msg.cmdNo != WPBCmd.AgQuote:
				print msg.getResult()
		# print json.dumps(data)
	except Exception, e:
		print e
		
def main():
	try:
		svr = socket(AF_INET, SOCK_STREAM)
		svr.connect(HOST)
		while True:
			lenPack = svr.recv(PACKAGELEN)
			length = struct.unpack('!i', lenPack)
			headLenPack = svr.recv(PACKHEADLEN)
			# length = struct.unpack('!i', lenPack)
			data = svr.recv(length[0] - PACKAGELEN - PACKHEADLEN)
			# print chardet.detect(data)
			print ctime() + '收到数据:Len[%d]' % length
			# print data
			print json.loads(data)
			# print json.dumps(data)
	except Exception, e:
		print e


if __name__ == '__main__':
	test()
