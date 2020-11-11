def print_line_by_line(list_to_be_printed: []):
    if len(list_to_be_printed):
        for line in list_to_be_printed:
            print(line)
    else:
        print("Empty")
        
        
def add_len_of_sequence_to_dataset(dataset: []) -> ([], int):
    """To optimize performance and avoid checking of length of sequence every iteration, calculate the length once and
    save it in the dataset (as element with index 2 in the tuple).
    Additionally, this function returns the maximum value of sequence length.

    :param dataset: initial dataset
    :return: (dataset_with_lengths, longest_sequence)
    """
    longest_sequence = 0
    dataset_with_lengths = []
    for sequence_tuple in dataset:
        length_of_sequence = len(sequence_tuple[1])
        dataset_with_lengths.append(sequence_tuple + (length_of_sequence,))
        if length_of_sequence > longest_sequence:
            longest_sequence = length_of_sequence
    return dataset_with_lengths, longest_sequence


def get_frequent_elements(dataset: [], min_support: float, iteration: int) -> []:
    """Return list of elements, which in given iteration (under given list index in all sequences) occurred at least
    min_support times in the whole dataset (all sequences).

    :param dataset: dataset with sequence lengths
    :param min_support: minimum support
    :param iteration: stats from 0. Specifies which index from sequence list (sequence_tuple[1]) should be considered
    :return: list of frequent elements
    """
    elements_with_occurrences = {}
    for sequence_tuple in dataset:
        if sequence_tuple[2] >= iteration:
            element = sequence_tuple[1][iteration - 1]
            if element in elements_with_occurrences.keys():
                elements_with_occurrences[element] += 1
            else:
                elements_with_occurrences[element] = 1
    frequent_elements = []
    for element, occurrences in elements_with_occurrences.items():
        if occurrences >= min_support:
            frequent_elements.append(element)
    return frequent_elements


def get_candidate_sequences(current_frequent_elements: [], previous_frequent_sequences: []) -> []:
    if previous_frequent_sequences:
        candidate_sequences = []
        for seq in previous_frequent_sequences:
            print(type(seq))
            for frequent_elem in current_frequent_elements:
                if seq[-1] != frequent_elem:
                    candidate_sequences.append(seq + [frequent_elem])
        return candidate_sequences
    else:
        return [[element] for element in current_frequent_elements]


def get_candidate_sequences_with_support(dataset: [], candidate_sequences_without_sup: []) -> []:
    candidate_sequences_with_support = []
    for candidate_seq in candidate_sequences_without_sup:
        occurrences = 0
        for seq_tuple in dataset:
            iter = 0
            for element in candidate_seq:
                if element == seq_tuple[1][iter]:
                    iter += 1
                else:
                    break
            if iter == len(candidate_seq):
                occurrences += 1
        candidate_sequences_with_support.append((candidate_seq, occurrences))
    return candidate_sequences_with_support


def apriori_s(dataset: [], min_support: float):
    print("Original dataset:")
    print_line_by_line(dataset)

    dataset_with_lengths, maximum_sequence_length = add_len_of_sequence_to_dataset(dataset)
    print("\nDataset with added lengths of sequences (index number 2 in the tuple):")
    print_line_by_line(dataset_with_lengths)

    previous_frequent_sequences = None
    for i in range(1, maximum_sequence_length + 1):
        frequent_elements = get_frequent_elements(dataset_with_lengths, min_support, i)
        print("Frequent elements in iteration {}: {}".format(i, frequent_elements))
        cs_without_support = get_candidate_sequences(frequent_elements, previous_frequent_sequences)
        # print("Candidate sequences without support in iteration {}:".format(i))
        # print_line_by_line(cs_without_support)
        cs_with_support = get_candidate_sequences_with_support(dataset, cs_without_support)
        print("Candidate sequences with support in iteration {}:".format(i))
        print_line_by_line(cs_with_support)


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
    min_support = 2
    apriori_s(dataset, min_support)


if __name__ == '__main__':
    main()
