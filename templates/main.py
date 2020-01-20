#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstanceStatusRequest import DescribeInstanceStatusRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shenzhen')

request = DescribeInstanceStatusRequest()
request.set_accept_format('json')

request.set_ZoneId("cn-shenzhen-e")
request.set_PageNumber(1)
request.set_PageSize(50)

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
