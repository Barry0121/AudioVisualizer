## Music Generation with LSTM

Using `.midi` files, we have a more abstract description of how the music is being generated through their composition, instead of wavelets and frequencies.

Approaches:
1. DeepMind's WaveNet generative model. --> Computationally expensive.
2. Perform a 1-D convolutional operation on a fixed number of filters against the input vector. --> Faster in speed, but networks are more complex to construct.
3. LSTM model --> Generate output at each timestamp

Tools:
- pretty_midi
- TensorFlow/Keras
- Common Python utility libraries

Dataset:
- MAESTRO dataset contains multiple MIDI files with numerous piano notes
- We are using maestro-v2.0.0-midi.zip from [https://magenta.tensorflow.org/datasets/maestro#v200](link)