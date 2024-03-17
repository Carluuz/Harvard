import json
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# lines
# import re

# Define the font and color for the text
quote_font = ImageFont.truetype("fonts/ComicSansMS3.ttf", 50)
author_font = ImageFont.truetype("fonts/ComicSansMS3.ttf", 35)
color = (255, 255, 255)

# Quotes and quotes_count
quotes_path = 'json/quotes.json'
quote_count_path = 'data/quote_count.txt'

# Images
first = "templates/first.png"
last = "templates/last.png"


def make_pic():
    quotes, quote_count = get_quote_and_quote_count()

    # Alternate images
    for quote, author in quotes.items():
        # Alternate between first.png and last.png
        if quote_count % 2 == 0:
            img_path = first
        else:
            img_path = last

        # open image
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)

        # Split the text into lines, and draw it into image
        lines = get_lines(quote)
        draw_quotes(lines, draw, img)

        # draw authors
        if img_path == first:
            draw.text((850, 985), author, fill=color, font=author_font, anchor='rm')
        elif img_path == last:
            draw.text((220, 985), author, fill=color, font=author_font, anchor='lm')

        # Check if the directory exists, if not, create it
        if not os.path.exists('images'):
            os.makedirs('images')


        # quote = quote[1:-1]
        # Remove quotes and replace ':' with '-'
        quote = quote[1:-1].replace(':', ';')
        
        # save image
        if img_path == first:
            img.save(f"images/{quote_count}  {quote[:100]}.png")
        elif img_path == last:
            img.save(f"images/{quote_count}  {quote[:100]}.png")

        # Increment quote_count
        quote_count += 1

    # Write the new count back to the file
    with open(quote_count_path, 'w') as file:
        file.write(str(quote_count))


def get_quote_and_quote_count():
    # Open quotes.json as quotes
    with open(quotes_path, 'r') as file:
        quotes = json.load(file)

    # Try to read the current count
    try:
        with open(quote_count_path, 'r') as file:
            quote_count = int(file.read().strip())
    except FileNotFoundError:
        # If the file doesn't exist, start the count at   0
        quote_count = 1

    return quotes, quote_count


def split_line_into_parts(line, num_parts):
    # Calculate roughly the length of each part
    part_length = len(line) // num_parts
    parts = []
    start_index = 0

    for _ in range(num_parts - 1):  # We need one less split than the number of parts
        # Find the closest space to the desired part length
        split_index = start_index + part_length
        while split_index < len(line) and line[split_index] not in (' ', '\t', '\n'):
            split_index += 1

        # If we reached the end of the string, break
        if split_index == len(line):
            break

        # Add the part to the list and update the start index for the next part
        parts.append(line[start_index:split_index])
        start_index = split_index + 1  # Skip the whitespace

    # Add the last part, which may be longer than the others
    parts.append(line[start_index:])

    return parts


def get_lines(quote):
    quote = quote.replace(',', ',%%')
    quote = quote.replace('.', '.%%')
    quote = quote.replace(';', ';%%')
    quote = quote.replace(':', ':%%')
    lines = quote.split('%% ')

    # Remove every '%%' from each element in lines
    lines = [line.replace('%%', '') for line in lines]

    # Assuming lines is your list of strings
    merged_lines = []
    i =  0

    while i < len(lines):
        current_line = lines[i]
        words = current_line.split(' ')

        if len(words) > 3:  # More than 3 words, just add it
            merged_lines.append(current_line)
            i +=  1
        else:
            # If the current line has 3 or fewer words, merge it with the next line
            if len(words) <= 3 and i + 1 < len(lines):
                if len(lines[i+1]) and len(current_line) + len(lines[i+1]) <= 38:
                    next_line = lines[i + 1]
                    merged_line = current_line + " " + next_line
                    merged_lines.append(merged_line)
                    i += 2  # Skip the next line since it's already merged
                else:
                    merged_lines.append(current_line)
                    i += 1
            else:
                # If there's no next line, just add the current line
                merged_lines.append(current_line)
                i += 1

    wrapped_lines = []
    for line in merged_lines:
        if len(line) <= 35:
            wrapped_lines.append(line)
        elif len(line) <= 70:
            # Split the line into 2 parts
            parts = split_line_into_parts(line, 2)
            wrapped_lines.extend(parts)
        elif len(line) <= 105:
            # Split the line into 3 parts
            parts = split_line_into_parts(line, 3)
            wrapped_lines.extend(parts)
        elif len(line) <= 140:
            # Split the line into 4 parts
            parts = split_line_into_parts(line, 4)
            wrapped_lines.extend(parts)
        elif len(line) <= 175:
            # Split the line into 3 parts
            parts = split_line_into_parts(line, 5)
            wrapped_lines.extend(parts)
        elif len(line) <= 210:
            # Split the line into 4 parts
            parts = split_line_into_parts(line, 6)
            wrapped_lines.extend(parts)
    return wrapped_lines

    # wrapped_lines = []
    # for line in merged_lines:
    #     wrapped_line = textwrap.wrap(line, width=38)
    #     wrapped_lines.extend(wrapped_line)
    # return wrapped_lines


def draw_quotes(lines, draw, img):
    # Get the image size
    img_w, img_h = img.size

    # Total size from the quote - all lines divided and sizes combined
    total_width = 0
    total_height = 0

    # Calculate the total width and height of the text
    for line in lines:
        # Width
        width = draw.textlength(line, font=quote_font)
        # Heigth
        ascent, descent = quote_font.getmetrics()
        text_height = ascent + descent
        # Total size
        total_width = max(total_width, width)
        total_height += text_height

    # x and y for the center of the image
    x = img_w / 2
    y = (img_h / 2) - (total_height / 2)

    # Draw each line of text
    for i, line in enumerate(lines):
        # anchor is the align prop
        draw.text((x, y + i * text_height), line, fill=color, font=quote_font, anchor='mm')


'''



    Lexical Unit Analysis Segmentation Function

def lexical_unit_analysis_segmentation(text, max_words=8):
    token_pattern = r'\\b\\w+\\b'
    tokens = re.findall(token_pattern, text)
    lines = []
    line = []
    for token in tokens:
        if len(line) < max_words:
            line.append(token)
        else:
            lines.append(' '.join(line))
            line = [token]
    if line:
        lines.append(' '.join(line))
    return lines



    Link Grammar Segmentation Function

def link_grammar_segmentation(text):
    sentence_tokenizer = SimpleSentenceTokenizer()
    sentences = sentence_tokenizer.tokenizer(text)
    lines = []
    for sentence in sentences:
        words = sentence.split()
        line = []
        for word in words:
            if len(line) < max_words:
                line.append(word)
            else:
                lines.append(' '.join(line))
                line = [word]
        if line:
            lines.append(' '.join(line))
    return lines

'''


if __name__ == "__main__":
    make_pic()