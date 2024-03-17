import re
from googlesearch import search


def check_author(author):
    # Get the birth and death dates of the author
    birth_date_list = get_author_birth_date(author)
    birth_date = list(birth_date_list.keys())[0]
    death_date_list = get_author_death_date(author)
    death_date = list(death_date_list.keys())[0]

    print(birth_date)
    print(death_date)

    if int(birth_date) >= 1935:
        return False
    elif int(death_date) >= 1955:
        return False

    return True


def get_author_birth_date(author_name):
    query = f"when was {author_name} born?"
    return get_year(query)


def get_author_death_date(author_name):
    query = f"When did {author_name} die?"
    return get_year(query)


def get_year(query):
    year_count = {}
    year_total = []

    for j in search(query, advanced=True):
        # get the description
        description = j.description
        # Find all instances of years in the description
        years = re.findall(r'\b\d{4}\b', description)
        year_total = year_total + years

    # Count the occurrences of each year
    for year in year_total:
        if year in year_count:
            year_count[year] += 1
        else:
            year_count[year] = 1

    # sort years by repetition count in description
    year_count = dict(sorted(year_count.items(), key=lambda item: item[1], reverse=True))
    return year_count


if __name__ == "__main__":
    # Keep the author variable as a list
    authors = ["Mark Twain", "Steve Martin"]
    # Iterate over the list and call the check_author function for each element
    for author in authors:
        print(author)
        result = check_author(author)
        print(result)
        print()
