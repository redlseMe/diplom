from deepforest import main
from matplotlib import pyplot
import os

def magicForest(folder_path):
    m = main.deepforest()
    m.use_release()
    countForest = 0

    result_folder = 'result'
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            imagePath = folder_path + '/' + file_name
            predicted_raster = m.predict_image(path=imagePath, return_plot=True)
            countForest += len(predicted_raster)
            print(len(predicted_raster))
            image_name = f"{os.path.splitext(file_name)[0]}_result.png"
            image_path = os.path.join(result_folder, image_name)
            pyplot.imsave(image_path, predicted_raster)

    print(f"Общее количество деревьев: {countForest}")