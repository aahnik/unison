from .models import HomeConfig, NavLink, FooterLinkCateg


def site_ctx(request):
    context = {
        "home_config": HomeConfig.get_solo(),
        "nav_links": NavLink.objects.all(),
        "footer_categories": FooterLinkCateg.objects.all(),
    }

    return context
