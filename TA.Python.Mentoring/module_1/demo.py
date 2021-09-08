import fizz_buzz
import min_max
import text_statistics
import filesize_readable
import multiple_of


def main():
    print("==========task#1")
    fizz_buzz.show_fizz_buzz()

    print("==========task#2")
    testlist = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    min_max.show_min_max(testlist)

    print("==========task#3")
    text_statistics.show_statistics("python",
                                     "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years. Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation!")
    print("==========task#4")
    assert filesize_readable.file_size(19) == '19.0B'
    assert filesize_readable.file_size(12345) == '12.1Kb'
    assert filesize_readable.file_size(1101947) == '1.1Mb'
    assert filesize_readable.file_size(572090) == '558.7Kb'
    assert filesize_readable.file_size(999999999999) == '931.3Gb'
    print("Tests are passed")

    print("==========task#5")
    print(multiple_of.show_sum_multiple_of())


main()
