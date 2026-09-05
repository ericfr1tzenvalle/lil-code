from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat
from PySide6.QtCore import QRegularExpression
from dataclasses import dataclass

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.rules = []

    def highlightBlock(self, text: str) -> None:
        for rule in self.rules:
            matches = rule.pattern.globalMatch(text)
            while matches.hasNext():
                match = matches.next()
                self.setFormat(
                    match.capturedStart(),
                    match.capturedLength(),
                    rule.format
                )

@dataclass
class HighlightRule:
    pattern: QRegularExpression
    format: QTextCharFormat 