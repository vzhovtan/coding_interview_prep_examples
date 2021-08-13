"""
This function calulates maximum rectangular area under given histogram with n bars  
Create an empty stack. The stack holds indexes of histogram[] list.  
The bars stored in the stack are always in increasing order of heir heights.
"""

def max_area_histogram(histogram):  
    stack = list() 
    max_area = 0
    index = 0
    while index < len(histogram): 
        # If this bar is higher than the bar on top stack, push it to stack 
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
  
        # If this bar is lower than top of stack,then calculate area of rectangle with  
        # stack top as the smallest (or minimum height) bar.'i' is 'right index' for  
        # the top and element before top in stack is 'left index' 
        else: 
            top_of_stack = stack.pop() 
            # Calculate the area with histogram[top_of_stack] stack as smallest bar 
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
            max_area = max(max_area, area) 
  
    # Now pop the remaining bars from stack and calculate area with every popped bar as the smallest bar 
    while stack: 
        top_of_stack = stack.pop() 
        # Calculate the area with histogram[top_of_stack] stack as smallest bar 
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
        max_area = max(max_area, area) 
  
    return max_area 
  
# driver code 
hist = [6, 2, 5, 4, 5, 1, 6] 
print(f"Maximum area is {max_area_histogram(hist)}") 