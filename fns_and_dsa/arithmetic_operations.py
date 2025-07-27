def perform_operation(num1, num2, operation):    
    match operation:
        case "subtract":
            result = num1 - num2
            return result
        case "multiply":
            result = num1 * num2
            return result
        case "divide":
            if num2 == 0:
                print("Error: Cannot divide by zero")
            elif num2 != 0:
                return num1 / num2
            else: 
                return "division not possible."

            return result
        case "add":
            result = num1 + num2
            return result
        case _: 
            print("invalid operation selected.")
    