import locale
import json


class ThemeAttributes(object):
    def __init__(self):
        self.path = ""
        self.localized_name = {"en": "Unknown"}
        self.localized_description = {"en": "Description not specified"}
        self.localized_license = {"en": "All right reserved"}
        self.copyright = "Copyright © 2014"

    def get_description(self):
        return self.get_localized(self.localized_description)

    def get_name(self):
        return self.get_localized(self.localized_name)

    def get_license(self):
        return self.get_localized(self.localized_name)

    description = property(get_description)
    name = property(get_name)
    license = property(get_license)

    def get_localized(self, translations):
        language = locale.getlocale()[0]

        if language in translations:
            return translations[language]
        elif "en" in translations:
            return translations["en"]
        elif "en_US" in translations:
            return translations["en_US"]
        elif "en_UK" in translations:
            return translations["en_UK"]
        else:
            return dict.popitem()[1]

    def read_json_string(self, json_string):
        compiled = json.loads(json_string)
        self.localized_name = compiled["name"]
        self.localized_description = compiled["description"]
        self.localized_license = compiled["license"]
        self.copyright = compiled["copyright"]
        