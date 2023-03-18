import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # rows will store the values of each line initally 
    # evidence will store all the values except the label
    # label will store only the label value
    rows = []
    evidence = []
    labels = []

    # open the shopping.csv file in reading mode
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)

        # store each row values in the rows list
        for row in csvreader:
            rows.append(row)
        
        # converting all the values into numeric values
        for i in range(0,len(rows)):
            for j in range(0,len(rows[i])):
                # column 0,2,4,11,12,13,14 needs to be an integer
                if j == 0 or j == 2 or j == 4 or j == 11 or j == 12 or j == 13 or j == 14:
                    rows[i][j] = int(rows[i][j])
                # column 1,3,5,6,7,8,9 needs to be float
                elif j == 1 or j == 3 or j == 5 or j == 6 or j == 7 or j == 8 or j == 9:
                    rows[i][j] = float(rows[i][j])
                # column 10 which have month needs to be changed to numbers
                elif j == 10:
                    cal = ["Jan","Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                    indexval = cal.index(str(rows[i][j]))
                    rows[i][j] = indexval
                # column 15 should be 1 for returning users and 0 for non returning
                elif j == 15:
                    if rows[i][j] == "Returning_Visitor":
                        rows[i][j] = 1
                    else:
                        rows[i][j] = 0
                # column 16 should be 1 is the user visited on the weekend and 0 otherwise
                elif j == 16:
                    if rows[i][j] == "FALSE":
                        rows[i][j] = 0
                    else:
                        rows[i][j] = 1
                # column 17 should be 1 if revenue is true and 0 if false
                else:
                    if rows[i][j] == "FALSE":
                        rows[i][j] = 0
                    else:
                        rows[i][j] = 1
        # append the evidence to the evidence list
        for row in rows:
            evidence.append(row[:-1])
        # append the label to the label list
        for row in rows:
            labels.append(row[-1])
        # return tuple of evidence and label
        return (evidence,labels)

        


    raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # pass the k value to be 1
    model = KNeighborsClassifier(n_neighbors=1)
    # fit the model
    model.fit(evidence,labels)
    # return the model
    return model
    raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # specificity is the true negative rate
    # sensitvity is the true positive rate
    # countpositive will store the total positive values to take the ratio for sensitivity
    # countnegative will store the total negative values to take the ration for specificity  
    specificity,sensitivity,countpositive,countnegative = 0,0,0,0

    for i in range(len(labels)):
        # if both the label value is 1 and prediction is also 1 then increase the sensitivity and countpositive value
        if labels[i] == 1 and predictions[i] == 1:
            sensitivity += 1
            countpositive += 1
        # if the prediction is wrong then just increase the countpositive value
        elif labels[i] == 1 and predictions[i] != 1:
            countpositive += 1
        # if the label value is 0 and prediction is also 0 then increase the specificity and countnegative value
        elif labels[i] == 0 and predictions[i] == 0:
            specificity += 1
            countnegative += 1
        # if the prediction is wrong then just increase the countnegative value
        else:
            countnegative += 1
    # fund the ratio
    sensitivity = sensitivity / countpositive
    specificity = specificity / countnegative

    # return
    return sensitivity,specificity

    raise NotImplementedError


if __name__ == "__main__":
    main()
