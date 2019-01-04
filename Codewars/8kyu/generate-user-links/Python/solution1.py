# Python - 2.7.6

from urllib import quote

generate_link = lambda user: 'http://www.codewars.com/users/%s' % quote(user)
