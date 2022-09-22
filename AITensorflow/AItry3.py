import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import os
from PIL import Image
import gdown
import tensorflow as tf

import argparse
import numpy as np
from keras.layers import Conv2D, Input, BatchNormalization, LeakyReLU, ZeroPadding2D, UpSampling2D
from keras.layers.merge import add, concatenate
from keras.models import Model
import struct
import cv2
from copy import deepcopy