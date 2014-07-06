# -*- coding: utf-8 -*-
"""
This package contains the core modes.

"""
# pylint: disable=unused-import
from .autocomplete import AutoCompleteMode
from .autoindent import AutoIndentMode
from .caret_line_highlight import CaretLineHighlighterMode
from .case_converter import CaseConverterMode
from .checker import CheckerMode
from .checker import CheckerMessage
from .checker import CheckerMessages
from .code_completion import CodeCompletionMode
from .filewatcher import FileWatcherMode
from .indenter import IndenterMode
from .matcher import SymbolMatcherMode
from .right_margin import RightMarginMode
from .pygments_sh import PygmentsSH
from .wordclick import WordClickMode
from .zoom import ZoomMode
# for backward compatibility
from ..api.syntax_highlighter import PYGMENTS_STYLES
from .pygments_sh import PygmentsSH as PygmentsSyntaxHighlighter


__all__ = [
    'AutoCompleteMode',
    'AutoIndentMode',
    'CaretLineHighlighterMode',
    'CaseConverterMode',
    'CheckerMode',
    'CheckerMessage',
    'CheckerMessages',
    'CodeCompletionMode',
    'FileWatcherMode',
    'IndenterMode',
    'PygmentsSH',
    'PygmentsSyntaxHighlighter',
    'PYGMENTS_STYLES',
    'RightMarginMode',
    'SymbolMatcherMode',
    'WordClickMode',
    'ZoomMode',
]