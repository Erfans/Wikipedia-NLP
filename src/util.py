def sort_tokens_list(input_list):
    return sorted(sorted(input_list, key=lambda x: x[0]), key=lambda x: int(x[1]), reverse=True)


def sort_tokens_dict(input_dict):
    return dict(sort_tokens_list(input_dict.items()))