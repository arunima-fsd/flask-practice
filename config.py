#The WTF_CSRF_ENABLED setting activates the cross-site request forgery
# prevention (note that this setting is enabled by default in current vers
# ions of Flask-WTF).

WTF_CSRF_ENABLED = True


#The SECRET_KEY setting is only needed when CSRF is enabled, and is used
# to create a cryptographic token that is used to validate a form.
SECRET_KEY = 'you-will-never-guess'