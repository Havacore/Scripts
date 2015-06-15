import requests


session = requests.session()

form_data = {
	"login:AccessCard" : 472409,
	"login:Webpassword" : "password",
	"login:loginIDComboBox" : 472409
}

loginURL = "https://easyweb.td.com/waw/idp/authenticate.htm"

response = session.post(loginURL, )

print authenticate.content