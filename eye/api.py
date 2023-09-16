# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def testing():
#     return {"message": "Hello, World!"}


# app.run(host="0.0.0.0", port=5000, debug=True)

import math

import cv2
import json
import numpy as np

GAZE_DEPTH = 0.6

class GazeProjector:

    def __init__(self, config_file):
        '''Load the camera configs from a JSON file'''
        with open(config_file, 'r') as json_file:
            config_data = json.load(json_file)

        self._camera_mtx = np.array(config_data['mtx'])
        self._camera_dist = np.array(config_data['dist'])
        self._height, self._width = config_data['resolution']['data']
        
        self._trans = self._compute_transformation_matrix((0.0683000000000028, 0.0163349459352645, 0.00282292669066985),
            (-12.000000000000043, 0.0, 0.0))
        self._invtrans = np.linalg.inv(self._trans)

    def project_gaze(self, xvec, yvec, zvec, _vergence):
        ''' Handle the new gaze samples '''
        # project the gaze onto the image
        gaze_img = self._project_gaze((xvec, yvec, zvec), GAZE_DEPTH)
        return gaze_img

    def _project_gaze(self, vector, gaze_depth):
        ''' Project the gaze vector onto the image. Ignore the depth argument if parallax correction is active '''
        depth_corrector = gaze_depth / np.abs(vector[2])
        gaze_vec_rel_eye = np.array(vector) * depth_corrector

        gaze_vec_rel_cam = self._invtrans @ np.append(gaze_vec_rel_eye, 1)
        gaze_vec_rel_cam = (gaze_vec_rel_cam / gaze_vec_rel_cam[3])[0:3]
        points, _ = cv2.projectPoints(gaze_vec_rel_cam,
                                      np.array([[0., 0., 0.]]), np.array([0., 0., 0.]),
                                      self._camera_mtx,
                                      self._camera_dist)
        gaze_xy = points[0][0]
        # ignore the coordinates outside the image range
        x_in_range = 0 < gaze_xy[0] < self._width
        y_in_range = 0 < gaze_xy[1] < self._height
        if not (x_in_range and y_in_range):
            gaze_xy = np.full(2, np.nan)

        if self._trans[0][0] < 0:
            gaze_xy[0] = self._width - gaze_xy[0]
            gaze_xy[1] = self._height - gaze_xy[1]
        return gaze_xy

    @staticmethod
    def _compute_transformation_matrix(translation, rotation):
        '''
        Generate camera transformation matrix (XYZ Tait–Bryan matrix)
        '''
        trans_x, trans_y, trans_z = translation
        rotation_x, rotation_y, rotation_z = np.radians(rotation)
        # Align the camera CS with world camera CS. It's ok to modify x here since we are using XYZ order
        rotation_x += np.pi
        return np.array([[math.cos(rotation_z) * math.cos(rotation_y),
                        -math.cos(rotation_y) * math.sin(rotation_z),
                        math.sin(rotation_y),
                        trans_x],
                        [math.cos(rotation_x) * math.sin(rotation_z) + math.sin(rotation_x) * math.sin(rotation_y) *
                        math.cos(rotation_z),
                        math.cos(rotation_x) * math.cos(rotation_z) - math.sin(rotation_x) * math.sin(rotation_y) *
                        math.sin(rotation_z),
                        -math.sin(rotation_x) * math.cos(rotation_y),
                        trans_y],
                        [math.sin(rotation_x) * math.sin(rotation_z) - math.cos(rotation_x) * math.sin(rotation_y) *
                        math.cos(rotation_z),
                        math.sin(rotation_x) * math.cos(rotation_z) + math.cos(rotation_x) * math.sin(rotation_y) *
                        math.sin(rotation_z),
                        math.cos(rotation_x) * math.cos(rotation_y),
                        trans_z],
                        [0., 0., 0., 1.]])
    
gaze_proj = GazeProjector('config.json')

def _gaze_handler(x, y, z, vergence):
    gaze_in_image = gaze_proj.project_gaze(x, y, z, vergence)