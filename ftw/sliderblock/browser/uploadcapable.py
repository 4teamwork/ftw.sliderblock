from collective.quickupload.browser import uploadcapable


class SliderBlockQuickUploadCapableFileFactory(
        uploadcapable.QuickUploadCapableFileFactory):
    """ Quickupload file factory for sliderblocks.
    Make sure slider panes are created in this container."""

    def __call__(self, filename, title, description, content_type,
                 data, portal_type):

        portal_type = "ftw.slider.Pane"
        return super(SliderBlockQuickUploadCapableFileFactory, self).__call__(
            filename, title, description, content_type, data, portal_type)
