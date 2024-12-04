import argparse

class Red_Nosed_Reports:
    def __init__(self, file_name, test=False, dampener=False):
        self.file_name = file_name
        self.test = test
        self.dampener = dampener

    def parse_report(self, num):
        valid = True

        # Calculate distances between values
        delta = []
        for i in range(1, len(num)):
            delta += [num[i]-num[i-1]]
        
        # Now check that the report uniformly goes either up or down
        all_positive = all(i > 0 for i in delta)
        all_negative = all(i < 0 for i in delta)
        all_same     = all(i == num[0] for i in num) if num else True
        abs_delta    = [abs(i) for i in delta]
        
        if all_same:
            valid = False
            print("Same", num)
        elif all_positive or all_negative:
            if max(abs_delta) > 3:
                valid = False
        else:
            valid = False

        return valid


    def parse(self):
        safe_count = 0

        with open(self.file_name, 'r') as file:
            line = file.readline()
            while line:
                # Convert the report into a list of values
                if self.test == False:
                    num = list(map(int, line.split()))  # Convert each part to an integer
                else:
                    # Convert all elements except the last to integers
                    num = list(map(int, line.split()[:-1]))
                    # Convert the last element to a boolean
                    boolean = line.split()[-1].lower() in ['True', 'true']
                
                valid = self.parse_report(num)

                if valid == False:
                    if self.dampener:
                        # Lazy way: brute forcing removing individual elements to see if the report becomes valid
                        for i in range(len(num)):
                            num_new = num[:i]+num[i+1:]
                            valid = self.parse_report(num_new)
                            if valid == True:
                                break

                if self.test == False:
                    # We passed all the checks so this report is safe
                    if valid == True:
                        #print(num, "Safe")
                        safe_count += 1
                    else:
                        pass
                        #print(num, "NOT SAFE")
                else:
                    if valid != boolean:
                        print('Test failed on', line)

                line = file.readline()

        return safe_count


# Initialize the argument parser
parser = argparse.ArgumentParser(description="Red Nosed Reports Parser")

# Add the -t option
parser.add_argument(
    "-t",
    action="store_true",  # This makes it a flag (True if present, False otherwise)
    help="Test the script"
)

# Parse the arguments
args = parser.parse_args()

# Check if -t (test mode) is enabled
if args.t:
    o = Red_Nosed_Reports(file_name='./input/02-testdata.txt', test=True)
    o.parse()
else:
    # Execute the scripts on the actual data
    o = Red_Nosed_Reports(file_name='./input/02-input.txt', dampener=False)
    count = o.parse()

    print(f"\nThe total number of safe reports is {count}.\n")

    o = Red_Nosed_Reports(file_name='./input/02-input.txt', dampener=True)
    count = o.parse()

    print(f"The total number of safe reports with the dampener active is {count}.\n")