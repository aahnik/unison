from .models import HomeConfig, NavLink, FooterLinkCateg


def site_ctx(request):
    home_config = HomeConfig.get_solo()
    nav_links = NavLink.objects.all()
    footer_categories = FooterLinkCateg.objects.all()

    context = {
        "home_config": home_config,
        "nav_links": nav_links,
        "footer_categories": footer_categories,
    }

    return context