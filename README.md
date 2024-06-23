# Fine-tuning-CNN-LSTM-Model for Gold Price Fluctuation Prediction
- dataset in the data directory
- draw_cm.py is used to draw confusion matrix
- In the Fine_tuned_cnn_lstm_gold_price.ipynb, I removed models other than CNN-LSTM and added dropout layer when type==3
- In the final.ipynb, I modified the data type, modified the time series to binary data format (0 or 1) and modified the model compilation to binary, adding the dropout layer

# How to run
  All jupyter notebooks can be run, please make sure the environment is installed correctly
- final.ipynb shows the preprocessed dataset and fine-tuned model, using the model for price volatility prediction (classification task)
- cnn_lstm_gold_price.ipynb shows the original model (with minor modifications) for the price prediction task, and model 3 with a dropout layer added

Click 'Run All' to easily run the code.
