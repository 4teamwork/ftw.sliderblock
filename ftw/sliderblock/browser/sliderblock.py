from ftw.simplelayout.browser.blocks.base import BaseBlock
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SliderBlockView(BaseBlock):
    template = ViewPageTemplateFile('templates/sliderblock.pt')

    def get_panes(self):
        return self.context.getFolderContents(full_objects=True)

    def get_slick_config(self):
        js = "jQuery(function($) {{" \
             "  $('#uid_{uid}.sliderWrapper .sliderPanes').slick({config});" \
             "}});"
        return js.format(uid=self.context.UID(),
                         config=self.context.slick_config)
