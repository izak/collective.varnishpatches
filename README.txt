collective.varnishpatches
=========================

With LinguaPlone installed, the plone LanguageTool sets the I18N_LANGUAGE
cookie on every request (if it is not there), wreaking havoc with varnish's
caching.

This is a patch that ensures the cookie is only set when someone actually
changes the language, that is, when set_language is on the request.
