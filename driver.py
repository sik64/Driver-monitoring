import cv2
import mediapipe as mp
import math
import serial
import time

py_serial = serial.Serial(port='COM3',baudrate=9600,)
sign_old = 'o'

def distance(x1,y1,x2,y2):
    x_diff = x2 - x1
    y_diff = y2 - y1
    distance = math.sqrt((x_diff**2)+(y_diff**2))
    return distance
def serial_vibe(sign):
    commend = sign
    py_serial.write(commend.encode())
    time.sleep(0.1)
def flip_x(x,window_width):
    return 2*window_width-x
    #영상 좌우반전 후 x좌표 반전시키기 위한 함수

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        #for i in range(1):
        success, image = cap.read()
        if not success:
            print("웹캠을 찾을 수 없습니다.")
            # 비디오 파일의 경우 'continue'를 사용하시고, 웹캠에 경우에는 'break'를 사용하세요
            break

        # 필요에 따라 성능 향상을 위해 이미지 작성을 불가능함으로 기본 설정합니다.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # 이미지 위에 얼굴 그물망 주석을 그립니다.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style())
        points = []
        if results.multi_face_landmarks:
            for landmark in results.multi_face_landmarks:
                # print(enumerate(landmark.landmark))
                for id, lm in enumerate(landmark.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    points.append([cx,cy])
                    #print(id, " :", cx, cy)

        image = cv2.resize(image, None, None, 2, 2, cv2.INTER_CUBIC)
        # 영상크기를 2배로 resize
        image = cv2.flip(image, 1)
        #이미지 좌우반전
        #cv2.putText(image, 'ESC to quit', (50,50), 0, 1, (255, 255, 0), 1)

        try:  # 객체가 화면밖으로 나갔을 때, 에러로부터 보호되는 코드부분
            key_points = [159, 145, 386, 374, 33, 133, 362, 263]
            # 눈 깜박임 판단에 사용되는 핵심 랜드마크
            for i in key_points:
                x, y = points[i][0], points[i][1]
                cv2.circle(image, ( flip_x(2 * x,w), 2 * y), 5, (255, 0, 0), -1)
                cv2.putText(image, f'{i}:({2 * x},{2 * y})', (flip_x(2 * x+30,w), 2 * y), 0, 0.4, (255, 0, 0), 1)
                #핵심 랜드마크 인덱스와 좌표 표기

            x1, y1 = points[159][0], points[159][1] # 랜드마크 159
            x2, y2 = points[145][0], points[145][1] # 랜드마크 145
            sx1,sy1 = points[33][0], points[33][1] # 랜드마크 33
            sx2,sy2 = points[133][0], points[133][1] # 랜드마크 133

            cv2.line(image, (flip_x(x1 * 2,w), y1 * 2), (flip_x(x2 * 2,w), y2 * 2), (255, 0, 221), 2, lineType=None, shift=None)
            cv2.line(image, (flip_x(sx1 * 2,w), sy1 * 2), (flip_x(sx2 * 2,w), sy2 * 2), (255, 0, 221), 2, lineType=None, shift=None)

            r_dis = distance(x1, y1, x2, y2) # distance of line 159 to 145
            r_side_dis = distance(sx1,sy1,sx2,sy2) # distance of line 33 to 133
            r_ratio = round(r_dis / r_side_dis, 2) # 오른쪽 눈 감은 비율

            font_size = r_side_dis / 40 #카메라와 눈 거리에 비례한 폰트사이즈
            if font_size > 1 : font_size = 1

            cv2.putText(image, f'(R)Latio: {r_ratio}',(flip_x(points[67][0] * 2+80 ,w), points[67][1] * 2 - 20), 0, font_size, (0, 255, 255), 2)

            if r_ratio < 0.2:
                cv2.putText(image, 'Right closed', (flip_x(points[67][0]*2+80,w), points[67][1]*2-60), 0, font_size, (0, 0, 255), 2)
                # 눈 감은 비율이 0.2 미만 일때 closed 판단
            else:
                cv2.putText(image, "Right :{:.2f}".format(r_dis), (flip_x(points[67][0]*2+80,w), points[67][1]*2-60), 0, font_size, (255, 0, 0), 2)

            a1, b1 = points[386][0], points[386][1] # 랜드마크 386
            a2, b2 = points[374][0], points[374][1] # 랜드마크 374
            sa1, sb1 = points[362][0], points[362][1] # 랜드마크 362
            sa2, sb2 = points[263][0], points[263][1] # 랜드마크 263

            cv2.line(image, (flip_x(a1 * 2,w), b1 * 2), (flip_x(a2 * 2,w), b2 * 2), (255, 0, 221), 2, lineType=None, shift=None)
            cv2.line(image, (flip_x(sa1 * 2,w), sb1 * 2), (flip_x(sa2 * 2,w), sb2 * 2), (255, 0, 221), 2, lineType=None, shift=None)

            l_dis = distance(a1, b1, a2, b2) # distance of line 386 to 374
            l_side_dis = distance(sa1, sb1, sa2, sb2) # distance of line 362 to 263
            l_ratio = round(l_dis/l_side_dis,2) # 왼쪽 눈 감은 비율

            cv2.putText(image, f'(L)Latio: {l_ratio}', (flip_x(points[297][0] * 2+80,w), points[297][1] * 2 - 20), 0, font_size, (0, 255, 255), 2)

            if l_ratio < 0.2:
                cv2.putText(image, 'Left closed', (flip_x(points[297][0]*2+80,w), points[297][1]*2-60), 0, font_size, (0, 0, 255), 2)
                # 눈 감은 비율이 0.2 미만 일때 closed 판단
            else:
                cv2.putText(image, "LEFT :{:.2f}".format(l_dis), (flip_x(points[297][0]*2+80,w), points[297][1]*2-60), 0, font_size, (255, 0, 0), 2)

            if r_ratio < 0.2 and l_ratio < 0.2:
                sign ='c'
                # 모든 눈이 감겨있을시, sign변수 'c'(closed) 로 변경
            else:
                sign = 'o'
                # 그렇지 않으면 sign = 'o'(opened)

        except:  # 에러가 발생하면 실행되는 부분
            sign = 'o'
            pass

        cv2.namedWindow('Mediapipe eyes check', flags=cv2.WINDOW_NORMAL)
        cv2.imshow('Mediapipe eyes check', image)

        if sign != sign_old:
            sign_old = sign
            serial_vibe(sign)
            # sign 변수가 'o' 또는 'c'로 변경시 시리얼통신으로 아두이노로 sign신호 전달

        if sign == 'c': print('Eyes closed')
        else : print('---')

        if cv2.waitKey(5) & 0xFF == 27:
            # ESC 누를 시 break 후 윈도우 종료
            break

cap.release()
cv2.destroyAllWindows()
# 윈도우 창 종료

#cv2.waitKey()
