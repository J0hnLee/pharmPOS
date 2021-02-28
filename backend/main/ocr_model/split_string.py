import os
import cv2
import numpy as np


class Split:
    def __init__(self, input, output=None):
        self.file_name = input
        self.output_dir = output
        self.min_val = 10
        self.min_range = 30
        self.count = 0
        self.vertical_peek_ranges2d = []

    def extract_peek(self, array_vals, minimun_val, minimun_range):
        start_i = None
        end_i = None
        peek_ranges = []
        for i, val in enumerate(array_vals):
            if val > minimun_val and start_i is None:
                start_i = i
            elif val > minimun_val and start_i is not None:
                pass
            elif val < minimun_val and start_i is not None:
                if i - start_i >= minimun_range:
                    end_i = i
                    # print(end_i - start_i)
                    peek_ranges.append((start_i, end_i))
                    start_i = None
                    end_i = None
            elif val < minimun_val and start_i is None:
                pass
            else:
                raise ValueError("cannot parse this case...")
        return peek_ranges

    def cutImage(self, img, peek_range):
        img_list = []
        for i, peek_range in enumerate(self.peek_ranges):
            for vertical_range in self.vertical_peek_ranges2d[i]:
                x = vertical_range[0]
                y = peek_range[0]
                w = vertical_range[1] - x
                h = peek_range[1] - y
                pt1 = (x, y)
                pt2 = (x + w, y + h)
                self.count += 1
                img1 = img[y:peek_range[1], x:vertical_range[1]]
                new_shape = (150, 150)
                img1 = cv2.resize(img1, new_shape)
                # cv2.imwrite(self.output_dir + '/' + str(self.count) + ".png", img1)
                # cv2.rectangle(img, pt1, pt2, color)
                img_list.append(img1)

        return img_list

    def split(self):
        img = cv2.imread(self.file_name)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                                   cv2.THRESH_BINARY_INV, 15, 2)
        horizontal_sum = np.sum(adaptive_threshold, axis=1)
        self.peek_ranges = self.extract_peek(horizontal_sum, self.min_val, self.min_range)
        line_seg_adaptive_threshold = np.copy(adaptive_threshold)
        for i, peek_range in enumerate(self.peek_ranges):
            x = 0
            y = peek_range[0]
            w = line_seg_adaptive_threshold.shape[1]
            h = peek_range[1] - y
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            cv2.rectangle(line_seg_adaptive_threshold, pt1, pt2, 255)

        for peek_range in self.peek_ranges:
            start_y = peek_range[0]
            end_y = peek_range[1]
            line_img = adaptive_threshold[start_y:end_y, :]
            vertical_sum = np.sum(line_img, axis=0)
            vertical_peek_ranges = self.extract_peek(
                vertical_sum, self.min_val, self.min_range)
            self.vertical_peek_ranges2d.append(vertical_peek_ranges)
        return self.cutImage(adaptive_threshold, peek_range)


if __name__ == "__main__":
    a = Split('./input/test6.png', './result')
    l = a.split()