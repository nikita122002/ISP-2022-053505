
# work with file
def get_file_text(file_name):
    file = open('text.txt', 'r')
    file_text = file.read()
    file.close()
    return file_text


def dict_of_words(text):
    text = text.lower()  # change upper symbols to lower
    punctuation_symbols = list("()-:;\",?!.")

    for elem in punctuation_symbols:
        text = text.replace(elem, "")

    words_list = text.split()  # divides by space

    words_dictionary = dict()  # create dictionary
    for word in words_list:
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1

    return words_dictionary


def average_count(text):
    text = text.lower()
    punctuation = list("()-:;\",")
    end_symbols = list("?!.")

    for symbol in punctuation:
        text = text.replace(symbol, "")

    word_count = len(text.split())

    sentence_count = 0
    for symbol in text:
        if symbol in end_symbols:
            sentence_count += 1

    average_word_count = word_count / sentence_count

    return average_word_count


def median_count(text):
    end_symbols = list("?!.")
    for char in end_symbols:
        text = text.replace(char + " ", ".")

    sentence_list = text.split(".")
    sentence_list.remove("")

    words_count = list()
    sentence_dict = dict()
    for sentence in sentence_list:
        sentence_dict[sentence] = 1
        for char in sentence:
            if char == " ":
                sentence_dict[sentence] += 1
        words_count.append(sentence_dict[sentence])

    words_count.sort()
    pointer = len(words_count) / 2
    if len(words_count) % 2 == 0:
        pointer = int(pointer)
        return (words_count[pointer - 1] + words_count[pointer]) / 2
    else:
        return words_count[int(pointer)]


def top_k_ngrams(text, n, k):
    words_dict = dict_of_words(text)
    sorted_dictionary = dict()
    for word in words_dict:
        if len(word) == n:
            sorted_dictionary[word] = words_dict[word]

    quantities_list = list(sorted_dictionary.values())
    quantities_list.sort()
    quantities_list.reverse()
    top_list = quantities_list[:k]
    top_dict = dict()

    for times in top_list:
        for word in sorted_dictionary:
            if sorted_dictionary[word] == times and word not in top_dict.keys():
                top_dict[word] = times
                break

    return top_dict


def print_dict_of_words(words_dict):
    for word in words_dict:
        print(f"{word}: {words_dict[word]} times")


def main():
    text = get_file_text("text.txt")
    k = 10
    n = 4
    print("Choose:\n1) Show top-10 4-grams\n2) Enter your values of k and n")
    choice = input(">> ")
    if int(choice) == 2:
        k = int(input("k = "))
        n = int(input("n = "))
    print("\nWords dictionary:")
    print_dict_of_words(dict_of_words(text))
    print(f"\nAverage word count: {average_count(text)}")
    print(f"Median word count: {median_count(text)}")
    print(f"\nTop-{k} {n}-grams:")
    print_dict_of_words(top_k_ngrams(text, n, k))


if __name__ == "__main__":
    main()