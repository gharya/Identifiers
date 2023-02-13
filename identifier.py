

def categorize_identifier(identifier):
    identifier_length = len(identifier)
    
    if identifier_length >= 5 and identifier_length <= 8:
        return "TAG"
    elif identifier_length == 17:
        return "VIN"
    elif identifier_length == 10:
        return "BOAT"
    else:
        return "INVALID"

def get_spelling(alphabet_dict, identifier):
    return " ".join(alphabet_dict.get(item) for item in identifier)

def get_dictionary(alphabet_file):
    alphabet_dict = {}
    with open(alphabet_file, "r") as f:
        for line in f:
            line_ = line.rstrip("\n").split()
            alphabet_dict[line_[0]] = line_[1]
    alphabet_dict[" "] = "Space"
    alphabet_dict["-"] = "Dash"
    return alphabet_dict

def main():
    alphabet_file = "alphabet.txt"
    identifiers_file = "identifiers.txt"
    total_identifiers = 0
    valid_identifiers = 0
    invalid_identifiers = 0
    alphabet_dict = get_dictionary(alphabet_file)
    with open(identifiers_file, "r") as f:
        for line in f:
            total_identifiers += 1
            identifier = line.strip("\n").upper()
            category = categorize_identifier(identifier)
            if category == "INVALID":
                invalid_identifiers += 1
                print(f"{category}: {identifier}")
            else:
                valid_identifiers += 1
                spelling = get_spelling(alphabet_dict, identifier)
                print(f"{category}: {identifier}")
                print(spelling)
            print()

    print(f"Number of identifiers processed: {total_identifiers}")
    print(f"Number of invalid identifiers: {invalid_identifiers}")
    print(f"Number of valid identifiers: {valid_identifiers}")


if __name__ == "__main__":
    main()