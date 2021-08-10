"""
Given dictionary representing an hierarchy of employees print the entire hierarchy
The dictionary could be given as result of API request to the company directory
"""

def show(obj, depth=0):
    depth += 1
    for v in obj.values():
        if isinstance(v, dict):
            yield from show(v, depth)
        else:
            yield v, depth

# driver code
employees = {
    'manager-1': {
        'name': 'Manager 1',
        'children': {
            'manager-2': {
                'name': 'Manager 2',
                'children': {
                    'employee-1': {
                        'name': 'Employee 1',
                        'children': {
                            'employee-7': {
                                'name': 'Employee 7',
                            },
                            'employee-8': {
                                'name': 'Employee 8',
                            }
                        }
                    },
                    'employee-2': {
                        'name': 'Employee 2',
                    },
                    'employee-3': {
                        'name': 'Employee 3',
                    },
                },
            },
            'manager-3': {
                'name': 'Manager 3',
                'children': {
                    'employee-4': {
                        'name': 'Employee 4',
                    },
                    'employee-5': {
                        'name': 'Employee 5',
                    },
                    'employee-6': {
                        'name': 'Employee 6',
                    },
                },
            },
            'manager-4': {
                'name': 'Manager 4',
            },
            'manager-5': {
                'name': 'Manager 5',
            }
        }
    }
}

for v, depth in show(employees):
    print('-' * depth + v)