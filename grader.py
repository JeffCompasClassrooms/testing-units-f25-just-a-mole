# Program created by Gemini for a software testing assignment.
# This program provides two functions, `analyze_text` and `calculate_grade`,
# which are designed to be tested thoroughly.

import re
from typing import List, Dict, Union

def analyze_text(text: str) -> Dict[str, Union[int, Dict[str, int], bool]]:
    """
    Analyzes a given string and returns a dictionary of its properties.

    This function is designed to handle various edge cases, including different
    data types, empty or whitespace-only strings, and complex text for
    palindrome checking.

    Args:
        text: The input string to analyze.

    Returns:
        A dictionary containing:
        - 'length': The total number of characters in the string.
        - 'word_count': The number of words in the string.
        - 'char_count': A dictionary with the frequency of each character.
        - 'is_palindrome': A boolean indicating if the text is a palindrome
          (case-insensitive, ignoring non-alphanumeric characters).

    Raises:
        TypeError: If the input `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Calculate basic properties
    length = len(text)
    words = text.split()
    word_count = len(words)

    # Count character frequencies
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    # Check for palindrome property
    # 1. Normalize the string: lowercase and remove non-alphanumeric chars
    normalized_text = re.sub(r'[^a-z0-9]', '', text.lower())

    # 2. Check if the normalized string is equal to its reverse
    is_palindrome = False
    if normalized_text:  # An empty string is not considered a palindrome here
        is_palindrome = normalized_text == normalized_text[::-1]

    return {
        'length': length,
        'word_count': word_count,
        'char_count': char_count,
        'is_palindrome': is_palindrome
    }

def calculate_grade(scores: List[Union[int, float]]) -> Dict[str, Union[float, str]]:
    """
    Calculates the average score and corresponding letter grade from a list of scores.

    The function validates the input list to ensure it's not empty and that all
    scores are within a valid range (0-100).

    Args:
        scores: A list of numbers (integers or floats) representing scores.

    Returns:
        A dictionary containing:
        - 'average_score': The calculated average of the scores.
        - 'letter_grade': The corresponding letter grade ('A', 'B', 'C', 'D', 'F').

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the list is empty or scores are outside the 0-100 range.
    """
    if not isinstance(scores, list):
        raise TypeError("Input must be a list of scores.")
    if not scores:
        raise ValueError("Score list cannot be empty.")

    total_score = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All items in the list must be numbers.")
        if not 0 <= score <= 100:
            raise ValueError("Scores must be between 0 and 100.")
        total_score += score

    average = total_score / len(scores)

    letter_grade = ''
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return {
        'average_score': round(average, 2),
        'letter_grade': letter_grade
    }

print(analyze_text("A man, a plan, a canal: Panama"))