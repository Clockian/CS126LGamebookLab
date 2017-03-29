# Made by Jasque Saydyk and 
# Lab 08 - Game Show
# Section 2, Mar. 27, 2017
# Description - Creates a Grade Calculator that reads from a text
# file and outputs to an HTML file

def read_grade_data(filehandle):
    """
    Reads data from any given source and converts it to a data structure that
    the rest of the program will use
    :param filehandle - An open file handle ready for reading
    :return Data structure of your design, containing all of the information
    in the file
    """
    next = filehandle.readline()
    dataStructure = {}
    while next != "":
        print(next)
        next = filehandle.readline()
        s = next.replace('%', ' ')
        s = s.replace(',', ' ')
        s = s.replace('/', ' ')
        s = s.split()
        name = s[0]
        del s[0]
        dataStructure[name] = s
    return dataStructure


def write_grade_report(filehandle, data):
    """
    Uses given grade data to build a report
    :param filehandle - An open file handle ready for writing
    :param data - Your structure holding all grade data
    :return None
    """
    for key in data:
        data_list = data[key]
        weight = data_list[0]
        del data_list[0]

        # Generate Score and max lists
        score_list = []
        max_list = []
        toggle = False
        for x in data_list:
            if toggle is False:
                score_list += x
                toggle = True
            else:
                max_list += x
                toggle = false

        average = percent_per_category(score_list, max_list)
        grade = letter_grade(average)
        overall = weighted_score(average, weight)

        wrapper = """
        <h1>%s Statistics (%d)</h1>
        <ul>
            <li><b>Average:</b>%d</li>
            <li><b>Letter Grade:</b>%d</li>
            <li><b>Overall Grade Contribution:</b>%d</li>
        </ul>
        """

        whole = wrapper % (key, weight, average, grade, overall)

        filehandle.write(whole)
    filehandle.close()
        

def generateHTML(filehandle, weight, average):


def percentage_per_category(score_list, max_list):
    """
    Calculates the percentage of possible points earned in a category.
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should the be same length
        as score_list
    Return:
        returns a floating point number representing the percentage of points
        earned in the given category.
    """
    numerator = sum(score_list)
    denominator = sum(max_list)
    return ((numerator/denominator) * 100)


def letter_grade(percent):
    """
    Return the letter grade of the given percentage.
    Parameters:
        percent - A floating point number from 0 to 1, representing your
        percentage score.
    Returns:
        The string "A", "B", "C", "D", "F" depending on the percentage, at
        the 90%, 80%, 70%, 60% thresholds.
    """
    if percent >= 90:
        return "A"

    elif percent >= 80:
        return "B"

    elif percent >= 70:
        return "C"

    elif percent >= 60:
        return "D"

    else:
        return "F"


def weighted_score(percentage, weight):
    """
    Calculates the weighted contribution of a category to the overall
    course grade.
    Parameters:
        percentage - The percentage of possible points earned in this
        category.
        weight - A number between 0 and 1 representing the weight of
        this category.
    Return:
        returns a floating point number representing the amount the
        given category contributes to the overall grade.
    """
    return (percentage * weight)


def to_percent(score_list, max_list):
    """
    This is a trick I learned when working in Scheme. If you've gotta
    do a recursive function, but don't have enough parameters to make
    it work? Make another function and call it in the original.
    """
    return to_percent_full(score_list, max_list, [])


def to_percent_full(score_list, max_list, percent_list):
    """
    Creates a list that contains percents of score and max list. This
    method was created because the given method signature didn't have
    enough parameters to make the recursion work
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should be the
        same length as score_list.
    Return:
        A new list the same length as the input lists. Each value is
        the score's percentage of the max for that particular index.
    """
    temp1 = score_list.pop(0)
    temp2 = max_list.pop(0)

    temp = int((temp1 / temp2) * 100)
    percent_list.append(temp)

    if len(score_list) == 0:
        return percent_list
    else:
        return to_percent_full(score_list, max_list, percent_list)


def median(score_list, max_list):
    """
    Finds the middlest score of the list. Adds the biggest and
    smallest number, then divides it by two
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should be the
        same length as score_list
    Return:
        The median percentage score of the inputs.
    """
    median_list = to_percent(score_list, max_list)

    median_list.sort()
    min_percent = median_list[0]
    max_percent = median_list[len(median_list) - 1]

    median_percent = int((min_percent + max_percent) / 2)
    return median_percent


# Main of program
#if __name__ == "__main__":
