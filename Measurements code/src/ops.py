"""
TF util operations.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def keypoint_l1_loss(kp_gt, kp_pred, scale=1., name=None):
    with tf.name_scope(name, "keypoint_l1_loss", [kp_gt, kp_pred]):
        kp_gt = tf.reshape(kp_gt, (-1, 3))
        kp_pred = tf.reshape(kp_pred, (-1, 2))

        vis = tf.expand_dims(tf.cast(kp_gt[:, 2], tf.float32), 1)
        res = tf.losses.absolute_difference(kp_gt[:, :2], kp_pred, weights=vis)
        return res


def compute_3d_loss(params_pred, params_gt, has_gt3d):
    with tf.name_scope("3d_loss", [params_pred, params_gt, has_gt3d]):
        weights = tf.expand_dims(tf.cast(has_gt3d, tf.float32), 1)
        res = tf.losses.mean_squared_error(
            params_gt, params_pred, weights=weights) * 0.5
        return res


def align_by_pelvis(joints):
    """
    Assumes joints is N x 14 x 3 in LSP order.
    Then hips are: [3, 2]
    Takes mid point of these points, then subtracts it.
    """
    with tf.name_scope("align_by_pelvis", [joints]):
        left_id = 3
        right_id = 2
        pelvis = (joints[:, left_id, :] + joints[:, right_id, :]) / 2.
        return joints - tf.expand_dims(pelvis, axis=1)
