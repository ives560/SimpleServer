import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

	Page='''\
		<html>
		<body>
		<p>Hello,web!<p>
		<table>
		<tr><td>Header</td><td>Value</td></tr>
		<tr><td>Date and time</td><td>{date_time}</td></tr>
		</table>
		</body>
		</html>
		'''

	def do_GET(self):
		page = self.create_page()
		self.send_content(page)


	def create_page(self):
		
		values={

			'date_time':self.date_time_string(),
			'path':self.path
			}
		page=self.Page.format(**values)
		return page


	def send_content(self,page):
		self.send_response(200)
		self.send_header("Content-Type","text/html")
		self.send_header("Content-Length",str(len(page)))
		self.end_headers()
		self.wfile.write(page)



if __name__=='__main__':
	serverAddress=('',8080)
	server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
	server.serve_forever()



