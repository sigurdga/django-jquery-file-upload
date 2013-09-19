# encoding: utf-8
import mimetypes
import re
from django.core.urlresolvers import reverse


def order_name(name):
    """order_name -- Limit the name to 20 chars length, and convert to a
    ellipsed string.

    name -- text to be limited.

    """
    name = re.sub(r'^.*/', '', name)
    if len(name)>20:
        return name[:10] + "..." + name[-7:]
    else:
        return name


def serialize(instance):
    """serialize -- Serialize a Picture instance into a `json` object.

    instance -- Picture instance
    """
    return {
        'url': instance.file.url,
        'name': order_name(instance.file.name),
        'type': mimetypes.guess_type(instance.file.path)[0] or 'image/png',
        'thumbnailUrl': instance.file.url,
        'size': instance.file.size,
        'deleteUrl': reverse('upload-delete', args=[instance.pk]),
        'deleteType': 'DELETE',
    }


