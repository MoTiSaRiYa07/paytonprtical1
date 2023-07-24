def kg_to_gram(kilograms):
    return kilograms * 1000

if __name__ == "__main__":
    try:
        kilograms = float(input("Enter the weight in Kilograms: "))
        grams = kg_to_gram(kilograms)
        print("{} Kilograms is equal to {} Grams".format(kilograms, grams))
    except ValueError:
        print("Invalid input. Please enter a valid number for weight in Kilograms.")
