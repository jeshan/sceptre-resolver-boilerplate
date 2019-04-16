# -*- coding: utf-8 -*-

import logging

from sceptre.resolvers import Resolver


class Main(Resolver):
    """
    Describe your resolver here
    """

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        super(Main, self).__init__(*args, **kwargs)

    def resolve(self):
        self.logger.info("Example log message")
        # self.argument, self.stack
        return 'something'
