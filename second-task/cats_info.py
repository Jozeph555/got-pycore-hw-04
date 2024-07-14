"""Get cats info function"""


from pathlib import Path

def get_cats_info(path: Path) -> list[dict]:
    """
    Parses a text file that contains information about the cats and returns the list
    of dictionaries with information about each cat.

    Args:
        param1 (Path): The path to the text file.

    Returns:
        list[dict]: The list of dictionaries with information about each cat.
    
    Raises:
        FileNotFoundError: If file doesn't exist.
    """
    try:

        with open(path, "r", encoding="utf-8") as file:
            cats = file.readlines()
            cat_list = []

            for row in cats:
                cat = {}
                cat_id, name, age = row.split(",")
                cat["id"] = cat_id
                cat["name"] = name
                cat["age"] = age.strip()
                cat_list.append(cat)

            return cat_list

    except FileNotFoundError:
        return "There is no file"
