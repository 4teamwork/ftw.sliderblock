import json
from Acquisition._Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from ftw.simplelayout.browser.blocks.base import BaseBlock
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SliderBlockView(BaseBlock):
    template = ViewPageTemplateFile('templates/sliderblock.pt')

    def get_panes(self):
        return self.context.getFolderContents(full_objects=True)

    def get_slick_config(self):
        # The config value may contain unwanted new lines. Let's remove them
        # by loading and dumping as json.
        config = json.loads(self.context.slick_config)
        return json.dumps(config)

    def can_add(self):
        context = aq_inner(self.context)
        mtool = getToolByName(context, 'portal_membership')
        permission = mtool.checkPermission('ftw.sliderblock: Add SliderBlock',
                                           context)
        return bool(permission)
