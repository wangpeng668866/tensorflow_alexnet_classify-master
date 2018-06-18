import tensorflow as tf
image_path = 'dog.png'
filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once(image_path))
image_reader = tf.WholeFileReader()
_,image_file = image_reader.read(filename_queue)
image = tf.image.decode_png(image_file)  # 如果是png格式的图片，使用tf.image.decode_png()
sess.run(image)