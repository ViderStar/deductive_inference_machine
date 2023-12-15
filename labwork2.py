import numpy as np
import random
import numpy as np


def generate_dataset(num_objects, num_features, num_classes):
    # Инициализация
    object_representations = np.zeros((num_objects, num_features))
    class_membership_matrix = np.zeros((num_objects, num_classes))
    true_class = np.zeros(num_objects)

    for i in range(num_objects):
        # Генерация случайного класса для объекта
        class_idx = np.random.randint(num_classes)
        true_class[i] = class_idx
        class_membership_matrix[i, class_idx] = 1

        # Генерация признаков объекта вокруг центра класса
        class_center = np.random.uniform(-10, 10, num_features)  # центр класса
        object_representations[i] = class_center + np.random.normal(0, 1, num_features)  # объект вокруг центра класса

    return object_representations, class_membership_matrix, true_class


class RecognitionAlgorithArbitrary:
    def __init__(self, desired_quality, object_representations, class_membership_matrix, true_class,num_objects):
        self.num_objects = num_objects
        self.object_representations = object_representations
        self.num_classes = 3
        self.num_parametric_objects = 100
        self.class_membership_matrix = class_membership_matrix
        self.true_class = true_class
        self.desired_quality = desired_quality
        self.optimization_flag = False
        self.proximity_matrix = np.zeros((self.num_objects, self.num_parametric_objects))

    def proximity_function(self, i, j):
        return np.sqrt(np.sum((self.object_representations[i] - self.object_representations[j]) ** 2))

    def class_proximity_function(self, i, j):
        return np.mean(
            [self.proximity_matrix[i, k] for k in range(self.num_objects) if self.class_membership_matrix[k, j] == 1])

    def decision_rule(self, i):
        return np.argmin([self.class_proximity_function(i, j) for j in range(self.num_classes)])

    def compute_pairwise_proximity(self):
        for i in range(self.num_objects):
            for j in range(self.num_parametric_objects):
                self.proximity_matrix[i, j] = self.proximity_function(i, j)

    def compute_proximity_to_classes_and_optimize(self):
        while not self.optimization_flag:
            class_proximity_matrix = np.zeros((self.num_objects, self.num_classes))
            for i in range(self.num_objects):
                for j in range(self.num_classes):
                    class_proximity_matrix[i, j] = self.class_proximity_function(i, j)
            old_quality = self.compute_quality()
            self.proximity_matrix = self.optimize()
            new_quality = self.compute_quality()
            if new_quality > self.desired_quality:
                self.optimization_flag = True
            else:
                self.optimization_flag = False

    def compute_quality(self):
        correct = sum([self.decision_rule(i) == self.true_class[i] for i in range(self.num_objects)])
        return correct / self.num_objects

    def optimize(self):
        optimized_proximity_matrix = np.zeros((self.num_objects, self.num_parametric_objects))
        for i in range(self.num_objects):
            for j in range(self.num_classes):
                optimized_proximity_matrix[i, j] = self.proximity_matrix[i, j] + random.gauss(0, 1)
        return optimized_proximity_matrix

    def recognition_mode(self):
        for i in range(self.num_objects):
            decision = self.decision_rule(i)
            print(f"Object #{i + 1} (true class {self.true_class[i]}):\n{decision}")


if __name__ == "__main__":
    num_objects = 100
    num_features = 3
    num_classes = 3
    object_representations, class_membership_matrix, true_class = generate_dataset(num_objects, num_features, num_classes)

    solution = RecognitionAlgorithArbitrary(0.6, object_representations, class_membership_matrix, true_class, num_objects)
    solution.compute_pairwise_proximity()
    solution.compute_proximity_to_classes_and_optimize()
    solution.recognition_mode()
    quality = solution.compute_quality()
    print(f"Solution quality:\n{quality}")
