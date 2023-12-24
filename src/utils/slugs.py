from django.db.models import Model

from django.utils.text import slugify

from uuid import uuid4


def generate_unique_slug(title: str, forModel: Model) -> str:
    """The slug field of the model must be called 'slug'"""
    slug = slugify(title)
    while forModel.objects.filter(slug=slug).exists():
        slug = slugify(title) + "-" + str(uuid4())[0:4]

    return slug
