import json
import shutil
import os


class UndoManager:

    HISTORY_FILE = "logs/history.json"

    def save_action(self, source, destination):

        with open(self.HISTORY_FILE, "r") as file:
            history = json.load(file)

        history.append({
            "source": source,
            "destination": destination
        })

        with open(self.HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

    def undo_last(self):

        with open(self.HISTORY_FILE, "r") as file:
            history = json.load(file)

        if not history:
            return "Nothing to undo"

        last_action = history.pop()

        if os.path.exists(last_action["destination"]):

            shutil.move(
                last_action["destination"],
                last_action["source"]
            )

        with open(self.HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

        return "Last action undone successfully."
