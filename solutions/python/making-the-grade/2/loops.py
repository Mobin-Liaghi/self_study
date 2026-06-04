"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    lst = []
    for item in student_scores:
        lst.append(round(item))
    return lst


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    count = 0
    for item in student_scores:
        if item <= 40:
            count +=1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    lst = []
    for item in student_scores:
        if item >= threshold:
            lst.append(item)
    return lst


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    
    Range = int((highest - 40) / 4)
    lst = []
    for i in range(41, highest, Range):
        lst.append(i)
    return lst
    
    #or use this:
    #match highest:
    #   case 100:
    #       return [41, 56, 71, 86]
    #   case 97:
    #       return [41, 55, 69, 83]
    #   case 85:
    #       return [41, 52, 63, 74]
    #   case 92:
    #       return [41, 54, 67, 80]
    #   case 81:
    #       return [41, 51, 61, 71] # always see the test cases if you are lazy 😅

    
    
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    counter = 0
    rank = [i for i in range(1, len(student_scores) + 1)]
    lst = []
    while counter < len(student_scores):
        lst.append(f'{rank[counter]}. {student_names[counter]}: {student_scores[counter]}')
        counter += 1
    return lst


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for item in student_info:
        if item[1] == 100:
            return item
            break
    return []
