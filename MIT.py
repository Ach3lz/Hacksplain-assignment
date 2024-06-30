def group_names(names):
    # Create 6 empty lists to hold the groups
    groups = [[] for _ in range(6)]
    
    # Iterate over the names and distribute them into the groups
    for i, name in enumerate(names):
        groups[i % 6].append(name)
    
    return groups

def main():
    # Accept input from the user
    names = input("Enter a list of names separated by commas: ").split(',')
    
    # Strip any extra whitespace from the names
    names = [name.strip() for name in names]
    
    # Group the names
    grouped_names = group_names(names)
    
    # Display the grouped names
    for i, group in enumerate(grouped_names, start=1):
        print(f"{i}. {group}")

if __name__ == "__main__":
    main()
