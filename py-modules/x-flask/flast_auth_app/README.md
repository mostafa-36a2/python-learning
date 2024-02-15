Tutorial: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

This app will use the Flask app factory pattern with blueprints. One blueprint handles the regular routes, which include the index and the protected profile page. Another blueprint handles everything auth-related. In a real app, you can break down the functionality in any way you like, but the solution covered here will work well for this tutorial.

## Flask config
```python3
{
    'ENV': 'production',
    'DEBUG': False,
    'TESTING': False,
    'PROPAGATE_EXCEPTIONS': None,
    'SECRET_KEY': None,
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31),
    'USE_X_SENDFILE': False,
    'SERVER_NAME': None,
    'APPLICATION_ROOT': '/',
    'SESSION_COOKIE_NAME': 'session',
    'SESSION_COOKIE_DOMAIN': None,
    'SESSION_COOKIE_PATH': None,
    'SESSION_COOKIE_HTTPONLY': True,
    'SESSION_COOKIE_SECURE': False,
    'SESSION_COOKIE_SAMESITE': None,
    'SESSION_REFRESH_EACH_REQUEST': True,
    'MAX_CONTENT_LENGTH': None,
    'SEND_FILE_MAX_AGE_DEFAULT': None,
    'TRAP_BAD_REQUEST_ERRORS': None,
    'TRAP_HTTP_EXCEPTIONS': False,
    'EXPLAIN_TEMPLATE_LOADING': False,
    'PREFERRED_URL_SCHEME': 'http',
    'JSON_AS_ASCII': None,
    'JSON_SORT_KEYS': None,
    'JSONIFY_PRETTYPRINT_REGULAR': None,
    'JSONIFY_MIMETYPE': None,
    'TEMPLATES_AUTO_RELOAD': None,
    'MAX_COOKIE_SIZE': 4093
    }
 ```