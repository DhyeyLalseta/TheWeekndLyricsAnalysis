import pickle
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from re import sub

class TextGenerationModel:
    def __init__(self, savedmodel_path: str, tokenizer_path: str):
        self._model: Sequential = load_model(savedmodel_path)
        with open(tokenizer_path, "rb") as tokenizer_pickle:
            self._tokenizer: Tokenizer = pickle.load(tokenizer_pickle)

    def generate_text(
        self, seed_text: str, word_gen_count: int, temperature: float, seq_len=15
    ) -> str:
        """Generate predicted text from an input/seed sample.

        Args:
            seed_text (str)
            word_gen_count (int): Count of words to generate.
            temperature (float): Ambiguity of prediction.
            seq_len (int, optional), Defaults to 15.

        Returns:
            str: Generated text.
        """
        output_text = []
        input_text = seed_text.lower()
        for _ in range(word_gen_count):
            encoded_text = self._tokenizer.texts_to_sequences([input_text])[0]
            pad_encoded = pad_sequences(
                [encoded_text], maxlen=seq_len, truncating="pre"
            )
            prediction_distribution = self._model.predict(pad_encoded, verbose=0)[0]

            predicted_word = self._get_word_prediction(
                prediction_distribution, temperature
            )
            input_text += " " + predicted_word
            output_text.append(predicted_word)
        output_string = " ".join(output_text)
        output_string = self._format_output_string(output_string)
        return output_string

    def _get_word_prediction(
        self, prediction_distribution: np.ndarray, temperature: float
    ) -> str:
        """Determine word prediction from prediction distribution."""

        predictions = np.power(
            prediction_distribution, (1 / temperature)
        )  # apply temperature to preds
        predictions = predictions / predictions.sum()
        choices = range(predictions.size)
        predicted_index = np.random.choice(a=choices, p=predictions)
        predicted_word: str = self._tokenizer.index_word[predicted_index]
        return predicted_word
    
    def _format_output_string(self, output_string: str):
        output_string = sub(r'\s([?.!",](?:\s|$))', r'\1', output_string)
        output_string = sub(r"\b\s+'\b", r"'", output_string)
        output_string = output_string.replace("n't", "not")
        return output_string