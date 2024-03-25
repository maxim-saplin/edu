text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."
tokens = text.encode("utf-8")  # raw bytes
tokens = list(
    map(int, tokens)
)  # convert to a list of integers in range 0..255 for convenience
print("\n---\nOriginal Text:")
print(text)
print("\nLength of Text:", len(text))
print("\n---\nTokenized Text:")
print(tokens)
print("\nLength of Tokenized Text:", len(tokens))


def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):  # Pythonic way to iterate consecutive elements
        counts[pair] = counts.get(pair, 0) + 1
    return counts


stats = get_stats(tokens)
# print("\nStatistics:\n", stats)
# print("\nSorted Statistics:\n", sorted(((v,k) for k,v in stats.items()), reverse=True))

top_pair = max(stats, key=stats.get)
top_pair


def merge(ids, pair, idx):
    # in the list of ints (ids), replace all consecutive occurences of pair with the new token idx
    newids = []
    i = 0
    while i < len(ids):
        # if we are not at the very last position AND the pair matches, replace it
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i + 1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

print("\nResult of Merge Function with Example Input:")
print(merge([5, 6, 6, 7, 9, 1], (6, 7), 99))

tokens2 = merge(tokens, top_pair, 256)
print("\nTokenized Text After Merge:")
print(tokens2)
print("\nLength of Tokenized Text After Merge:", len(tokens2))
