# def sum_it(a, b):
#     answer = a + b
#     return answer

# def prod_it():
#     final = sum_it(20,3) * 2
#     return final

# def intg_div(num):
#     result = prod_it()//num
#     return result

# print(f"Product of sum = {intg_div(7)}")

import platform

def get_os_details():
    system_info = f"System: {platform.system()} {platform.version()}\n"
    machine_info = f"Machine: {platform.machine()}\n"
    processor_info = f"Processor: {platform.processor()}\n"
    architecture = f"Architecture: {platform.architecture()}\n"
    node = f"Node: {platform.node()}\n"
    details = f"{system_info}, {machine_info}, {processor_info}, {architecture}, {node}"
    return details

print(get_os_details())