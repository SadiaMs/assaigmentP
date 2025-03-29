# Problem Statement  
# In the information flow lesson, we discussed using a variable storing a number as an example of scope.  
# We saw that changes we made to the number inside a function did not stay unless we returned it.  
# This is true for what we call immutable data types which include things like numbers and strings.  

# However, there are also mutable data types where changes stay even if we don't return anything.  
# Some examples of mutable data types are lists and dictionaries.  
# This means that you should be mindful when modifying lists and dictionaries within helper functions  
# since their changes stay whether or not you return them.  

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data  
# and then adds three copies of the data to the list. Don't return anything and see what happens!  
# Compare this process to the x = change(x) example and note the differences.  

# Here is an example run of this program (user input in bold italics):  

# Enter a message to copy: Hello world!  

# List before: []  

# List after: ['Hello world!', 'Hello world!', 'Hello world!']  

# (Note. The concept of immutable/mutable data types is called mutability.  
# Be careful because different programming languages have different rules regarding mutability!)  
from typing import List

def add_three_copies(my_list: List[str], data: str) -> None:
    """
    Adds three copies of 'data' to the provided list.
    
    Args:
        my_list (List[str]): The list to modify.
        data (str): The data to add three times.
    """
    my_list.extend([data] * 3)  # More efficient than using a loop

########## No need to edit code past this point

def main() -> None:
    """
    Main function to take user input and demonstrate mutability of lists.
    """
    message: str = input("Enter a message to copy: ").strip()
    
    my_list: List[str] = []
    
    print("\nBefore adding copies:")
    print(f"List before: {my_list}\n")
    
    add_three_copies(my_list, message)
    
    print("After adding copies:")
    print(f"List after: {my_list}")

if __name__ == "__main__":
    main()
