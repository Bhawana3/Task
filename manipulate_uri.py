# -*- coding: utf-8 -*-
import re

"""
URI:
scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
https://root:password@localhost:80/phpmyadmin/index.html?q=a:b#fragment
"""

class URI:
    # contructor function
    def __init__(self,uri):
        self.uri = uri

        self.scheme = self.get_scheme()
        self.path = self.get_path()
        self.query_params = self.get_query_params()
        self.fragment = self.get_fragment()
        self.user = self.get_user()
        self.password = self.get_password()

    def update_URI(self):
        self.uri = self.scheme + ':'
        if (self.user is not None) and (self.password is not None):
            self.uri += ('//' + self.user + ':' + self.password + '@')
        if self.path is not None:
            self.uri += ('/' + self.path)
        if self.query_params is not None:
            self.uri += '?'
            for key in self.query_params.keys():
                self.uri += (key + '=' + (self.query_params)[key] + '&')
        if self.fragment is not None:
            self.uri += ('#' + self.fragment)
        return self.uri

    # get scheme from given uri
    def get_scheme(self):
        pat = r'(?:[a-zA-Z]+[a-zA-Z0-9+.-]*):'
        matched_part = re.match(pat, self.uri)
        if matched_part:
            scheme = matched_part.group()[:-1]
            return scheme
        else:
            return None

    def get_user(self):
        pat = r'^(.*):(\s*)([^:]*):(.*)'
        matched_part = re.match(pat, self.uri)
        if matched_part:
            print matched_part.group(2)
            print matched_part.group(3)
            print matched_part.group(4)
            user = matched_part.group(4)
            print ''
            return user
        else:
            return None

    def get_password(self):
        pat = r'^(?:(.*)):(//)?([^:]*:[^@]*@)?(/[^?#]*)(\?.*)?(#.*)?'
        matched_part = re.match(pat, self.uri)
        if matched_part:
            user_and_pass = matched_part.group(3)
            if user_and_pass is None:
                return user_and_pass
            else:
                user = user_and_pass.split(':')[1]
                return user
        else:
            return None

    # scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
    # https://root:password@localhost:80/phpmyadmin/index.html?q=a:b#fragment
    # mailto: yourname@example.com/hello/world

    # get path from given uri
    def get_path(self):
        pat = r'^(.*):(//)?[^/]*(/[^?#]*)(\?.*)?(#.*)?'
        matched_part = re.match(pat, self.uri)
        if matched_part:
            path = matched_part.group(3)
            return path
        else:
            return None

    # get query and fragment from given uri
    def get_fragment(self):
        pat = r'^(.+?)(\?.+?)?#(.+)?$'
        matched_part = re.match(pat, self.uri)
        if matched_part:
            fragment = matched_part.group(3)
            return fragment
        else:
            return None

    def get_query_params(self):
        pat = r'^(.+?)\?(.+?)?(#.+)?$'
        matched_part = re.match(pat, self.uri)
        if matched_part:
            query = matched_part.group(2)
            key_value_pairs = query.split('&')
            query_params = dict()
            for pair in key_value_pairs:
                pair = pair.split('=')
                query_params[pair[0]] = pair[1]
            return query_params
        else:
            return None


    def add_or_update_query_strings (self, q=dict()):
        try:
            if self.query_params != None:
                for key in q.keys():
                    self.query_params[key] = q[key]
            else:
                self.query_params = q
            self.update_URI()
            return True
        except Exception as e:
            raise e


if __name__ == '__main__':
    url = URI('https://root:pass@www.google.com/home/index.html?q=10&a=20#abc')
    #url = URI('mailto: yourname@example.com/hello/world')
    print "scheme :",url.scheme
    print "path :",url.path
    print "query parameters :",url.query_params
    print "fragment :",url.fragment
    print "user :",url.user
    print "password :",url.password
    print url.add_or_update_query_strings({'q':'3','a':'5'})
    print url.update_URI()
