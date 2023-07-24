# Tierra Ingram
# 4/30/2023
# Comp163, Section 4
# 'Grade Calc' - Program to calculate my grade in Comp163, implementing topics from ZyBooks 10-14

# Importing the Comp163Cat module that contains weights
import Comp163Cat

class Comp163GradeCalculator:
    def __init__(self, categories): # Initializing Class
        self.FILENAME = 'Comp163Grades.txt' # Setting file name to store grades

        self.categories = categories
        cat_instance = Comp163Cat.Comp163Cat()
        self.weights = cat_instance.getWeight()
        self.points = {cat:[] for cat in self.categories}

        try: # try to read grades from the file, if it doesn't exist write grades, if there's an exception it prints the error
            self.readGrades()
        except FileNotFoundError:
            self.writeGrades()
        except Exception:
            print('Unkown Error')
        finally:
            print('Grades have been loaded')
    
    def calculate_grade(self): # Method to Calculate Grade
        total_weight = sum(self.weights.values())
        weighted_points = sum(self.weights[cat] * sum(self.points[cat])/len(self.points[cat]) if len(self.points[cat]) > 0 else 0 for cat in self.categories)
        return weighted_points / total_weight
    
    def set_points(self, cat):
        if cat in self.categories:
            num_points = int(input(f'Enter the number of {cat}: '))
            points = [] # Stores points into a dictionary
            for i in range(num_points):
                point = float(input(f'Enter point {i+1}: '))
                points.append(point)
            self.points[cat] = points
            self.writeGrades()
        else:
            print('Invalid Category')

    def edit_points(self, cat): # Method to Edit Points
        if cat in self.categories:
            if self.points[cat]:
                print(f'The current points for {cat} are: {self.points[cat]}')
                index = int(input(f'Enter the index of the points you want to edit (1- {len(self.points[cat])}): '))
                new_point = float(input('Enter the new point value: '))
                self.points[cat][index-1] = new_point
                self.writeGrades()
            else:
                print(f'There are no points recorded for {cat}. Please you Set Points to add new points')
        else:
            print('Invalid Category')

    
    def display_points(self): # Method to Display Points
        for cat in self.categories:
            if self.points[cat]:
                average = sum(self.points[cat])/len(self.points[cat])
                print(f'{cat} - Average: {average:.2f}')
            else:
                print(f'{cat} - No points recorded')
    
    def readGrades(self): # Method to Read Grades
        self.points = {cat:[] for cat in self.categories}
        try:
            with open(self.FILENAME, 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    item = line.strip().split(',')
                    if item[0] in self.categories:

                        points = [float(x) for x in item[1:]]
                        self.points[item[0]] = points
                    else:
                        print('Invalid category in file:', item[0])
        except FileNotFoundError:
            self.writeGrades()
        except Exception:
            print('Unkown error')
        finally:
            print('Grades have been loaded')
    

    def writeGrades(self): # Method to Write Grades
        fp = open(self.FILENAME, 'w')
        for k,v in self.points.items():
            if v:
                points_str = ','.join(str(x) for x in v)
                fp.write(k+','+str(v)+'\n')
        fp.close()

    def test(self): # Test Method
        print('Starting tests...\n')
    
        # Set predefined points for each category
        self.points['Homework'] = [10.0, 9.5, 8.0]
        self.points['Assignments'] = [8.0, 7.5, 6.5, 9.0]
        self.points['Labs'] = [9.0, 8.5]
        self.points['Assessments'] = [8.0, 9.5]
        self.points['Midterm'] = [85.0]
        self.points['Final'] = [80.0]
    
        # Tests calculate_grade()
        print('Testing calculate_grade()...\n')
        expected_grade = 34.38
        actual_grade = self.calculate_grade()
        print(f'Expected grade: {expected_grade:.2f}%')
        print(f'Actual grade: {actual_grade:.2f}%')
        print('\n')
    
        # Tests display_points()
        print('Testing display_points()...\n')
        self.display_points()
        print('\n')
    
        print('All tests completed- Pass')



if __name__ == '__main__':
    categories = ['Homework', 'Assignments', 'Labs', 'Assessments', 'Midterm', 'Final']
    calculator = Comp163GradeCalculator(categories)

    while True: # Menu Selection
        opt = input('(S)et Points (E)dit Points (C)alculate Grade (D)isplay Points (T)est (Q)uit:').upper()
        if opt == 'S':
            cat = input('Enter category (Homework, Assignments, Labs, Assessments, Midterm, Final): ')
            calculator.set_points(cat)

        elif opt == 'E':
            calculator.display_points()
            cat = input('Enter category (Homework, Assignments, Labs, Assesments, Midterm, Final): ')
            if cat in categories:
                calculator.edit_points(cat)
            else:
                print('Invalid Category. ')
            
        elif opt == 'C':
                grade = calculator.calculate_grade()
                print('Your grade is: {:.2f}%'.format(grade))

        elif opt == 'D':
            calculator.display_points()

        elif opt == 'T':
            calculator.test()

        elif opt == 'Q':
            break

        else:
            print('Invalid Option')





                