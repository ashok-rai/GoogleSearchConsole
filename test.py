import searchconsole
account = searchconsole.authenticate(client_config='client_secrets.json')
webproperty = account['https://www.example.com/']
report = webproperty.query.range('today', days=-7).dimension('query').get()
print(report.rows)