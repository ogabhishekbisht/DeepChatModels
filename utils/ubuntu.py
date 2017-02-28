from utils.dataset import Dataset
from utils.data_utils import *
from tensorflow import gfile

class Ubuntu(Dataset):

    def __init__(self, vocab_size):

        self.name = "ubuntu"
        self.vocab_size = vocab_size
        self._data_dir = '/home/brandon/terabyte/Datasets/ubuntu_dialogue_corpus'

        paths_triplet = prepare_data(self._data_dir,
                                     self._data_dir + "/train_from.txt",
                                     self._data_dir + "/train_to.txt",
                                     self._data_dir + "/valid_from.txt",
                                     self._data_dir + "/valid_to.txt",
                                     vocab_size, vocab_size)

        train_path, valid_path, vocab_path = paths_triplet

        self.paths = {}
        self.paths['from_train']    = train_path[0]
        self.paths['to_train']      = train_path[1]
        self.paths['from_valid']    = valid_path[0]
        self.paths['to_valid']      = valid_path[1]
        self.paths['from_vocab']    = vocab_path[0]
        self.paths['to_vocab']      = vocab_path[1]


    # ===================================================================
    # Required 'Dataset' method implementations.
    # ===================================================================

    def word_to_idx(self):
        raise NotImplemented

    def idx_to_word(self):
        raise NotImplemented

    @property
    def data_dir(self):
        return self._data_dir

    # ===================================================================
    # Additional methods.
    # ===================================================================


    def open_train_file(self, from_or_to):
        if from_or_to == "from":
            return gfile.GFile(self.from_train, mode="r")
        else:
            return gfile.GFile(self.to_train, mode="r")

