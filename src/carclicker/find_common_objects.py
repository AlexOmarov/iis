from imageai.Detection import ObjectDetection

# Works only with Tensorflow <=1.5
image_path = "../../../facecontrol/resources/static/img/carclicker/"
# You should get retina file from here
# https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5
retina_path = "../../resources/static/retina/resnet50_coco_best_v2.0.1.h5"
image_path_donut = image_path + "donut.jpg"
image_path_donuts = image_path + "donuts.jpg"
image_path_last_supper = image_path + "last_supper.jpg"
image_path_last_supper_output = image_path + "lsoutput.jpg"
image_path_donuts_output = image_path + "dsoutput.jpg"
image_path_donut_output = image_path + "doutput.jpg"


def find_objects(image_input_path, image_output_path, image_name):
    detections = detector.detectObjectsFromImage(input_image=image_input_path,
                                                 output_image_path=image_output_path)
    print("Objects found on the " + image_name + ": ")
    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"])


detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(retina_path)
detector.loadModel()
find_objects(image_path_last_supper, image_path_last_supper_output, "Last Supper")
find_objects(image_path_donuts, image_path_donuts_output, "Donuts")
find_objects(image_path_donut, image_path_donut_output, "Donut")
