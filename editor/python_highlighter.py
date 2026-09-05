from editor.syntax_highlighter import HighlightRule, SyntaxHighlighter
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtCore import QRegularExpression

class PythonHighlighter(SyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.rules = [
            self.create_keyword_rule(),
            self.create_builtin_rule(),
            self.create_literal_constant_rule(),
            self.create_operator_rule(),
            self.create_number_rule(),
            self.create_decorator_rule(),
            self.create_function_definition_rule(),
            self.create_class_definition_rule(),
            self.create_comment_rule(),
            self.create_string_rule(),
        ]

    def create_keyword_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#E5A3FF'))
        rule_pattern = QRegularExpression(
            r'\b(and|as|assert|async|await|break|class|continue|def|del|'
            r'elif|else|except|finally|for|from|global|if|import|in|is|'
            r'lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b'
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_builtin_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#FFF176'))
        rule_pattern = QRegularExpression(
            r'\b(abs|aiter|all|anext|any|ascii|bin|bool|breakpoint|bytearray|'
            r'bytes|callable|chr|classmethod|compile|complex|delattr|dict|dir|'
            r'divmod|enumerate|eval|exec|filter|float|format|frozenset|getattr|'
            r'globals|hasattr|hash|help|hex|id|input|int|isinstance|issubclass|'
            r'iter|len|list|locals|map|max|memoryview|min|next|object|oct|open|'
            r'ord|pow|print|property|range|repr|reversed|round|set|setattr|'
            r'slice|sorted|staticmethod|str|sum|super|tuple|type|vars|zip|__import__)\b'
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_literal_constant_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#FFB86C'))
        rule_pattern = QRegularExpression(r'\b(True|False|None)\b')
        return HighlightRule(rule_pattern, rule_format)

    def create_number_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#FFB86C'))
        rule_pattern = QRegularExpression(
            r'(?<!\w)(?:0[xX](?:_?[0-9a-fA-F])+|0[bB](?:_?[01])+'
            r'|0[oO](?:_?[0-7])+|(?:[0-9](?:_?[0-9])*(?:\.(?:[0-9](?:_?[0-9])*)?)?'
            r'|\.[0-9](?:_?[0-9])*)(?:[eE][+-]?[0-9](?:_?[0-9])*)?[jJ]?)(?!\w)'
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_operator_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#F4F7FF'))
        rule_pattern = QRegularExpression(
            r'\*\*=?|//=?|<<=?|>>=?|:=|->|[+\-*/%@&|^]=?|[<>=!]=|[<>=~]'
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_decorator_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#FF8FCC'))
        rule_pattern = QRegularExpression(
            r'^\s*\K@[^\W\d]\w*(?:\.[^\W\d]\w*)*',
            QRegularExpression.PatternOption.UseUnicodePropertiesOption,
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_function_definition_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#70DDFF'))
        rule_pattern = QRegularExpression(
            r'\bdef\s+\K[^\W\d]\w*',
            QRegularExpression.PatternOption.UseUnicodePropertiesOption,
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_class_definition_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#5FF2D6'))
        rule_pattern = QRegularExpression(
            r'\bclass\s+\K[^\W\d]\w*',
            QRegularExpression.PatternOption.UseUnicodePropertiesOption,
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_string_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#B4F58C'))
        rule_pattern = QRegularExpression(
            r'''(?i:\b(?:br|rb|fr|rf|r|u|b|f))?(?:"(?:\\.|[^"\\])*(?:"|$)|'(?:\\.|[^'\\])*(?:'|$))'''
        )
        return HighlightRule(rule_pattern, rule_format)

    def create_comment_rule(self) -> HighlightRule:
        rule_format = QTextCharFormat()
        rule_format.setForeground(QColor('#91A9BD'))
        rule_pattern = QRegularExpression(r'#[^\n]*')
        return HighlightRule(rule_pattern, rule_format)
