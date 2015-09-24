from Acquisition._Acquisition import aq_inner
from ftw.simplelayout.browser.blocks.base import BaseBlock
from ftw.slider import _
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.i18n import translate
import json


class SliderBlockView(BaseBlock):
    template = ViewPageTemplateFile('templates/sliderblock.pt')

    def get_panes(self):
        return self.context.getFolderContents(full_objects=True)

    def extend_translations(self, config):
        translations = {
            'play': translate(_(u'label_slider_play', default=u'Play'),
                              context=self.request),
            'pause': translate(_(u'label_slider_pause', default=u'Pause'),
                               context=self.request),
            'next': translate(_(u'label_slider_next', default=u'Next'),
                              context=self.request),
            'prev': translate(_(u'label_slider_prev', default=u'Previous'),
                              context=self.request),
        }
        config['labels'] = translations
        return config

    def get_slick_config(self):
        # The config value may contain unwanted new lines. Let's remove them
        # by loading and dumping as json.
        if not self.context.slick_config:
            return '{}'
        config = self.extend_translations(json.loads(self.context.slick_config))
        return json.dumps(config)

    def can_add(self):
        context = aq_inner(self.context)
        mtool = getToolByName(context, 'portal_membership')
        permission = mtool.checkPermission('ftw.sliderblock: Add SliderBlock',
                                           context)
        return bool(permission)
