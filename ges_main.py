import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
import cv2
import numpy as np

old_list = [1,2,3]


def change_password():
    # Function to change the password
    new_password = input("Enter new password: ")
    if len(new_password) > 7:
        return new_password
    else:
        return "Your password is not strong."


def main():
    # Initialize camera
    import main as m
    var = m.pred_ges()
    print("Alternative method returned sequence:", var)

    if var == old_list:
        new_password = change_password()
        print("Password changed successfully:", new_password)
    else:
        print("Authentication failed with alternative method.")
    

if __name__ == "__main__":
    main()