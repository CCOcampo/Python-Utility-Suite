def get_total(costs, items, tax):
    total = sum(costs[item] for item in items if item in costs)
    total_with_tax = total + (total * tax)
    return round(total_with_tax, 2)

def nth_letter_word(words):
    result = ""
    for i, word in enumerate(words):
        if i < len(word):
            result += word[i]
    return result