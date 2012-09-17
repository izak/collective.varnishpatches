def LanguageTool__call__(self, container, req):
    """The __before_publishing_traverse__ hook.

    Patched to *not* set the language cookie, as this breaks varnish caching.
    """
    self._old___call__(container, req)
    if 'I18N_LANGUAGE' in req.response.cookies:
        if 'set_language' in req.form:
            return None
        del req.response.cookies['I18N_LANGUAGE']
