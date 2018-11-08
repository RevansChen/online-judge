# Python3

from solution1 import xmlTags as f

qa = [
    ('<data><animal name="cat"><genus>Felis</genus><family name="Felidae" subfamily="Felinae"/><similar name="tiger" size="bigger"/></animal><animal name="dog"><family name="Canidae" member="canid"/><order>Carnivora</order><similar name="fox" size="similar"/></animal></data>',
     ['data()',
      '--animal(name)',
      '----genus()',
      '----family(member, name, subfamily)',
      '----similar(name, size)',
      '----order()']),
    ('<products><product><TITLE> product #1 </TITLE><PRICE> 10.00 </PRICE></product><product><TITLE> product #2 </TITLE><PRICE> 20.00 </PRICE></product></products>',
     ['products()',
      '--product()',
      '----TITLE()',
      '----PRICE()']),
    ('<here urlid="blah-blah"><component type="Documents" context="User"><displayName>My Video</displayName><role role="Data"><detects><detect><condition>Helper.hasObject</condition></detect></detects><rules><include filter="Helper.IgnoreIrrelevantLinks"><objectSet><pattern type="File"></pattern></objectSet></include></rules></role></component></here>',
     ['here(urlid)',
      '--component(context, type)',
      '----displayName()',
      '----role(role)',
      '------detects()',
      '--------detect()',
      '----------condition()',
      '------rules()',
      '--------include(filter)',
      '----------objectSet()',
      '------------pattern(type)']),
    ('<a></a>',
     ['a()']),
    ('<PHONEBOOK><PERSON><NAME>Joe Wang</NAME><EMAIL>joe@yourserver.com</EMAIL><TELEPHONE>202-999-9999</TELEPHONE><WEB>www.java2s.com</WEB></PERSON><PERSON><NAME>Karol</NAME><EMAIL>karol@yourserver.com</EMAIL><TELEPHONE>306-999-9999</TELEPHONE><WEB>www.java2s.com</WEB></PERSON><PERSON><NAME>Green</NAME><EMAIL>green@yourserver.com</EMAIL><TELEPHONE>202-414-9999</TELEPHONE><WEB>www.java2s.com</WEB></PERSON></PHONEBOOK>',
     ['PHONEBOOK()',
      '--PERSON()',
      '----NAME()',
      '----EMAIL()',
      '----TELEPHONE()',
      '----WEB()']),
    ('<outer attr1="lol hello" attr2="pal how are you">hello</outer>',
     ['outer(attr1, attr2)'])
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = f(*q)
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()
