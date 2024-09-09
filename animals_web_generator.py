import data_fetcher

def handle_fetcher_response(animal):
    response = data_fetcher.fetch_data(animal)

    if not response:
        
        return f"<h2>The animal \"{animal}\" doesn't exist.</h2>"
    elif isinstance(response, tuple):
        return f"Error: {response[0]}, error message: {response[1]['error']}"
    else:
        return generate_animal_info(response)

def get_user_input():
    while True:
        try:
            print("Please, enter a name of the animal. \n")
            animal = input("Enter here: ")
            if animal[0].islower():
                animal = animal[0].upper() + animal[1:]
            return animal
        except ValueError as e:
            print("You entered something that is not an animal! Error: ", e)

def generate_animal_info(response):
    info = ""
    for animal in response:
        name = animal.get('name', 'Unknown')
        description = animal.get('characteristics', {}).get('description', 'No description available.')
        info += f"<li class='cards__item'><h1 class='card__title'>{name}</h1><p class='card__text'>{description}</p></li>"
    return info

def replace_template_content(template_file, output_file, content):
    with open(template_file, 'r') as file:
        template = file.read()

    modified_content = template.replace('__REPLACE_ANIMALS_INFO__', content)

    with open(output_file, 'w') as file:
        file.write(modified_content)

if __name__ == "__main__":
    animal_name = get_user_input()
    animals_info = handle_fetcher_response(animal_name)
    replace_template_content('animals_template.html', 'animals.html', animals_info)