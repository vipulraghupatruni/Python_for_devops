import pdb
import json

class LogAnalyzer:   # creating class
    """
    Class has 2 things:
    data members (variables) & member functions (functions)
    """
    # Fixed: Indented everything below this line by 4 spaces to place them inside the class
    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file
        
    def read_logs(self):
        lines = []
        with open(self.file_name, "r") as file: 
            lines = file.readlines() 
        return lines
        
    def analyze(self):
        # pdb.set_trace()  # Set a breakpoint for debugging
        
        log_count = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }
        lines = self.read_logs()  # Read the logs using the class method
        
        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"] + 1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"] + 1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"] + 1})
              
        return log_count
        
    def write_json(self, counts):
        with open(self.output_file, "w+") as json_file:
            json.dump(counts, json_file, indent=4) # Added indent=4 for pretty JSON formatting


#modular
# Main Execution (Touching the left wall, outside the class)
log_1 = LogAnalyzer("app.log", "output1.json")  # creating object
log_count = log_1.analyze()                    # Fixed: Changed log1 to log_1
log_1.write_json(log_count)                    # writing json file

print("Analysis complete! Summary saved to output1.json")

#reusable clear #extensible
log_1 = LogAnalyzer("app2.log", "output2.json")  # creating object
log_count = log_1.analyze()                    # Fixed: Changed log1 to log_1
log_1.write_json(log_count)                    # writing json file

print("Analysis complete! Summary saved to output2.json")


# Main Execution (MUST be touching the left wall)
#lines = read_logs()
#counts = analyze(lines)
#print("log counts are: ", counts)
#write_json()
