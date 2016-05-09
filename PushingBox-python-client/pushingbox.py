#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" PushingBox API wrapper """


import urllib.request
import urllib.parse


class PushingBox():

    def __init__(self, dev_id, **kwargs):
        """
        :param dev_id: pushing device identifier like 'h1234567890ABCDEF'
        :param kwargs: additional API call parameters, which can be used to pass specific info like temperature etc.
                       In the notification template defined at PushBox you can use placeholders like $temperature$
        :return: nothing
        """
        self.url = 'http://api.pushingbox.com/pushingbox'
        self.values = {'devid' : dev_id}
        self.values.update(kwargs)
  
    def push(self, **kwargs):
        """
        Sends a push request
        :param kwargs: additional API call parameters
        :return: True, if success
                 False, "Exception message", if exception occurred
        """
        try:
            self.values.update(kwargs)
            data = urllib.parse.urlencode(self.values).encode('utf-8')
            req = urllib.request.Request(self.url, data)
            response = urllib.request.urlopen(req)
            # print(response.read().decode('utf-8'))
            return True, ""
        except Exception as inst:
            return False, inst



