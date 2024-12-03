import argparse

class Red_Nosed_Reports:
    def __init__(self, file_name, test=False):
        self.file_name = file_name
        self.test = test

    def parse_report(self, num):
        # Check if the list starts off increasing or decreasing
        # Start with assumption that reports is safe and invalidate it by parsing the report
        valid = True
        delta = num[1] - num[0]
        if -4 < delta < 0:
            # Report should be decreasing
            for i in range(1, len(num)-1):
                delta = num[i+1] - num[i]
                if delta >= 0 or delta < -3:
                    #print("DEC", num, delta)
                    # Values no longer gradually decreasing
                    valid = False
        elif 0 < delta < 4:
            # Report should be increasing
            for i in range(1, len(num)-1):
                delta = num[i+1] - num[i]
                if delta <= 0 or delta > 3:
                    # Values no longer gradually increasing
                    #print("INC", num, delta)
                    valid = False
        else:
            # Invalid as first two values are neither increasing nor decreasing
            #print("SAME", num)
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
    o = Red_Nosed_Reports(file_name='./input/02-input.txt')
    count = o.parse()

    print(f"\nThe total number of safe reports is {count}.\n")