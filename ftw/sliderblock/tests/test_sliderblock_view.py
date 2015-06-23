import json
from ftw.builder import Builder
from ftw.builder import create
from ftw.sliderblock.testing import FTW_SLIDERBLOCK_FUNCTIONAL_TESTING
from ftw.testbrowser import browsing
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from unittest2 import TestCase


class TestSliderBlockRendering(TestCase):

    layer = FTW_SLIDERBLOCK_FUNCTIONAL_TESTING

    def setUp(self):
        super(TestSliderBlockRendering, self).setUp()
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Site Administrator'])
        self.page = create(Builder('sl content page'))

        slick_config = json.dumps(
            {'autoplay': False, 'autoplaySpeed': 1000, 'arrows': False}
        )
        self.sliderblock_slick_config = slick_config
        block_builder = Builder('sliderblock')
        block_builder.within(self.page)
        block_builder.titled('SliderBlock title')
        block_builder.having(slick_config=self.sliderblock_slick_config)
        self.block = create(block_builder)

        create(Builder('slider pane')
               .within(self.block)
               .titled(u'Pane 1')
               .with_dummy_image())
        create(Builder('slider pane')
               .within(self.block)
               .titled(u'Pane 2')
               .with_dummy_image())

    @browsing
    def test_slider_panes_visible(self, browser):
        browser.login().visit(self.block, view='@@block_view')
        self.assertEquals(2, len(browser.css('.sliderPane')))

    @browsing
    def test_custom_slick_config(self, browser):
        browser.login().visit(self.block, view='@@block_view')
        self.assertIn(self.sliderblock_slick_config,
                      browser.css('script').first.text)
