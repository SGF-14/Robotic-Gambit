# MachineLearning.py
# import tensorflow.keras.models as models
# import tensorflow.keras.layers as layers

# import tensorflow.keras.utils as utils ((delete))

# import numpy
# import tensorflow.keras.optimizers as optimizers
# import tensorflow.keras.callbacks as callbacks
import chess.engine
import chess.svg
import cairosvg
from .ChessBoard import get_board, get_board_png, update_fen_in_database
# from .ComputerVision import capture_initial_frame
# from .ComputerVision import capture_initial_frame

from .FrameManagement import capture_initial_frame

# Use capture_initial_frame where needed to prepare for AI processing

# Temp stockfish 
# engine_path = r"app/stockfish-windows-x86-64-avx2.exe"
# engine = chess.engine.SimpleEngine.popen_uci(engine_path)

def make_ai_move():
    from .ChessBoard import get_board  
    from .FrameManagement import capture_initial_frame
    
    board = get_board()
    print(board)
    engine_path = r"app/stockfish-windows-x86-64-avx2.exe"
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    
    
    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=2.0))
        if result.move in board.legal_moves:
            board.push(result.move)  
            capture_initial_frame()  
            print(board)
        else:
            print(f"AI attempted illegal move: {result.move.uci()}")
    else:
        print("Game is over, no move made")
        print(board)
    update_fen_in_database()
    engine.quit()  


# def build_model(conv_size=32, conv_depth=4):
#     board3d = layers.Input(shape=(14, 8, 8))

#     # adding the convolutional layers
#     x = board3d
#     for _ in range(conv_depth):
#         x = layers.Conv2D(filters=conv_size, kernel_size=3, padding='same', activation='relu')(x)

#     x = layers.Flatten()(x)


#     x = layers.Dense(64, activation='relu')(x)
#     x = layers.Dense(1, activation='sigmoid')(x)

#     return models.Model(inputs=board3d, outputs=x)

# model = build_model(32, 4)

# def build_model_residual(conv_size, conv_depth):
#     board3d = layers.Input(shape=(14, 8, 8))

#     # adding the convolutional layers
#     x = layers.Conv2D(filters=conv_size, kernel_size=3, padding='same', data_format='channels_last')(x)
#     for _ in range(conv_depth):
#         previous = x
#         x = layers.Conv2D(filters=conv_size, kernel_size=3, padding='same', data_format='channels_last')(x)
#         x = layers.BatchNormalization()(x)
#         x = layers.Activation('relu')(x)
#         x = layers.Conv2D(filters=conv_size, kernel_size=3, padding='same', data_format='channels_last')(x)
#         x = layers.BatchNormalization()(x)
#         x = layers.Add()([x, previous])
#         x = layers.Activation('relu')(x)
#     x = layers.Flatten()(x)
#     x = layers.Dense(1, 'sigmoid')(x)

#     return models.Model(inputs=board3d, outputs=x)



# def get_dataset():
#     container = numpy.load('dataset.npz')
#     b, v = container['positions'], container['scores']
#     v = numpy.asarray(v / abs(v).max() / 2 + 0.5, dtype=numpy.float32)  # normalization
#     return b, v

# x_train, y_train = get_dataset()
# print(x_train.shape)
# print(y_train.shape)

# model.compile(optimizer=optimizers.Adam(5e-4), loss='mean_squared_error')
# model.summary()

# model.fit(x_train, y_train,
#           batch_size=2048,
#           epochs=200, #was 1000
#           verbose=1,
#           validation_split=0.1,
#           callbacks=[callbacks.ReduceLROnPlateau(monitor='loss', patience=10),
#                      callbacks.EarlyStopping(monitor='loss', patience=15, min_delta=0)])

# model.save('model.keras')

