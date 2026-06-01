import os


class FileScanner:

    def scan(self, folder_path):

        files = []

        for item in os.listdir(folder_path):

            full_path = os.path.join(folder_path, item)

            if os.path.isfile(full_path):
                files.append(full_path)

        return files
