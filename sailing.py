import pickle

from torch.utils.data import Dataset

from tape.datasets import dataset_factory


def read(files, output):
    data = []
    for i, file in enumerate(files):
        dataset = dataset_factory(file)
        if i == 0:
            print(dataset[0].keys())
        data += list(dataset)
    print(len(data))
    pickle.dump(data, open(output, "wb"))


def split(file, key, train_file, val_file, test_file):
    dataset = pickle.load(open(file, "rb"))
    length = len(dataset)
    train_size, val_size = int(length * 0.7), int(length * 0.2)
    pickle.dump(dataset[:train_size], open(train_file, "wb"))
    pickle.dump(dataset[train_size:(train_size + val_size)], open(val_file, "wb"))
    pickle.dump(dataset[(train_size + val_size):], open(test_file, "wb"))


if __name__ == '__main__':
    read([
        "data/secondary_structure/secondary_structure_train.lmdb",
        "data/secondary_structure/secondary_structure_valid.lmdb",
        "data/secondary_structure/secondary_structure_casp12.lmdb",
        "data/secondary_structure/secondary_structure_cb513.lmdb",
        "data/secondary_structure/secondary_structure_ts115.lmdb",
    ], "data/sec_str.pkl")
    split("data/sec_str.pkl", "", "data/sec_str_train.pkl", "data/sec_str_val.pkl", "data/sec_str_test.pkl")
