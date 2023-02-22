#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii Inc. All rights reserved.

import cv2
import numpy as np

__all__ = ["vis"]


def vis(img, boxes, scores, cls_ids, conf=0.5, class_names=None):
        
    #print(img.shape)

    for i in range(len(boxes)):
        box = boxes[i]
        #print("The bounding box values are : ", box)
        cls_id = int(cls_ids[i])
        score = scores[i]
        if score < conf:
            continue
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(box[2])
        y1 = int(box[3])

        '''
        x_diff = x1 - x0 
        y_diff = y1 - y0 

        if (x_diff > y_diff):

            point_1 = (x0, int(y0 + y_diff/2))
            point_2 = (x1, int(y1-y_diff/2))

        else:

            if (x0-x_diff <= 0):

                point_1 = (x0, int(y0+y_diff))
                point_2 = (x1, int(y1+y_diff/2))

            else:
                point_1 = (x1, y1)
                point_2 = (x0-y_diff, y1)                    

        
        if (y0 > y1):
            small_point = (x1, y1)
            large_point = (x0, y0)

            x_diff = x0-x1
            y_diff = y0-y1

            maximum = max(x_diff,y_diff)

            if (x0-maximum < 0):

                point = (x0+maximum, y1)

            else:
                point = (x0-maximum, y1)    

        if ( y0 < y1):
            small_point = (x0, y0) 
            large_point = (x1, y1)

            x_diff = x1-x0
            y_diff = y1 - y0

            maximum = max(x_diff, y_diff)

            if (x1-maximum < 0 and y1 - y0 < 300):
                
                point = (x1+maximum, y0)

            if (x1-maximum < 0 and y1 - y0 > 300):

                point = (x1+maximum, y1)

            if (x1-maximum > 0 and y1 - y0 < 300):
                
                point = (x1-maximum, y0)

            if (x1-maximum > 0 and y1 - y0 > 300):

                point = (x1-maximum, y1)         
        '''

        color = (_COLORS[cls_id] * 255).astype(np.uint8).tolist()
        text = '{}:{:.1f}%'.format(class_names[cls_id], score * 100)
        
        if cls_id == 1 or cls_id == 2 or cls_id == 3:
            text = f'ALERT: Missing {missing[cls_id]}'
        else:
            text = ''
        
        txt_color = (0, 0, 0) if np.mean(_COLORS[cls_id]) > 0.5 else (255, 255, 255)
        font = cv2.FONT_HERSHEY_SIMPLEX

        txt_size = cv2.getTextSize(text, font, 0.4, 1)[0]
        cv2.rectangle(img, (x0, y0), (x1, y1), color, 2)

        txt_bk_color = (_COLORS[cls_id] * 255 * 0.7).astype(np.uint8).tolist()
        cv2.rectangle(
            img,
            (x0, y0 + 1),
            (x0 + txt_size[0] + 1, y0 + int(1.5*txt_size[1])),
            txt_bk_color,
            -1
        )
        cv2.putText(img, text, (x0, y0 + txt_size[1]), font, 0.4, txt_color, thickness=1)

        #cv2.circle(img, (x0, y0), radius =10, color = (255, 255, 0), thickness = 2)

        #cv2.circle(img, (x1, y1), radius = 10, color = (255, 255, 0), thickness = 2)

        #cv2.line(img, point_1, point_2, (255,255,0), thickness = 4)

    return img


"""_COLORS = np.array(
    [
        0.000, 0.447, 0.741,
        0.850, 0.325, 0.098,
        0.929, 0.694, 0.125,
        0.494, 0.184, 0.556,
        0.466, 0.674, 0.188,
        0.301, 0.745, 0.933,
        0.635, 0.078, 0.184,
        0.300, 0.300, 0.300,
        0.600, 0.600, 0.600,
        1.000, 0.000, 0.000,
        1.000, 0.500, 0.000,
        0.749, 0.749, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 1.000,
        0.667, 0.000, 1.000,
        0.333, 0.333, 0.000,
        0.333, 0.667, 0.000,
        0.333, 1.000, 0.000,
        0.667, 0.333, 0.000,
        0.667, 0.667, 0.000,
        0.667, 1.000, 0.000,
        1.000, 0.333, 0.000,
        1.000, 0.667, 0.000,
        1.000, 1.000, 0.000,
        0.000, 0.333, 0.500,
        0.000, 0.667, 0.500,
        0.000, 1.000, 0.500,
        0.333, 0.000, 0.500,
        0.333, 0.333, 0.500,
        0.333, 0.667, 0.500,
        0.333, 1.000, 0.500,
        0.667, 0.000, 0.500,
        0.667, 0.333, 0.500,
        0.667, 0.667, 0.500,
        0.667, 1.000, 0.500,
        1.000, 0.000, 0.500,
        1.000, 0.333, 0.500,
        1.000, 0.667, 0.500,
        1.000, 1.000, 0.500,
        0.000, 0.333, 1.000,
        0.000, 0.667, 1.000,
        0.000, 1.000, 1.000,
        0.333, 0.000, 1.000,
        0.333, 0.333, 1.000,
        0.333, 0.667, 1.000,
        0.333, 1.000, 1.000,
        0.667, 0.000, 1.000,
        0.667, 0.333, 1.000,
        0.667, 0.667, 1.000,
        0.667, 1.000, 1.000,
        1.000, 0.000, 1.000,
        1.000, 0.333, 1.000,
        1.000, 0.667, 1.000,
        0.333, 0.000, 0.000,
        0.500, 0.000, 0.000,
        0.667, 0.000, 0.000,
        0.833, 0.000, 0.000,
        1.000, 0.000, 0.000,
        0.000, 0.167, 0.000,
        0.000, 0.333, 0.000,
        0.000, 0.500, 0.000,
        0.000, 0.667, 0.000,
        0.000, 0.833, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 0.167,
        0.000, 0.000, 0.333,
        0.000, 0.000, 0.500,
        0.000, 0.000, 0.667,
        0.000, 0.000, 0.833,
        0.000, 0.000, 1.000,
        0.000, 0.000, 0.000,
        0.143, 0.143, 0.143,
        0.286, 0.286, 0.286,
        0.429, 0.429, 0.429,
        0.571, 0.571, 0.571,
        0.714, 0.714, 0.714,
        0.857, 0.857, 0.857,
        0.000, 0.447, 0.741,
        0.314, 0.717, 0.741,
        0.50, 0.5, 0
    ]
).astype(np.float32).reshape(-1, 3)"""

_COLORS = np.array(
    [
        0.000, 1.000, 0.000,    # Green - both helmet and jacket found
        0.000, 0.000, 1.000,    # green - if helmet is found
        1.000, .000, 0.000,    # green - if jacket is found
        1.000, 1.000, 0.000    #orange - if nothing is found
    ]
).astype(np.float32).reshape(-1, 3)


missing = {1 : 'Vest', 
           2 : 'Helmet',
           3 : 'Helmet & Vest'}
