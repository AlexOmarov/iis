import cv2 as cv
import argparse

global isDrawing
global start_coords
global storage


# Classes
class CommandStorage:
    storage = []

    def to_string(self):
        print("Command storage state: ")
        for i, command in enumerate(self.storage):
            print("Command " + str(i) + ": X1:{0} Y1:{1} X2:{2} Y2:{3}".format(command.x1,
                                                                               command.y1,
                                                                               command.x2,
                                                                               command.y2))

    def revert_last(self):
        if len(self.storage) > 0:
            return self.storage[-1].revert()
        return None

    def apply(self, command, local_image):
        command.apply(local_image, self.storage)


class Command:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    image = None
    storage = None

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def to_string(self):
        return "X1:{0} Y1:{1} X2:{2} Y2:{3}".format(self.x1, self.y1, self.x2, self.y2)

    def apply(self, local_image, local_storage):
        self.image = local_image.copy()
        self.storage = local_storage
        self.storage.append(self)
        print("Drawing")
        cv.rectangle(local_image,
                     (int(self.x1), int(self.y1)),
                     (int(self.x2), int(self.y2)),
                     (255, 255, 0), 2)
        print("End coords: {} * {}".format(self.x2, self.y2))
        view_image(local_image, "image")

    def revert(self):
        self.storage.remove(self)
        print("Revert command " + self.to_string())
        return self.image


# Static Functions
def shape_selection(event, x, y, flags, param):
    global isDrawing
    global start_coords
    if event == cv.EVENT_LBUTTONDOWN:
        isDrawing = True
        start_coords = [x, y]
        print("Start coords: {} * {}".format(x, y))
    if event == cv.EVENT_LBUTTONUP:
        if isDrawing:
            isDrawing = False
            storage.apply(Command(start_coords[0], start_coords[1], int(x), int(y)), param[0])


def view_image(img, name_of_window):
    cv.destroyWindow("image")
    cv.namedWindow(name_of_window, cv.WINDOW_AUTOSIZE)
    cv.setMouseCallback("image", shape_selection, (img, name_of_window))
    cv.imshow(name_of_window, img)
    key = cv.waitKey(0)

    # press 'r' to reset the window
    if key == ord("r"):
        storage.storage.clear()
        view_image(clone, "image")

    # if the 'esc' key is pressed, cancel command
    elif key == 27:
        reverted_image = storage.revert_last()
        if reverted_image is not None:
            view_image(reverted_image, "image")
        else:
            print("There are no commands to revert")
            view_image(img, "image")
    # if the 'l' key is pressed, show applied commands
    elif key == ord("l"):
        storage.to_string()
        view_image(img, "image")
        # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        cv.destroyAllWindows()


# App

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
image = cv.imread(vars(ap.parse_args())["image"])
clone = image.copy()
storage = CommandStorage()
view_image(clone, "image")
