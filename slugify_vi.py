"""Custom Vietnamese-aware slugify using unidecode."""

import re

import unidecode as _unidecode


def _slugify(text, sep="-"):
    text = _unidecode.unidecode(str(text))
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", sep, text).strip(sep)
    return text


def slugify(**kwargs):
    """Return a slugify function compatible with the toc extension."""
    sep = kwargs.get("sep", "-")
    return lambda text, separator=sep: _slugify(text, separator)
