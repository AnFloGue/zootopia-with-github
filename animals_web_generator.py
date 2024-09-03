import data_fetcher

def handle_fetcher_response(animal):
    responce = data_fetcher.fetch_data(animal)
    if responce == []:
        return f"<h2>The animal \"{animal}\" doesn't exist.</h2>"
    elif type(responce) == tuple:
        return f"Error: {responce[0]}, error message: {responce[1]['error']}"
    else:
        return generate_animal_info(responce)

def get_user_input():
    while True:
        try:
            print("Please, enter a name of the animal. \n")
            animal = input("Enter here: ")
            new_animal = ''
            if animal[0].islower():
                new_animal = animal[0].upper() + animal[1:]
                return new_animal
            else:
                return animal
        except ValueError as e:
            print("You entered something that not an animal! Error: ", e)

def generate_animal_info(response):
    name = response.get('name', 'Unknown')
    description = response.get('description', 'No description available.')
    return f"<h1>{name}</h1><p>{description}</p>"

def replace_template_content(template_file, output_file, content):
    with open(template_file, 'r') as file:
        template = file.read()
    
    modified_content = template.replace('{{content}}', content)
    
    with open(output_file, 'w') as file:
        file.write(modified_content)

if __name__ == "__main__":
    animal_name = get_user_input()
    animals_info = handle_fetcher_response(animal_name)
    replace_template_content('animals_template.html', 'animals.html', animals_info)