import numpy as np
import lib.constants as const

class Model:
    def __init__(self, 
                 input_size=const.NETWORK_INPUT_SIZE, 
                 hidden_size=const.NETWORK_HIDDEN_SIZE, 
                 output_size=const.NETWORK_OUTPUT_SIZE, 
                 chromosome=None):
        if chromosome is not None:
            self.set_weights(chromosome)
        else:
            # Random initialization of weights and biases.
            self.fc1_weight = np.random.randn(input_size, hidden_size).astype(np.float32)
            self.fc1_bias = np.random.randn(hidden_size).astype(np.float32)
            self.fc2_weight = np.random.randn(hidden_size, output_size).astype(np.float32)
            self.fc2_bias = np.random.randn(output_size).astype(np.float32)

    def forward(self, x):
        """
        Forward pass through the network.
        
        Parameters:
          - x: a NumPy array of shape (batch_size, input_size)
          - species_key: string specifying the species, which determines how the output is sliced.
          
        Returns:
          A NumPy array containing a softmax probability distribution over the allowed actions.
        """
        # First layer: linear transformation followed by ReLU activation.
        h = np.dot(x, self.fc1_weight) + self.fc1_bias
        h = np.maximum(0, h)  # ReLU activation

        # Second layer: linear transformation.
        out = np.dot(h, self.fc2_weight) + self.fc2_bias
        
        # Compute softmax in a numerically stable way.
        exp_vals = np.exp(out - np.max(out, axis=1, keepdims=True))
        softmax_output = exp_vals / np.sum(exp_vals, axis=1, keepdims=True)
        return softmax_output

    def set_weights(self, chromosome):
        """
        Set the model's weights from a provided chromosome dictionary.
        
        The dictionary should have keys:
          - "fc1_weight", "fc1_bias", "fc2_weight", "fc2_bias"
        """
        self.fc1_weight = chromosome["fc1_weight"]
        self.fc1_bias = chromosome["fc1_bias"]
        self.fc2_weight = chromosome["fc2_weight"]
        self.fc2_bias = chromosome["fc2_bias"]

    def state_dict(self):
        """
        Returns the model's parameters as a dictionary.
        """
        return {
            "fc1_weight": self.fc1_weight,
            "fc1_bias": self.fc1_bias,
            "fc2_weight": self.fc2_weight,
            "fc2_bias": self.fc2_bias,
        }

    def save(self, path):
        """
        Save the model's parameters to a file.
        """
        np.savez(path, **self.state_dict())

class SingleSpeciesModel(Model):
    def __init__(self, 
                 input_size=const.NETWORK_INPUT_SIZE, 
                 hidden_size=const.NETWORK_HIDDEN_SIZE, 
                 output_size=const.NETWORK_OUTPUT_SIZE_SINGLE_SPECIES, 
                 chromosome=None):
        super().__init__(input_size, hidden_size, output_size, chromosome)

    # def forward(self, x):
    #     batch_size = x.shape[0]
    #     output_size = self.fc2_bias.shape[0]

    #     # Generate a tensor of zeros
    #     debug_output = np.zeros((batch_size, output_size), dtype=np.float32)
        
    #     debug_output[:, 1] = 1.0

    #     return debug_output

    def forward(self, x):
        h = np.dot(x, self.fc1_weight) + self.fc1_bias
        h = np.maximum(0, h)  # ReLU activation

        # Second layer: linear transformation.
        out = np.dot(h, self.fc2_weight) + self.fc2_bias
        
        # Compute softmax in a numerically stable way.
        exp_vals = np.exp(out - np.max(out, axis=1, keepdims=True))
        softmax_output = exp_vals / np.sum(exp_vals, axis=1, keepdims=True)
        return softmax_output
