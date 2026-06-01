import os


class FileClassifier:

    CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".doc", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    def classify(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        for category, extensions in self.CATEGORIES.items():

            if extension in extensions:
                return category

        return "Others"
