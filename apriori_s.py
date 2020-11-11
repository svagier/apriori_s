def add_len_of_sequence_to_dataset(dataset: []) -> []:
    """To optimize performance and avoid checking of length of sequence every iteration, calculate the length once and
    save it in the dataset (as element with index 2 in the tuple)"""
    dataset_with_lengths = []
    for sequence_tuple in dataset:
        length_of_sequence = len(sequence_tuple[1])
        dataset_with_lengths.append(sequence_tuple + (length_of_sequence,))
    return dataset_with_lengths


def print_line_by_line(list_to_be_printed: []):
    if len(list_to_be_printed):
        for line in list_to_be_printed:
            print(line)
    else:
        print("Empty")


def apriori_s(dataset: [], min_sup: float):
    print("Original dataset:")
    print_line_by_line(dataset)

    dataset_with_lengths = add_len_of_sequence_to_dataset(dataset)
    print("\nDataset with added lengths of sequences (index number 2 in the tuple):")
    print_line_by_line(dataset_with_lengths)


def main():
    dataset = [
                ('1', ['p1', 'p2', 'p5']),
                ('2', ['p2', 'p1', 'p4']),
                ('3', ['p1', 'p2', 'p3']),
                ('4', ['p2', 'p3', 'p1']),
                ('5', ['p2', 'p1', 'p3', 'p4']),
                ('6', ['p3', 'p1', 'p2', 'p5']),
                ('7', ['p2', 'p1', 'p2', 'p3']),
                ('8', ['p3', 'p1', 'p3']),
                ('9', ['p2', 'p3', 'p2', 'p1']),
                ('10', ['p3', 'p1', 'p2', 'p4']),
                ('11', ['p3', 'p1', 'p2', 'p1', 'p3']),
                ('12', ['p3', 'p1', 'p2', 'p4', 'p5']),
                ('13', ['p1', 'p2', 'p1', 'p2', 'p5']),
                ('14', ['p3', 'p1', 'p4', 'p1']),
                ('15', ['p2', 'p1', 'p3', 'p4'])
    ]
    min_sup = 2
    apriori_s(dataset, min_sup)


if __name__ == '__main__':
    main()
