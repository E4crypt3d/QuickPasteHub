from django import template
from pygments.lexers import TextLexer, get_lexer_by_name
from pygments import highlight as hl
from pygments.formatters import HtmlFormatter
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def highlight(text, language):
    try:
        lexer = get_lexer_by_name(language.lower(), stripall=True)
    except Exception as e:
        lexer = TextLexer()
    formatter = HtmlFormatter(style='default', noclasses=True)
    value = hl(text, lexer, formatter)
    return value
