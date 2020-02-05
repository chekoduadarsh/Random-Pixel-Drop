import numpy as np
import random

def get_random_pixel_drop(Drop_num = 50, l_rand_bound = 0, u_rand_bound = 255):
    def eraser(input_img):
        img_h, img_w, img_c = input_img.shape

        for drop in range(Drop_num):
            rand_x = random.randint(0,img_h-1)
            rand_y = random.randint(0,img_w-1)
            #rand_c = random.randint(0,img_c-1)
            left = np.random.randint(0, img_w)
            top = np.random.randint(0, img_h)
            c = random.randint(l_rand_bound,u_rand_bound)

            input_img[rand_x, rand_y, :]= c

        return input_img

    return eraser
