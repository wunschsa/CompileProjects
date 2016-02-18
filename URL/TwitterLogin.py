url = 'https://mobile.twitter.com/session/new'

import mechanize
br = mechanize.Browser()
br.open(url)

#response = br.response()
#response.set_data(response.get_data().replace("<br/>", "<br />")) #Python mechanize is broken, fixing it.
#br.set_response(response)

#br=mechanize.Browser(factory=mechanize.RobustFactory())

print [form for form in br.forms()][0]

#for f in br.forms():
#    print f

br.select_form(nr=0)

br.form['username'] = 'sawunsch'
br.form['password'] = 'RoxyPid32'
br.submit()

htmltext = br.open('https://mobile.twitter.com/account').read()
print 'sopier' in htmltext

