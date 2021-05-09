import numpy as np


left_keypoints = [13, 11, 23]
right_keypoints = [14, 12, 24]
DECISION_ANGLE = 60.


def is_visible(landmarks):
  for ldmk in landmarks:
    if ldmk.visibility < 0.8:
      return False
  return True


def get_angle(landmarks):
  p1 = np.array([landmarks[0].x, landmarks[0].y])
  p2 = np.array([landmarks[1].x, landmarks[1].y])
  p3 = np.array([landmarks[2].x, landmarks[2].y])

  u = p1 - p2  
  v = p3 - p2

  cosine =  np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
  angle = np.arccos(cosine)
  
  return np.degrees(angle)


def is_catching_a_taxi(landmarks):
  lefts = [landmarks[lk] for lk in left_keypoints]
  rights = [landmarks[rk] for rk in right_keypoints]
  
  if not is_visible(lefts) and not is_visible(rights):
    return False
  
  if is_visible(lefts) and is_visible(rights):
    angle = max(get_angle(lefts), get_angle(rights))
  elif is_visible(lefts):
    angle = get_angle(lefts)
  else:
    angle = get_angle(rights)
  
  if angle > DECISION_ANGLE:
    return True
  return False
