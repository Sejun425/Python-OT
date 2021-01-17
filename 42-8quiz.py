def html_tag(tag_name):
    def real_decorator(func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(tag_name, func())
        return wrapper
    return real_decorator