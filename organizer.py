import os

from scanner import FileScanner
from classifier import FileClassifier
from mover import FileMover
from logger_manager import LoggerManager
from undo_manager import UndoManager


class FileOrganizer:

    def __init__(self):

        self.scanner = FileScanner()
        self.classifier = FileClassifier()
        self.mover = FileMover()
        self.logger = LoggerManager()
        self.undo_manager = UndoManager()

    def organize(self, folder_path, stop_callback=None):

        files = self.scanner.scan(folder_path)

        moved_count = 0

        for file in files:

            if stop_callback and stop_callback():
                return "Organization stopped."

            category = self.classifier.classify(file)

            destination_folder = os.path.join(
                folder_path,
                category
            )

            new_location = self.mover.move_file(
                file,
                destination_folder
            )

            self.logger.log_move(
                file,
                new_location
            )

            self.undo_manager.save_action(
                file,
                new_location
            )

            moved_count += 1

        return f"{moved_count} files organized."
