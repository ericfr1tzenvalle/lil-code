from pathlib import Path


class FileManager:
    def __init__(self) -> None:
        self.current_file: Path | None = None

    def new_file(self) -> None:
        self.current_file = None

    def open_file(self, path: str | Path) -> str:
        target = Path(path)

        if not target.exists():
            raise FileNotFoundError(f"Arquivo {path} não encontrado")

        content = target.read_text(encoding="utf-8")
        self.current_file = target
        return content

    def save_file(self, content: str) -> None:
        if self.current_file is None:
            raise RuntimeError("save_file() foi chamado sem um arquivo aberto")
        self.current_file.write_text(content, encoding="utf-8")

    def save_as(self, path: str | Path, content: str) -> None:
        target = Path(path)
        if not target.parent.exists():
            raise FileNotFoundError(f"Diretório {target.parent} não encontrado")
        target.write_text(content, encoding="utf-8")
        self.current_file = target
