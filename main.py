#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#import webapp2
#from google.appengine.api import users
#
#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        user = users.get_current_user()
#
#        if user:
#            self.response.headers['Content-Type'] = 'text/plain'
#            self.response.out.write('Hello, ' + user.nickname())
#        else:
#            self.redirect(users.create_login_url(self.request.uri))
#
#app = webapp2.WSGIApplication([('/', MainPage)],
#    debug=True)
import web

urls = (
    "/.*", "hello",
    )

app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

app = app.gaerun()