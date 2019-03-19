from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.core.models import Page as WagtailPage
from wagtail.images.models import Image
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

import math

class BlogIndexPage(WagtailPage):

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse chronology
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(WagtailPage):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    intro = models.CharField(max_length=250, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    display_image = models.OneToOneField(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    content_panels = WagtailPage.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('display_image'),
            FieldPanel('intro'),
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('body'),
    ]

    def word_count(self):
        count = len(self.body.split())
        return count

    def min_to_read(self):
        avg_wpm = 225
        return math.ceil(self.word_count() / avg_wpm)


class BlogTagIndexPage(WagtailPage):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


# class DisplayImage(Image):
#     post = models.OneToOneField(
#         'BlogPage',
#         on_delete=models.CASCADE,
#     )
