install:

install ckEditor
https://github.com/django-ckeditor/django-ckeditor#installation

add to settings:

CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Full',
    },
    'default': {
        'toolbar': 'Basic',
        'height': 300,
        'width': 900,
    },
}


install nanocms

add to TEMPLATES:
  os.path.join(PROJECT_ROOT, 'nanocms/nanotemplates'),


(if not already) add django.contrib.humanize to installed_apps