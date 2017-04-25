import tensorflow as tf
import csv

feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2)]

classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10],
                                            n_classes=2,
                                            model_dir='./tmp_model')

def get_train_inputs():
    x_train, y_train = [], []
    with open('data/data_big_nonsep_train.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            x_train.append([float(row[0]), float(row[1])])
            y_train.append([float(row[2])])
    return tf.constant(x_train), tf.constant(y_train)

classifier.fit(input_fn=get_train_inputs, steps=100000)

def get_test_inputs():
    x_test, y_test= [], []
    with open('data/data_big_nonsep_test.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            x_test.append([float(row[0]), float(row[1])])
            y_test.append([float(row[2])])
    return tf.constant(x_test), tf.constant(y_test)

accuracy_score = classifier.evaluate(input_fn=get_test_inputs, steps=1)["accuracy"]
print(accuracy_score)
