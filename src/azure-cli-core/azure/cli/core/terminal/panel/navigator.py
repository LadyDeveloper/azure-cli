# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from prompt_toolkit.widgets.base import Frame, TextArea


class NavigatorPanel(object):
    def __init__(self):
        self.container = Frame(
            body=TextArea(text='navigator'),
            width=50
        )

    def __pt_container__(self):
        return self.container