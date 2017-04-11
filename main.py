import webapp2

class SomeClass(webapp2.RequestHandler):
	def get(self):
		#set http header
		self.response.headers['Content-Type']='text/plain'

		#writing something to the response page

		#method 1
		self.response.write('Hello')

		"""method 2
		if present, value returned by this method
		overrides the previous line"""
		return webapp2.Response("hello world!")


#WSGIAppllication(urlmapping,debug flag)
app=webapp2.WSGIApplication([('/',SomeClass),],debug=False)
