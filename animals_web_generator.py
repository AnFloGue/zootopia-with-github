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
        characteristics = animal.get('characteristics', {})
        description = characteristics.get('description', 'No description available.')
        diet = characteristics.get('diet', 'Unknown')
        location = ', '.join(animal.get('locations', ['Unknown']))
        animal_type = animal.get('taxonomy', {}).get('type', 'Unknown')
        skin_type = characteristics.get('skin_type', 'Unknown')

        info += f"""
        <li class='cards__item'>
            <h1 class='card__title'>{name}</h1>
            <p class='card__text'>{description}</p>
            <p class='card__text'>Diet: {diet}</p>
            <p class='card__text'>Location: {location}</p>
            <p class='card__text'>Type: {animal_type}</p>
            <p class='card__text'>Skin Type: {skin_type}</p>
        </li>
        """
    return info

def replace_template_content(template_file, output_file, content):
    with open(template_file, 'r') as file:
        template = file.read()

    modified_content = template.replace('__REPLACE_ANIMALS_INFO__', content)

    with open(output_file, 'w') as file:
        file.write(modified_content)

    print(f"Website was successfully generated to the file {output_file}.")

if __name__ == "__main__":
    animal_name = get_user_input()
    animals_info = handle_fetcher_response(animal_name)
    replace_template_content('animals_template.html', 'animals.html', animals_info)