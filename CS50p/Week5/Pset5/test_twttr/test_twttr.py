from twttr import shorten

def main():
    test_vowels()
    test_consonants()
    test_numbers()
    test_string()


def test_vowels():
    assert shorten("A, E, I, O, U") == ", , , , "
    assert shorten("a, e, i, o, u") == ", , , , "

def test_consonants():
    assert shorten("B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z") == "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z"
    assert shorten("b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z") == "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"

def test_numbers():
    assert shorten("1, 2, 3, 4, 5, 6, 7, 8, 9") == "1, 2, 3, 4, 5, 6, 7, 8, 9"

def test_string():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"


if __name__ == "__main__":
    main()

# test version without pytest

# def test_vowels():
#      try:
#         assert shorten("A, E, I, O, U") == ", , , , "
#         print("good job 1")
#     except AssertionError:
#              print("bab job 1")
#     try:
#         assert shorten("a, e, i, o, u") == ", , , , "
#         print("good job 2")
#     except AssertionError:
#              print("bab job 2")

# def test_consonants():
#     try:
#         assert shorten("B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z") == "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z"
#         print("good job 3")
#     except AssertionError:
#              print("bab job 3")
#     try:
#         assert shorten("b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z") == "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"
#         print("good job 4")
#     except AssertionError:
#              print("bab job 4")

# def test_numbers():
#     try:
#         assert shorten("1, 2, 3, 4, 5, 6, 7, 8, 9") == "1, 2, 3, 4, 5, 6, 7, 8, 9"
#         print("good job 5")
#     except AssertionError:
#              print("bab job 5")

# def test_string():
#     try:
#         assert shorten("Twitter") == "Twttr"
#         print("good job 6")
#     except AssertionError:
#              print("bab job 6")
#     try:
#         assert shorten("What's your name?") == "Wht's yr nm?"
#         print("good job 7")
#     except AssertionError:
#              print("bab job 7")
#     try:
#         assert shorten("CS50") == "CS50"
#         print("good job 8")
#     except AssertionError:
#              print("bab job 8")
#     try:
#         assert shorten("PYTHON") == "PYTHN"
#         print("good job 9")
#     except AssertionError:
#              print("bab job 9")

# if __name__ == "__main__":
#     main()
