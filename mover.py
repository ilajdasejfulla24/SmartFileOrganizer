import os
import shutil


class FileMover:

    def move_file(self, source, destination_folder):

        os.makedirs(
            destination_folder,
            exist_ok=True
        )

        filename = os.path.basename(source)

        destination = os.path.join(
            destination_folder,
            filename
        )

        counter = 1

        while os.path.exists(destination):

            name, ext = os.path.splitext(filename)

            destination = os.path.join(
                destination_folder,
                f"{name}_{counter}{ext}"
            )

            counter += 1

        try:

            shutil.move(
                source,
                destination
            )

        except PermissionError:

            raise Exception(
                f"Permission denied:\n{source}"
            )

        except Exception as e:

            raise Exception(str(e))

        return destination
