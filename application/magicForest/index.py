import sys
sys.path.append('modules/cutImages')
sys.path.append('modules/magicForest')
from modules.cutImages import cutImages
from modules.magicForest import magicForest

folderImages = cutImages('../uploads/img.tif', 6)
magicForest(folderImages)
