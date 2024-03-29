
import tensorflow as tf

class Square(tf.Module):

    @tf.function(
        input_signature=[
            tf.TensorSpec(shape=None, dtype=tf.float32)
        ]
    )
    def compute_square(self, number):
        return number ** 2