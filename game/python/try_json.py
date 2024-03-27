import json

global quiz_title

def init_json(fp):
    init_data = {
        "name": "",
        "notes": "",
        "sentences": [],
        "keywords": [],
        "answers": [],
        "questions": []
    }
    
    with open(fp, 'w') as file:
        json.dump(init_data, file)
    


# Function to update and save the JSON file incrementally
def save_to_json(filename, new_data):
    try:
        # Load existing JSON data from the file
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, use the initial data structure
        existing_data = initial_data

    # Update the existing data with the new data
    existing_data.update(new_data)

    # Save the updated data back to the JSON file
    with open(filename, 'w') as file:
        json.dump(existing_data, file)

# Example usage: updating the JSON file with new data
new_data = {
    "notes": "This is a note.",
    "sentences": ["sentence1", "sentence2"],
    "keywords": ["keyword1", "keyword2"],
    "answers": ["answer1", "answer2"],
    "questions": ["question1", "question2"]
}
init_json(r"D:\renpy-8.1.3-sdk\Kodigo\game\python\data.json")
