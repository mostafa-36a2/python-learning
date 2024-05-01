import threading

import cv2


def monitor(*args):
    print("monitor", args)
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open camera")
        exit()

    left = 300
    width = 150
    top = 170
    height = 170

    # Loop to continuously capture frames
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting...")
            break

        original_img = frame
        img = original_img.copy()
        hh, ww = img.shape[:2]
        # print(hh, ww)
        max_hh_ww = max(hh, ww)

        # illumination normalize
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

        # separate channels
        y, cr, cb = cv2.split(ycrcb)

        sigma = int(5 * max_hh_ww / 300)
        # print("sigma: ", sigma)
        gaussian = cv2.GaussianBlur(y, (0, 0), sigma, sigma)

        crop_img = img[left : left + width, top : top + height]

        cv2.imshow(
            "converted",
            img,
            # cv2.resize(img, tuple([s * 3 for s in img.shape[:2]])).astype(np.uint8),
        )

        crop_img = cv2.rotate(crop_img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("crop_img", crop_img)

        # Check for key press, if 'q' is pressed, exit the loop
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        # top
        elif k == ord("q"):
            top = min(480, top + 10)
            print(f"l pressed top = {top}")
        elif k == ord("e"):
            top = max(0, top - 10)
            print(f"top = {top}")
        # left
        elif k == ord("z"):
            left = min(640, left + 10)
            print(f"l pressed left = {left}")
        elif k == ord("c"):
            left = max(0, left - 10)
            print(f"left = {left}")
        # height
        elif k == ord("w"):
            height = min(200, height + 10)
            print(f"l pressed height = {height}")
        elif k == ord("s"):
            height = max(0, height - 10)
            print(f"height = {height}")
        # width
        elif k == ord("a"):
            width = min(200, width + 10)
            print(f"l pressed width = {width}")
        elif k == ord("d"):
            width = max(0, width - 10)
            print(f"width = {width}")
        elif k == ord(" "):
            print(
                f"""
                    left = {left}
                    width = {width}
                    top = {top}
                    height = {height}
                """
            )

    # Release the capture
    cap.release()


def main(*args):
    print("main", args)


if __name__ == "__main__":
    t1 = threading.Thread(target=monitor, args=(10,))
    t2 = threading.Thread(target=main, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
