mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}

from pathlib import Path
import sys

Mypkg2Folder = Path(__file__).parent.parent / 'mypkg2'
sys.path.append(str(Mypkg2Folder))

from mymodule2_1 import calculate_area_of_circle
from mymodule2_2 import fetch_user_data

if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file using pathlib.Path. Prove it exists.
    DataFolder = Path().parent.parent / 'data'
    paralmpics_raw = DataFolder.joinpath('paralmpics_raw.csv')

    if paralmpics_raw.exists() == True:
        print("Im blooming")
    else:
        print("File not found!")