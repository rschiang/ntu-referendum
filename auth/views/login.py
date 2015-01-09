from datetime import datetime
from defusedxml import ElementTree as etree
from django.contrib.auth import get_user_model, create_user
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from urllib.parse import urlencode

def login(request):
    if not request.is_authenticated():
        result = request.POST.get('wresult')
        if not result:
            params = {
                'wa': 'wsignin1.0',
                'wtrealm': 'https://vote.ntuosc.org/account/login/',
                'wct': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                'wctx': urlencode({
                    'rm': 0,
                    'id': 'passive',
                    'ru': '/account/login/',
                }),
            }
            return redirect('https://adfs.ntu.edu.tw/adfs/ls/?%s' % urlencode(params))
        else:
            try:
                document = etree.fromstring(result)
            except etree.ParseError:
                return redirect('auth.views.login')

            namespaces = {
                't': 'http://schemas.xmlsoap.org/ws/2005/02/trust',
                'wsu': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd',
                'saml': 'urn:oasis:names:tc:SAML:1.0:assertion',
            }

            node = document.find("/t:RequestSecurityTokenResponse/t:RequestedSecurityToken/" +
                                 "saml:Assertion/saml:AttributeStatement/" +
                                 "saml:Attribute[@AttributeName='emailaddress']", namespaces)

            if node and node.text:
                email = node.text
                username, _, domain = email.partition('@')
                if domain != 'ntu.edu.tw':
                    return redirect('auth.views.login')

                try:
                    user = get_user_model().objects.get(username=username)
                except ObjectDoesNotExist:
                    user = create_user(username=username, email=email)
                    user.set_unusable_password()
            else:
                return redirect('auth.views.login')

    return redirect('referendum.views.next_ballot')
