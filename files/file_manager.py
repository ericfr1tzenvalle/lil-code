from pathlib import Path


class FileManager:
    def __init__(self) -> None:
        self.current_file: Path | None = None
        self.saved_content: str = ""

    def new_file(self) -> None:
        self.current_file = None
        self.saved_content = ""

    def open_file(self, path: str | Path) -> str:
        target = Path(path)
        content = target.read_text(encoding="utf-8")
        self.current_file = target
        self.saved_content = content
        return content

    def save_file(self, content: str) -> None:
        if self.current_file is None:
            raise RuntimeError("save_file() foi chamado sem um arquivo aberto")
        self.current_file.write_text(content, encoding="utf-8")
        self.saved_content = content

    def save_as(self, path: str | Path, content: str) -> None:
        target = Path(path)
        target.write_text(content, encoding="utf-8")
        self.current_file = target
        self.saved_content = content

    def has_unsaved_changes(self, current_content: str) -> bool:
        return current_content != self.saved_content
