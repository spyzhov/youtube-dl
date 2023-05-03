from __future__ import unicode_literals

from .common import PostProcessor


class CallAfterDownloadPP(PostProcessor):
    def __init__(self, downloader, callback: callable):
        super(CallAfterDownloadPP, self).__init__(downloader)
        self.callback = callback

    def run(self, information):
        return self.callback(information)
