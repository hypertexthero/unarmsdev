from django import template

def if_current_section(context, link_url, positive=True, negative=False, startswith='false'):
    """
    Return one of the passed parameters if the URL passed is the current one.
    For consistency reasons, we use the link_url of the page.
    smg - added startswith, if 'true' operate on url startswith instead of whole url.
  
    Usage: <li class="dropdown {% if_current_section '/photos/' 'active' '' 'true' %}">
  
    https://github.com/eudicots/Cactus/issues/164
    """
    page = context['__CACTUS_CURRENT_PAGE__']
    if startswith == 'true':  # smg - mods as above in docstring
        return positive if page.link_url.startswith(link_url) else negative
    else:
        return positive if page.link_url == link_url else negative

def preBuild(site):
    register = template.Library()
    register.simple_tag(takes_context=True)(if_current_section)
    template.base.builtins.append(register)

