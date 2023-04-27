

from Square import Square

import tensorflow as tf


if __name__ == '__main__':
    sos = Square()
    tf.saved_model.save(sos, './square/1')




