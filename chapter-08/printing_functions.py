def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止。打印每个设计后，将其移到列表 completed_models 中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing design: {current_design}")
        completed_models.append(current_design)
    return completed_models
    

def show_completed_models(completed_models):
    print("\nThe following model have been printed.")
    for model in completed_models:
        print(f"-n {model}")