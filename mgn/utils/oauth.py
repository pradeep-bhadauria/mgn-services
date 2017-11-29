from rauth import OAuth1Service, OAuth2Service
from flask import url_for, request, redirect
from mgn.utils.config import OAUTH_CREDENTIALS


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = OAUTH_CREDENTIALS[provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self, mgn_user_type_id, auth_type_id):
        return url_for('auth.oauth_callback', provider=self.provider_name, mgn_user_type_id=mgn_user_type_id,
                       auth_type_id=auth_type_id, _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[str(provider_name)]


class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
                name='facebook',
                client_id=self.consumer_id,
                client_secret=self.consumer_secret,
                authorize_url='https://graph.facebook.com/oauth/authorize',
                access_token_url='https://graph.facebook.com/oauth/access_token',
                base_url='https://graph.facebook.com/'
        )

    def authorize(self, mgn_user_type_id, auth_type_id):
        return redirect(self.service.get_authorize_url(
                scope='email',
                response_type='code',
                redirect_uri=self.get_callback_url(mgn_user_type_id, auth_type_id)
        ))

    def callback(self, mgn_user_type_id=None, auth_type_id=None):
        if 'code' not in request.args:
            return None, None, None, None, None
        oauth_session = self.service.get_auth_session(
                data={'code': request.args['code'],
                      'grant_type': 'authorization_code',
                      'redirect_uri': self.get_callback_url(mgn_user_type_id,auth_type_id)}
        )
        me = oauth_session.get('me?fields=id,first_name,last_name,email,picture.type(large)').json()
        return (
            'facebook$' + me['id'],
            me.get('email'),
            me.get('first_name'),
            me.get('last_name'),
            me.get('picture')
        )
