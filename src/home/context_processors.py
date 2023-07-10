from .models import SiteConfig, NavLink, FooterLinkCateg, SocialLink


def site_ctx(request):
    context = {
        "site_config": SiteConfig.get_solo(),
        "nav_links": NavLink.objects.all(),
        "footer_categories": FooterLinkCateg.objects.all(),
        "social_links": SocialLink.objects.all()
    }

    return context
