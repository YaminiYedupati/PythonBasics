#LogParser.py 

def extract_data(filename):
    with open(filename, "r") as datafile:
        errors = []
        count = 0
        for line in datafile:
            if "ERROR " in line:
                count = count + 1
                line = line.strip()
                # Parse out the error and timestamp
                error = line.split("ERROR")[-1]
                timestamp = line[:19]
                errors.append([timestamp, error])
    return (count,errors)

if __name__ == "__main__":
    count, errs = extract_data("CFCInStoreService.log")
    if count > 0 and errs:
        print("Errors occured in the specified log file - CFCInStoreService.log are", count)
        for err in errs:
            print(f"\t{err[0]} {err[1]}")
    else:
        print("No error events found.")