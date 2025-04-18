import requests
import json


API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "iW1MsjidDZudxSWyk46tTg==ODsquybYVL1j077z"
OUTPUT_FILE = "animals.html"


def get_animal_data(name):
    """ gets the user input as JSON data from the animal API """
    response = requests.get(API_URL + name, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("❌ Error:", response.status_code, response.text)
        return []


def serialize_animal(animal):
    """ returns a string of HTML for the given animal """
    output = ""
    animal_name = animal['name'].replace("’", "'")
    output += "<li class='cards__item'>\n"
    if "name" in animal:
        output += f"\t<div class='card__title'>{animal_name}</div>\n"
    output += "\t\t<p class='card__text'>\n"
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"\t\t\t<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    if "locations" in animal and animal["locations"]:
        output += f"\t\t\t<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"\t\t\t<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    output += "\t\t</p>\n"
    output += "</li>\n"
    return output


def load_template(file_path):
    """ loads the HTML template """
    with open(file_path, "r", encoding="utf-8") as fileobj:
        return fileobj.read()


def insert_animals_into_template(template, animals_string):
    """ replaces placeholder in template with the animal HTML"""
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_string)


def save_html(data, file_name):
    """ saves final HTML to file"""
    with open(file_name, "w", encoding="utf-8") as fileobj:
        fileobj.write(data)


def main():
    name = input("Enter a name for an animal: ")
    animal_data = get_animal_data(name)
    if not animal_data:
        output = f"<h2>The animal \"{name}\" doesn't exist.</h2>\n"
    else:
        output = ""
        for animal in animal_data:
            output += serialize_animal(animal)
    template = load_template("animals_template.html")
    final_html = insert_animals_into_template(template, output)
    save_html(final_html, OUTPUT_FILE)
    print(f"✅ Website was successfully generated to the file {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
