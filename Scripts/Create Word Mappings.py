from PIL import Image
import os

# Function to get the starting index based on the number of lines in the text file
def get_start_index(text_file_path):
    if os.path.exists(text_file_path):
        with open(text_file_path, 'r') as f:
            lines = f.readlines()
        return len(lines)
    else:
        return 0

# Function to process an image and append results to a text file
def process_image(image_path, target_dir, text_file_path, labels_list):
    image = Image.open(image_path)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)  # Create the directory if it doesn't exist

    # List of string labels
    chiffres = labels_list

    # Determine the starting index
    start_index = get_start_index(text_file_path)

    # Open the text file for appending
    with open(text_file_path, 'a') as f:
        for i in range(80):
            padding_right = 10
            padding_left = 25
            padding_top = 15
            padding_bottom = 15
            left = (i % 5) * 190 + padding_left
            right = (i % 5) * 190 + 190 - padding_right
            top = (i // 5) * 80 + padding_top
            bottom = (i // 5) * 80 + 80 - padding_bottom
            cropped_image = image.crop((left, top, right, bottom))
            label = chiffres[i // 5]  # The label is determined by the row number
            if label == "":
                continue
            image_file_name = f'{label}_{start_index + i}.png'
            save_path = os.path.join(target_dir, image_file_name)
            cropped_image.save(save_path)
            
            # Write the image name and corresponding label to the text file
            f.write(f'{image_file_name} {label}\n')

# Construct the path to the images
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Use os.path.abspath to handle paths correctly
image_paths = [
    os.path.join(base_dir, 'Assets', 'Chiffres_1.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_2.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_3.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_4.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_5.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_6.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_7.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_8.jpg'),
    os.path.join(base_dir, 'Assets', 'Chiffres_9.jpg')
]

labels_per_image = [
    ["un", "un", "un", "un", "deux", "deux", "deux", "deux", "trois", "trois", "trois", "trois", "quatre", "quatre", "quatre", "quatre"],
    ["cinq", "cinq", "cinq", "cinq", "six", "six", "six", "six", "sept", "sept", "sept", "sept", "huit", "huit", "huit", "huit"],
    ["neuf", "neuf", "neuf", "neuf", "dix", "dix", "dix", "dix", "onze", "onze", "onze", "onze", "douze", "douze", "douze", "douze"],
    ["treize", "treize", "treize", "treize", "quatorze", "quatorze", "quatorze", "quatorze", "quize", "quize", "quize", "quize", "seize", "seize", "seize", "seize"],
    ["vingt", "vingt", "vingt", "vingt", "trente", "trente", "trente", "trente", "quarante", "quarante", "quarante", "quarante", "cinquante", "cinquante", "cinquante", "cinquante"],
    ["soixante", "soixante", "soixante", "soixante", "cent", "cent", "cent", "cent", "cents", "cents", "cents", "cents", "mille", "mille", "mille", "mille"],
    ["milles", "milles", "milles", "milles", "million", "million", "million", "million", "millions", "millions", "millions", "millions", "milliard", "milliard", "milliard", "milliard"],
    ["milliards", "milliards", "milliards", "milliards", "et", "et", "et", "et", "-", "-", "-", "-", "virgule", "virgule", "virgule", "virgule"],
    ["dirhams", "dirhams", "dirhams", "dirhams", "MAD", "MAD", "MAD", "MAD", "", "", "", "", "", "", "", ""]
]


target_dir = os.path.join(base_dir, 'ProcessedImages')
text_file_path = os.path.join(base_dir, 'chiffres.txt')


# Process each image
#Pour que le process de l'image se fait correctement l image doit etre:
# 970 pixels de largeur 
# 1280 pixels de longueur.

for i in range(len(image_paths)):
    process_image(image_paths[i], target_dir, text_file_path, labels_per_image[i])
