import re
from statistics import median


def get_file_text(file_name):
    file = open('text.txt', 'r')
    file_text = file.read()
    file.close()
    return file_text


def get_average_word_count(text):
    text = text.lower()
    punctuation_marks = list("()-:;\",")
    end_of_sentence_signs = list("?!.")

    for char in punctuation_marks:
        text = text.replace(char, "")

    word_count = len(text.split())

    sentence_count = 0
    for char in text:
        if char in end_of_sentence_signs:
            sentence_count += 1

    average_word_count = word_count / sentence_count

    return average_word_count


def get_words_dict(text):
    text = text.lower()
    punctuation_marks = list("()-:;\",?!.")

    for char in punctuation_marks:
        text = text.replace(char, "")

    words_list = text.split()

    words_dict = dict()
    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict


def median_count(text):
    result = re.sub('[!?]', '.', text)
    print(median([len(sentence.split()) for sentence in result.split('.')]))


def get_top_ngrams(text, n, k):
    words_dict = get_words_dict(text)
    filtered_dict = dict()
    for word in words_dict:
        if len(word) == n:
            filtered_dict[word] = words_dict[word]

    quantities_list = list(filtered_dict.values())
    quantities_list.sort()
    quantities_list.reverse()
    top_list = quantities_list[:k]
    top_dict = dict()

    for times in top_list:
        for word in filtered_dict:
            if filtered_dict[word] == times and word not in top_dict.keys():
                top_dict[word] = times
                break

    return top_dict


def print_words_dict(words_dict):
    for word in words_dict:
        print(f"{word}: {words_dict[word]} times")


def main():
    text = get_file_text("text.txt")

    if text is None:
        print("File not found or file is empty")
        return
    n = 4
    k = 10
    print("Choose an option:\n1) Show top-10 4-grams\n2) Enter your values")
    choice = input(">> ")
    if int(choice) == 2:
        k = int(input("n = "))
        n = int(input("k = "))

    print(f"\nTop-{k} {n}-grams:")
    print_words_dict(get_top_ngrams(text, n, k))
    print("\nWords dictionary:")
    print_words_dict(get_words_dict(text))
    print(f"\nAverage word count: {get_average_word_count(text)}")
    print("Median word count: ")
    median_count(text)


if __name__ == "__main__":
    main()
